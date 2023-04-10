from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo, TodoItems
from .forms import TodoForm, UserCreation, EditTodoForm
from .filters import TodoFilter, CompletedTodoFilter
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login')
def home(request):

    user = request.user
    filter = TodoFilter()
    todos = Todo.objects.filter(user=user)
    completedTodos = Todo.objects.filter(user=user, is_completed=True)

    print(todos)

    if request.method == "GET":
        OUTPUT = TodoFilter(request.GET, queryset=todos)
        todos = OUTPUT.qs

    message = """
        Hola from Django! ^_^
    """

    context = {
        # "message": message
        "todos": todos,
        "user": user,
        "filter": filter,
        "completedTodos": completedTodos,
    }

    # return HttpResponse(message)
    return render(request, 'home.html', context)


@login_required(login_url='/login')
def detailed(request, id):
    todo = Todo.objects.get(id=id)
    items = todo.todoitems_set.all()
    context = {
        "todo": todo,
        "items": items
    }
    return render(request, 'detailed.html', context)


@login_required(login_url='/login')
def completedTodos(request):

    user = request.user
    filter = CompletedTodoFilter()
    todos = Todo.objects.filter(user=user, is_completed=True)

    print(todos)

    if request.method == "GET":
        OUTPUT = CompletedTodoFilter(request.GET, queryset=todos)
        todos = OUTPUT.qs

    context = {
        "todos": todos,
        "user": user,
        "filter": filter,
    }

    return render(request, 'completedTodos.html', context)


@login_required(login_url='/login')
def createTodo(request):
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form": form
    }
    return render(request, 'createTodo.html', context)


@login_required(login_url='/login')
def updateTodo(request, id):
    todo = Todo.objects.get(id=id)
    form = EditTodoForm(instance=todo)
    if request.method == "POST":
        form = EditTodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request, 'updateTodo.html', context)


@login_required(login_url='/login')
def deleteTodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')


def createUser(request):
    form = UserCreation()

    if request.method == "POST":
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form": form
    }
    return render(request, 'signup.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    context = {
        # "form": form
    }

    return render(request, 'login.html', context)


@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('/')
