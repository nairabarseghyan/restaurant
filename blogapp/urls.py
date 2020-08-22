from django.urls import path
# from . import views
from .views import HomeView
from .views import ArticleDetailView, AddPostView, UpdatePostView, DeletePostView
urlpatterns = [
   # path('', views.home, name='home')
   path('', HomeView.as_view(), name='home'),
   path('article_details/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
   path('add_post/', AddPostView.as_view(), name='add_post'),
   path('article_details/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
   path('article_details/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]
