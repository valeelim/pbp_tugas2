import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import generic
from .forms import RegisterForm
from .models import Task


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'todolist.html'
    login_url = 'login/'
    context_object_name = 'task_list'

    def get_queryset(self):
        try:
            return list(Task.objects.filter(user=self.request.user))
        except Task.DoesNotExist:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['task_list'] = Task.objects.filter(user=self.request.user)
        except Task.DoesNotExist:
            context['task_list'] = None
        context.update({
            'username': self.request.COOKIES['username'],
            'last_login': self.request.COOKIES['last_login'],
        })
        return context


def create_task(request):
    if request.method == 'POST':
        Task.objects.create(
            user=request.user,
            date=datetime.datetime.now(),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        return HttpResponseRedirect(reverse('todolist:show_todolist'))
    return render(request, 'todolist.html', {})

def delete_task(request, task_id):
    if request.method == 'POST':
        Task.objects.get(pk=task_id).delete()
        return HttpResponseRedirect(reverse('todolist:show_todolist'))

def finish_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        task.is_finished ^= True
        task.save()
        return HttpResponseRedirect(reverse('todolist:show_todolist'))


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('todolist:login')
        else:
            form = RegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            response.set_cookie('username', username)
            return response
        else:
            messages.info(request, 'Username or password incorrect')
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('todolist:login')
