
from .forms import SearchForm


def devc(request):
    """ context processor for the site templates """
    query = request.GET.get('query', '')
    search_form = SearchForm({'query': query})
    return {

        'search_form': search_form,
    }
