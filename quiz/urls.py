from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.index, name='index'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/submit/', views.quiz_submit, name='quiz_submit'),
    path('quiz/<int:quiz_id>/result/', views.quiz_result, name='quiz_result'),
    path('category/<slug:slug>/', views.category_page, name='category_page'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('ratings/', views.ratings, name='ratings'),
    path('ratings/export/', views.export_ratings, name='export_ratings'),

    # Auth
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Admin
    path('panel/', views.admin_dashboard, name='admin_dashboard'),
    path('panel/quizzes/', views.admin_quiz_list, name='admin_quiz_list'),
    path('panel/quizzes/add/', views.admin_quiz_add, name='admin_quiz_add'),
    path('panel/quizzes/edit/<int:quiz_id>/', views.admin_quiz_edit, name='admin_quiz_edit'),
    path('panel/quizzes/delete/<int:quiz_id>/', views.admin_quiz_delete, name='admin_quiz_delete'),
    path('panel/categories/', views.admin_category_list, name='admin_category_list'),
    path('panel/categories/add/', views.admin_category_add, name='admin_category_add'),
    path('panel/categories/edit/<int:cat_id>/', views.admin_category_edit, name='admin_category_edit'),
    path('panel/categories/delete/<int:cat_id>/', views.admin_category_delete, name='admin_category_delete'),
    path('panel/users/', views.admin_user_list, name='admin_user_list'),
]
