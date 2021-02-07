from django.urls import path
from .views import HomePageView, TodoCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/new/', TodoCreateView.as_view(), name='post_new'),
]
