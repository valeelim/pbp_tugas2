import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import RegisterForm
from .models import Task


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'todolist.html'
    login_url = 'todolist:login'
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
            'username': self.request.user,
        })
        return context


def show_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')


def create_task(request):
    if request.method == 'POST':
        newTask = Task(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        newTask.save()
        return JsonResponse({
            'pk': newTask.pk,
            'title': newTask.title,
            'description': newTask.description,
            'date': newTask.date
        })
    return render(request, 'todolist.html', {})


def delete_task(request, task_id):
    if request.method == 'POST':
        Task.objects.get(pk=task_id).delete()
        return JsonResponse({
            'pk': task_id
        })


def finish_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        task.is_finished ^= True
        task.save()
        return JsonResponse({
            'pk': task.pk,
            'currentState': task.is_finished
        })


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todolist:login')
        else:
            return render(request, 'register.html', {'form': form})
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
            response.set_cookie('last_login', str(
                datetime.datetime.now()), max_age=60*60*24*14)
            response.set_cookie('username', username, max_age=60*60*24*14)
            return response
        else:
            return render(request, 'login.html', {'notFound': True})
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    response.delete_cookie('username')
    return response
