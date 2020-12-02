from django.db.models import Q
from .models import SearchTerm, Post
import secrets
import string

TRACKING_ID_SESSION_KEY = 'tracking_id'

STRIP_WORDS = ['a', 'an', 'and', 'by', 'for', 'from', 'in', 'no', 'not',
               'of', 'on', 'or', 'that', 'the', 'to', 'with']


def tracking_id(request):
    """ get the current user's tracking_id, sets new one if blank;
    Note: the syntax below matches the text, but an alternative,
    clearer way of checking for a tracking_id would be the following:

    if not TRACKING_ID_SESSION_KEY in request.session:

    """
    if request.session.get(TRACKING_ID_SESSION_KEY, '') == '':
        request.session[TRACKING_ID_SESSION_KEY] = _generate_tracking_id()
    return request.session[TRACKING_ID_SESSION_KEY]


def _generate_tracking_id():
    """ function for generating secure random tracking ID values """
    tracking_id_length = 48
    characters = string.ascii_letters + string.digits + string.punctuation
    tracking_id = ''.join((secrets.choice(characters)
                           for _ in range(tracking_id_length)))
    return tracking_id


def get_client_ip(request):
    X_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if X_forwarded_for:
        ip = X_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def store(request, query):
    """ stores the search text """
    # if search term is at least three chars long, store in db
    if len(query) > 2:
        term = SearchTerm()
        term.query = query
        term.ip_address = get_client_ip(request)
        term.tracking_id = tracking_id(request)
        term.user = None
        if request.user.is_authenticated:
            term.user = request.user
        term.save()
# get products matching the search texts


def posts(search_text):
    words = _prepare_words(search_text)
    products = Post.published.all()
    results = {}
    results['posts'] = []
    # iterate through keywords
    for word in words:
        posts = products.filter(Q(title__icontains=word)
                                | Q(body__icontains=word))
        results['posts'] = posts
    return results


def _prepare_words(search_text):
    """ strip out common words, limit to 5 words """
    words = search_text.split()
    for common in STRIP_WORDS:
        if common in words:
            words.remove(common)
    return words[0:100]
