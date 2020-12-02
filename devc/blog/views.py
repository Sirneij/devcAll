from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from hitcount.views import HitCountDetailView
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, UpdatePostForm, CommentForm
from django.template.loader import render_to_string
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity

def blog_index(request, tag_slug=None):
    object_list = Post.published.all()
    if request.user.is_staff or request.user.is_superuser:
        object_list = Post.objects.all()
    common_tags = Post.tags.most_common()[:2]
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 5) # 5 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    context = {
        'page': page, 
        'posts': posts, 
        'tag': tag, 
        'common_tags': common_tags,
        }
    return render(request, 'blog/index.html', context)

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    post_tags_ids = post.tags.values_list('id', flat=True)
    # is_ovated = False
    # if post.ovation.filter(id=request.user.id).exists():
    #     is_ovated = True
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','-publish')[:4]
    form = CommentForm(request.POST or None)
    parent = form['parent'].value()
    if request.method == "POST":
        if form.is_valid():
            temp = form.save(commit=False)
            temp.post = post
            temp.author = request.user
            
            if parent == '':
                #Set a blank path then save it to get an ID
                temp.path = []
                temp.save()
                temp.path = [temp.id]
            else:
                #Get the parent node
                node = Comment.objects.get(id=parent)
                temp.depth = node.depth + 1
                temp.path = node.path
                
                #Store parents path then apply comment ID
                temp.save()
                temp.path.append(temp.id)
                
            #Final save for parents and children
            temp.save()
            return redirect(post.get_absolute_url()) 
    
    #Retrieve all comments and sort them by path
    comment_tree = Comment.objects.filter(post=post).order_by('path')
    if request.is_ajax():
        html = render_to_string('comments/index.html', locals(), request=request)
        return JsonResponse({'form': html})
    return render(request, 'blog/post_detail.html', locals())
@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.slug = slugify(newpost.title)
            # newpost.author = request.user
            newpost.save()
            messages.success(
                request, f'A new post has successfully been added!')
            return HttpResponseRedirect(newpost.get_absolute_url())
        else:
            messages.error(
                request, f'New post addition has not been successfull..')
    else:
        form = PostForm()
    context = {
        "form": form,
    }
    return render(request, "blog/post_form.html", context)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    form_class=UpdatePostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_staff:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_staff:
            return True
        return False


class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'search/search.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Post.objects.annotate(
                similarity=TrigramSimilarity('title', query),
            ).filter(similarity__gt=0.3).order_by('-similarity')
        return object_list

# def post_search(request):
#     query = request.GET.get("q")
#     results = []
#     if query:
#         results = Post.objects.annotate(
#                 similarity=TrigramSimilarity('title', query),
#             ).filter(similarity__gt=0.3).order_by('-similarity')
#         object_list = object_list.filter(
#                 Q(title__icontains=query)|
#                 Q(body__icontains=query)|
#                 Q(author__first_name__icontains=query) |
#                 Q(author__last_name__icontains=query)
#                 ).distinct()
#     return render(request, 'search/search.html', locals())