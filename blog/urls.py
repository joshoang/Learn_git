from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name ="blog"

urlpatterns = [
    path('',views.list, name="blog"),
    path('<int:id>',views.post, name='post'),
    path('generic',views.PostListView.as_view(), name="blog_generic"),
    path('generic_<int:pk>',views.post_detail_comment, name='post_generic'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-all-post',views.GetAllPost.as_view(), name="api-all-post"),
]
