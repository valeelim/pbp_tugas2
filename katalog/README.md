# Katalog
Site dapat diakses [disini](https://vl-pbp-tugas2.herokuapp.com/katalog/)

## Bagan 
---
![](https://i.imgur.com/xOIqfhw.png)
- User melakukan request HTML dengan memasukkan URL yang dituju
- Jika URL tersebut cocok dengan salah satu URL pada `urlpatterns` yang didefinisikan pada `urls.py` sesuai , maka akan dilanjutkan pada fungsi yang ditunjuk pada `views.py`.
- `views.py` lalu menjalankan fungsinya dan jika diperlukan akan meminta *query* sesuai dengan *model* yang didefinisikan pada `models.py`.
- Database lalu mengembalikan data yang dimilikinya sebagai *response* kepada `views`.
- Setelah mendapatkan data dari database, `views` akan memilih template HTML untuk menampilkan suatu halaman.
- Template HTML yang ditampilkan didefinisikan dengan syntax HTML pada `./templates/<nama_template>.html`
- HTML tersebut lalu dikembalikan dan ditampilkan pada browser user.

<br>

## Virtual Environment
---
Dengan menggunakan *virtual environment* saat mengimplementasikan projek python kita, kita dapat memisahkan projek yang sedang kita kerjakan dengan projek lain. Pada dasarnya *virtual environment* menyediakan suatu lingkungan dimana dependencies yang di-*install* pada projek tersebut akan hanya terdapat pada projek tersebut.

Tanpa *virtual environment*, dependencies yang di-*install* akan terdapat pada lingkungan global yang dapat menimbulkan kerusakan pada projek lain.

Tentunya tanpa *virtual environment*, anda masih bisa membuat suatu aplikasi berbasis web, namun sangat tidak disarankan karena dapat terjadi beberapa error terhadap dependencies pada projek yang sedang dikerjakan dan juga projek lain yang telah selesai.

<br>

## Implementasi
---
### Langkah 1
 Pada `views.py`, dilakukan ***import*** terhadap *model* `CatalogItem` yang akan diambil datanya dari database. Lalu  menggunakan `ListView` yang disediakan pada `generic view` untuk mempermudah implementasi.

 Pada fungsi `IndexView` diberikan `template_name` sebagai template HTML yang akan ditampilkan, yaitu `katalog.html`, dan juga mengganti `context_object_name` yang secara *default* `object_list` menjadi `katalog_list` agar mempermudah pembacaan code.

<br>

### Langkah 2
 Routing dilakukan pada file `urls.py` dengan mendefinisikan `app_name` sebagai `katalog` sebagai namespace yang dapat digunakan dengan `include`.

 `path('katalog/', include(katalog.urls)` didefinisikan pada `project_django/urls.py` agar pada url `katalog/`, path pada `katalog/urls.py` dapat digunakan.

<br>

### Langkah 3
 Dengan menggunakan perintah `python .\manage.py makemigrations & python ./manage.py migrate`, models yang terdapat pada `models.py` akan diterapkan sebagai skema model pada database Django lokal.

 Lalu dengan data-data yang telah disediakan pada `fixtures/initial_catalog_data.json`, akan dijalankan perintah `python .\manage.py loaddata initial_catalog_data.json` untuk memasukkan data tersebut ke database Django lokal.

<br>

### Langkah 4
Untuk melakukan `deployement` di **Heroku**, digunakan file `Procfile` dan `.github/workflows/dpl.yml` untuk menjalankan beberapa perintah dan juga menyediakan konfigurasi yang diperlukan *Heroku*.

