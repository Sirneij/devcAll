from . import views
from django.urls import path
app_name = 'portfolio'
urlpatterns = [
    path('<str:username>/', views.portfolio_index, name='portfolio_index'),
    #Work experience
    path('<str:username>/experience/new', views.experience_new, name='experience_new'),
    path('<str:username>/<int:id>/experience/update', views.experience_update, name='experience_update'),
    path('<str:username>/<int:id>/experience/delete', views.experience_delete, name='experience_delete'),
    #Education
    path('<str:username>/education/new', views.education_new, name='education_new'),
    path('<str:username>/<int:id>/education/update', views.education_update, name='education_update'),
    path('<str:username>/<int:id>/education/delete', views.education_delete, name='education_delete'),
]
