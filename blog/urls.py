from django.urls import path
from blog.views import AddPostView, DeletePostView, HomeView, PostDetailView, UpdatePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/add', AddPostView.as_view(), name='add-post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),
]