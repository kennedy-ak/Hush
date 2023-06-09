from django.urls import path,include
from blog.views import PostView,user_category_list,home_view,feed_view,robots_txt,delete_category_post,create_post,update_category_post,category_post,user_post_list,update_post,delete_post,CommentView,CategoryView,PostViewDetailed,CategoryViewDetailed,CommentViewDetailed,search,detail,category
urlpatterns = [
    
    #User post...........................
    path("list-category/",user_category_list,name="user_category_list"),
    path("category-post/",category_post,name="category_post"),
    path("update-category-post/<str:id>/",update_category_post,name="update_category_post"),
    path("delete-category-post/<str:id>/",delete_category_post,name="delete_category_post"),
    path("list-post/",user_post_list,name="user_post_list"),
    path("list-category/",user_category_list,name="user_category_list"),
    path("create-post/",create_post,name="user_create_post"),
    path("update-post/<str:id>/",update_post,name="user_update_post"),
    path("delete-post/<str:id>/",delete_post,name="user_delete_post"),
    #Main blog......................
    path('feed/',feed_view,name='feed',),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',home_view,name="home"),
    path('search/',search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', detail, name='post_detail'),
    path('<slug:slug>/',category, name='category_detail'),  
    #Api ...........................................
    path("api/post/",PostView.as_view()),
    path("api/post/detailed-view/<str:id>/",PostViewDetailed.as_view()),
    path("api/category/",CategoryView.as_view()),
    path("api/category/detailed-view/<str:id>/",CategoryViewDetailed.as_view()),
    path("api/comment/",CommentView.as_view()),
    path("api/comment/detailed-view/<str:id>/",CommentViewDetailed.as_view()),
   
]
