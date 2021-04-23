from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name ="home"
urlpatterns = [
    path('',views.index),
    path('contact/', views.contact , name ='contact'),
    path('login_auth/',auth_views.LoginView.as_view(template_name="pages/login_auth.html"), name="login_auth"),
    path('logout_auth/',auth_views.LogoutView.as_view(next_page='/'),name='logout_auth'),

    path('login/',views.Login.as_view(), name="login"),
    path('logout/',views.Logout.as_view(),name='logout'),
    path('register/', views.register, name ="register")
]
