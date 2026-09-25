from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_ors),
    path('display/', views.display),
    path('welcome/', views.welcome),
    path('signup/', views.user_signup),
    path('logout/',views.logout),
    path('signin/', views.user_signin),
    path('testlist/',views.test_list),
    path('list/',views.user_list),
    path('', views.welcome),
]