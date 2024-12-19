
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_items})


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))