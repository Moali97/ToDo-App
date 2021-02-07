from django.http import request
from django.urls import reverse
from django.views.generic import ListView
from .models import List
from django.views.generic.edit import CreateView


class HomePageView(ListView):
    model = List
    context_object_name = 'all_posts_list'
    template_name = 'home.html'


class TodoCreateView(CreateView):
    model = List
    template_name = 'post_new.html'
    fields = ['title']

    def get_success_url(self):
        return reverse('home')
