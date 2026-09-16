from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Developers
    path('developers/', views.developer_list, name='developers'),
    path('developer/<int:pk>/', views.developer_detail, name='developer_detail'),

    # Projects
    path('projects/', views.project_list, name='projects'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('my-project/<int:pk>/', views.my_project_detail, name='my_project_detail'),
    
    # Find Work & Posting
    path('project-for-you/', views.project_for_you, name='project_for_you'),
    path('projects-for-you/', views.project_for_you, name='projects_for_you'), # old link backup
    
    path('post-a-project/', views.post_a_project, name='post_a_project'), # correct name
    path('post-project/', views.post_a_project, name='post_project'), # backup - both work

    # My Pages
    path('my-projects/', views.my_projects, name='my_projects'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    # Auth
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]