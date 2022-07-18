from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'sayt/index.html', {'title': 'Главная страница сайта', 'tas': tasks})


def about(request):
    return render(request, 'sayt/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма некорректна'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'sayt/create.html', context)





# Create your views here.
