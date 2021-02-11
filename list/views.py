from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from .models import List
from django.views.generic.edit import CreateView, DeleteView


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


class TodoDetailView(DetailView):
    model = List
    template_name = 'post_detail.html'


class TodoDeleteView(DeleteView):
    model = List
    template_name = 'delete.html'

