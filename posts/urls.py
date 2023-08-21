from django.urls import path

from .views import PostDetail, PostList

urlpatterns = [
    path("", PostList.as_view(), name="posts_list"),  # type: ignore
    path("<int:pk>/", PostDetail.as_view(), name="posts_detail"),  # type: ignore
]
