from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # post list has been assigned to the root url i,e http://127.0.0.1:800/
]