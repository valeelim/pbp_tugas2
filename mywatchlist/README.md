# My Watch List
Link to the site [here](https://vl-pbp-tugas2.herokuapp.com/)

## JSON, XML, and HTML
**HTML** (HyperText Markup Language) is used as a standard markup for web applications mainly for presentation, whilst **XML** (eXtensible Markup Language) is mainly used for storing and transfering data. **JSON** (JavaScript Object Notation) is similar to **XML** in that it is a data interchange format, which is more popular than **XML** since it is lightweight and easy to read.
<br>

## Significance of Data Delivery on Platform Implementation
Generally speaking, an application will need a way to store various types of data that users input into the database. Communication between clients and servers are quintessential to say the least, which is why it is incredibly important for that data to be delivered through safely (obviously) and as fast as possible.

Just imagine a scenario where you are in dire need of information, such as *"How do you open TARBALL files"* from google, and it returns some results after 10 minutes. That would be a massive waste of time, considering the fact that you would still not be able to open a TARBALL file *teehee*, and a massive inconvenience in general.

That scenario by itself I think is a good enough reason to demonstrate how important data delivery is.
<br>

## Implementation of MyWatchList
- To start a new application, all I need to do is run:
```shell
python manage.py startapp mywatchlist
```
- Adding the URL for this new application requires adding a new path to the `project_django/urls.py` urlpatterns. I also added a few things to the `mywatchlist/urls.py` such as setting the app_name and some urlpatterns that correlates with `mywatchlist/`.

```python
urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
]
``` 
- The models for `mywatchlist` is created inside the `mywatchlist/models.py` file, where I created a new Class and defined the attributes that it needs. After that is created, I went ahead and run `makemigrations` and `migrate` to apply the changes.
```python
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
```
```shell
python manage.py makemigrations
python manage.py migrate
```
- At this point, I want to add some data to my database. To do that, I made a new file named `initial_mywatchlist_data.json` inside a brand new folder `mywatchlist/fixtures`. After creating a few seed data, all I had to do was load that data.
```json
[
    ...
    {
        "model": "mywatchlist.mywatchlist",
        "pk": ...,
        "fields": {
            "watched": ...,
            "title": ...,
            "rating": ...,
            "release_date": ...,
            "review": ...
        }
    },
    ...
]
```
```shell
python manage.py loaddata initial_mywatchlist_data.json
```
- After creating some seed data, of course you want to see it presented to you, in this task we were asked to present them in **JSON**, **XML**, and **HTML** format. To present those, I used **serializers**. I created 2 functions in `mywatchlist/views.py` for **JSON** and **XML**, and also 1 class for **HTML** using generic views to present a HTML template that I made `mywatchlist/templates/mywatchlist.html`.
```python
def show_json(request):
    ...
    return HttpResponse(serializers.serialize('json', ...), ...)

def show_xml(request):
    ...
    return HttpResponse(serializers.serialize('xml', ...), ...)

class IndexView(generic.ListView):
    ...
    return context
```
- After I made the views, I need to make it accessible through URLS. So I just need to add the paths to `mywatchlist/urls.py`.
```python
urlpatterns = [
    path('json/', views.show_json, name='json_format'),
    path('xml/', views.show_xml, name='xml_format'),
    path('html/', views.IndexView.as_view(), name='html_format'),
]
```
- And that is it, all I need to do now is deploy it to **Heroku**. Modify the `Procfile` by adding a command to make sure **Heroku** actually loads the data provided in the `fixtures`, then push it to **GitHub** and done :dog:.
```python
release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json && python manage.py loaddata initial_mywatchlist_data.json'
```

## Postman Screenshots on Data Retrieved From Each Format
### HTML
![](https://i.imgur.com/k2xcYbs.png)
### JSON
![](https://i.imgur.com/W5pAUUL.png)
### XML
![](https://i.imgur.com/CYSAp3H.png)
