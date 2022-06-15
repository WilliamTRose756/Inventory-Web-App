from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.manager, name="manager"),
    path('delete/<int:pk>/', views.item_delete, name="manager-delete"),
    path('update/<int:pk>/', views.item_update, name="manager-update"),
    path('search_results/', views.search_results, name="search-results"),
    path('expiration_view/', views.expiration, name="expiration"),
    path('login', views.login, name='login'),
    path('logout_user', views.logout_user, name='logout'),
]


