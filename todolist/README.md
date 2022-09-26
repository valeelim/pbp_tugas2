# Todolist
Link to the site [here](https://vl-pbp-tugas2.herokuapp.com/)

## Using `{% csrf_token %}` on Forms
CSRF (Cross-Site Request Forgery) is a type of attack that other malicious sites, or users commit. CSRF itself exploits the fact that sites usually recognize a certain user using cookies. Users might visit those malicious websites and the site would send hidden forms which enables them to get the credentials  of a user. That by itself sounds like danger, and it is. They are now able to use your credentials to access your bank account, forums, and many more. 

That's why Django provides a simple way to prevent that, by using `csrf_token` which is unique for that particular site. It also provides a CSRF cookie. `csrf_token` is basically a token that the server sends to you when you request the form (in a hidden form field with a **csrfmiddlewaretoken**). When you submit the form, it checks the token, and if it does not match, the server won't accept it.

If you do not attach `{% csrf_token %}` to forms, of course you would be vulnerable to those attacks. Sometimes you would also get a 403 error, since all requests must have the CSRF cookie and the **csrfmiddlewaretoken**.

## Manual Forms
Yes, you can create your own forms. Start off by creating a `forms.py` file. That file is basically the type of form that you will define yourself, for example, the data or fields that it will receive. You can also customize it's attributes by accessing the **widgets**.

Once you've created the form, on your `views.py`, you can access that form, for eg: `form = <Form_Name>()` which receives the form data from `request.POST`. 

On the template on the other hand, you would just refer to the form created by using `{{ form.<field_name> }}`, which would render an `<input>` tag with the corresponding widget attributes that you declared yourself.

## Form Data Flow

The flow of data starts from the user. The user would then fill in the form that the server sends. After the user submits that data, the server would then process that data based on the method that the form is constructed with (usually in the form of `POST`) since form does not allow `DELETE` or `PUT`. The data is then processed by the server, to check whether it conforms to the constraints the form gives. If it is not valid, the server would then throw an error to the user, and the user would have to fill it again. If it is valid, the server would then take that data, and create or save it to the database.

When the user wants to see a certain piece of data, it is pretty simple. First, the server would check whether or not the user is allowed to see the page itself (some pages are not protected, but some are). If they are allowed to, the server would just take that data from the database, and pass those data to the front-end by context. The HTML template would then render the data alongside the HTML templates defined.

## Implementation of ToDoList
- To start a new application `todolist`, just run the command
```shell
python manage.py startapp todolist
```

- In order for the main application to access this particular application, I would need to provide a path to this application. I do that by just adding a new path to the urlpatterns of `project_django/urls.py`.
```python
urlpatterns = [
    ...
    path('todolist/', include(`todolist.urls`)),
    ...
]
```

- To create a new model `Task`, just create a new model inside `todolist/models.py` named `Task` with it's corresponding attributes.
```python
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```

- To implement the registration form, you could use `UserCreationForm`. For this app, I used a custom one which I implemented on `todolist/forms.py`. Basically I just declared a bunch of attributes on the widgets for each field.
```python
class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'placeholder': 'Joji',
            'class': 'form-control',
        })
        ...

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
```
After I created the form, I can just use it for the register views. 
```python
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todolist:login')
    context = {'form': form}
    return render(request, 'register.html', context)
```

- To implement the login, I did not use a custom form, since the only thing I need to check is if the user exists or not. To do that, I presented a simple HTML form to the user, and when the user submits the form, I get the `username` and `password` and checks whether the database has the user stored. If it's not, then the user would have to fill the form again or create a new account. If it exists, the user would be redirected to the `todolist:show_todolist` page and `set_cookie` to make the user experience better.
```python
def login_user(request):
    if request.method == 'POST':
        ...
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(...)
            response.set_cookie(...)
            return response
    return render(request, 'login.html', {})
```

- The logout is incredibly simple, I just need to import the logout function from `django.contrib.auth`, and when the user decides to logout, all I need to do is:
```python
def logout_user(request):
    logout(request)
    return redirect('todolist:login')
```

- To implement the `show_todolist` page, I need to do a couple of things. To show the username of the user, I could just use the currently stored cookie to know who the user is, and pass that as a context from the views to the template.

- To add a new task, I basically made a navbar partials, so that I in the future I might be able to reuse it, and when the user clicks `Add New Task`, a modal pops out which presents a form for the user to fill with the task that they want to create. After they submit the form, it sends a `POST` request to the `create_task` function, which basically creates a new `Task` object with the user as the ForeignKey.

- For the logout button, it's located on the upper right corner of the window, which you have to press (there's an arrow). There should be a `Logout` button.

- For the task data, I presented them in an accordion to make it more readable (hopefully), the data is given by the server based on the ForeignKey of each task. If the ForeignKey matches the User, that would mean the Task belongs to the user, and I just pass that as context as well.

- To route all those things, I added a couple paths inside `todolist/urls.py`.
```python
urlpatterns = [
    path('', views.IndexView.as_view(), name='show_todolist'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('create-task/', views.create_task, name='create_task'),
    path('<int:task_id>/delete-task/', views.delete_task, name='delete_task'),
    path('<int:task_id>/finish-task/', views.finish_task, name='finish_task'),
]
```

- To deploy the application, I just have to push the file to github :D.


