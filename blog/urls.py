from . import views
from django.urls import path
app_name = 'blog'
urlpatterns = [
    path('', views.blog_index, name='blog-index'),
    path('new/', views.post_new, name='post_create'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
    path('update/<slug:slug>/', views.PostUpdateView.as_view(), name='post-update'),
    path('delete/<slug:slug>/', views.PostDeleteView.as_view(), name='post-delete'),
    path('tag/<slug:tag_slug>/', views.blog_index, name='blog_index_by_tag'),
    # path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.results, name='search_results'),
    # path('ovation/', views.ovation, name='ovation'),
]
