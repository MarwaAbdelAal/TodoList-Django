from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detailed/<str:id>', views.detailed, name='detailed'),
    path('createTodo/', views.createTodo, name='createTodo'),
    path('updateTodo/<str:id>', views.updateTodo, name='updateTodo'),
    path('deleteTodo/<str:id>', views.deleteTodo, name='deleteTodo'),
    path('signup', views.createUser, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('completedTodos', views.completedTodos, name='completedTodos'),
]
