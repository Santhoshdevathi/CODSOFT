from django.shortcuts import render
import datetime
from .models import Todos

# Create your views here.

def todoHome(request):
    if request.method == 'POST':
        content = request.POST['content']
        x = datetime.datetime.now()
        date = x.strftime('%Y-%m-%d')
        newTodo = Todos.objects.create(content=content,date=date)
        newTodo.save()
        allTodos = Todos.objects.all()
        return render(request,'Todo/todoHome.html',{'allTodos':allTodos})
    allTodos = Todos.objects.all()
    return render(request,'Todo/todoHome.html',{'allTodos':allTodos})

def deleteTodo(request):
    if request.method == 'POST':
        id = request.POST['to_delete']
        Todos.objects.get(id=id).delete()
        allTodos = Todos.objects.all()
        return render(request,'Todo/todoHome.html',{'allTodos':allTodos})

def updateForm(request):
    if request.method == 'POST':
        id = request.POST['to_update']
        todo = Todos.objects.get(id=id)
        content = todo.content
        return render(request,'Todo/updateForm.html',{'content':content,'id':id})
def updateTodo(request):
    if request.method == 'POST':
        content = request.POST['content']
        val = request.POST['updation']
        Todos.objects.filter(id=val).update(content=content)
        allTodos = Todos.objects.all()
        return render(request,'Todo/todoHome.html',{'allTodos':allTodos})

