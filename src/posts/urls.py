from django.urls import path

from .api import posts, PostsListApi, PostListIdApi, CreateListApi, UpdateListApi, DeleteListApi

app_name = "posts"

urlpatterns = [
    path("", posts, name="list"),
    path("list/", PostsListApi.as_view(), name="posts_list"), 
    path("list/<int:pk>/", PostListIdApi.as_view(), name="posts_list_detail "), 
    path("create/", CreateListApi.as_view(), name="create_list"),  
    path("update/<int:pk>/", UpdateListApi.as_view(), name="update_list"),
    path("delete/<int:pk>/", DeleteListApi.as_view(), name="delete_list"),
]
