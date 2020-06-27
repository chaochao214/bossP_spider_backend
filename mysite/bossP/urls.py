from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('search/<searchName>', views.search, name='search'),
    path('search/', views.search1, name='search1'),
]
