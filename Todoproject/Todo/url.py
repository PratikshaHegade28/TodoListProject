from django.urls import path
from .import views

urlpatterns =[
    path('',views.Todoview,name='Todo'),
    path('addTodo/',views.addTodo,name='add_Todo'),
    path('deleteTodo/<int:Todo_id>/',views.deleteTodo,name='delete_Todo'),
]