from django.urls import path, include
from .views import HomeView, DashboardView, CreateBlogView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create/', CreateBlogView.as_view(success_url="/"), name='create_blog'),

]