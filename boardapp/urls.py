from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupfunc, name='signup'),
    path('login/', views.loginfunc, name='login'),
    path('list/', views.listfunc, name='list'),
    path('logout/', views.logoutfunc, name='logout'),
    path('detail/<int:pk>/', views.detailfunc, name='detail'),
    path('good/<int:pk>/', views.goodfunc, name='good')
]
