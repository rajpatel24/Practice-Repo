from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, TemplateView, CreateView
from .models import Blog


class HomeView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blog_entries'
    paginate_by = 3

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-blog_date')
        # validate ordering here
        return ordering


class DashboardView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "dashboard.html"
    context_object_name = 'blog_entries'
    paginate_by = 3

    def get_queryset(self):
        return Blog.objects.filter(blog_author=self.request.user)


class CreateBlogView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "create_blog.html"
    fields = ['blog_title', 'blog_text']

    def form_valid(self, form):
        form.instance.blog_author = self.request.user
        return super().form_valid(form)

