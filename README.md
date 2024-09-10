Nama : Zillan ahmad ryandi

NPM : 2306275443

Kelas : PBP F

1.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

--Membuat sebuah proyek Django baru.

Di dalam direktori SWIFT-GET,saya buat berkas requirements.txt dan tambahkan beberapa dependencies.
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
setelah itu saya melakukan instalasi dependencies dengan terlebi dahulu menjalankan
```
env\Scripts\activate
```
agar virtual environment aktif
kemudian run
```
pip install -r requirements.txt
```
kalau sudah terinstall semua jalankan
```
django-admin startproject swiftget .
```

--Membuat aplikasi dengan nama main pada proyek tersebut.

masi berada pada direktori yang sama jalankan
```
python manage.py startapp main
```
buka berkas settings.py dalam direktori swift_buy(ya swift_buy bukan swift_get) Tambahkan main ke dalam daftar aplikasi yang ada sebagai elemen paling terakhir. Daftar aplikasi dapat kamu akses pada variabel INSTALLED_APPS.

```
INSTALLED_APPS = [
    ...,
    'main'
]
```


-- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

membuat berkas baru dalam direktori main dengan nama urls.py
dan isikan urls.py dengan
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
setelah menambakan itu pindah ke urls.py yang berada pada swift_buy

Impor fungsi include dari django.urls.


```
from django.urls import path, include
```

Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.
```
urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```


--Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
name
price
description


pindah ke berkas models.py pada main dan isikan dengan
```
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=255)

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
```


-- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

tambahkan kode ini ke views.py
```
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'swift get',
        'npm' : '2306275443',
        'name': 'Zillan Ahmad Ryandi',
        'class' : 'PBP F'
    }

    return render(request, "main.html", context)
```
setelah itu pindah ke main.html dan tambhakan 
```
<h1>{{app_name}}</h1>
<body>

<h5>app name: {{ app_name  }}</h5>
<p><p>
<h5>Name: {{ name }} </h5>
<p><p>
<h5 >class: {{ class }} </h5>
<p><p>
    
</body>

```
--Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

menambahkan kode pada direktori main
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

kemudian pindah ke urls.py pada swift_buy dan tambahkan
```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```
--Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

pindah ke settings.py dan tambahkan allowed host zillan-ahmad-swiftget.pbp.cs.ui.ac.id

penampilan settings.py seharusnya seperti ini
```
ALLOWED_HOSTS = ["localhost", "127.0.0.1","zillan-ahmad-swiftget.pbp.cs.ui.ac.id"]
```
setelah penampilan sudah benar jalankan
```
git remote add origin https://github.com/zeenight/swift-get
git remote add pws http://zillan-ahmad-swiftget.pbp.cs.ui.ac.id/
git add .
git commit -m "TRY PWS"
git branch -M main
git push -u origin main
git bracnh -M main
git push pws main
```
--Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Capture](https://github.com/user-attachments/assets/b1fa8f13-6212-43ee-9a78-2a9c2432e4b6)


--Fungsi Git dalam Pengembangan Perangkat Lunak
Git digunakan untuk melacak perubahan kode, memungkinkan kerja kolaboratif tanpa konflik. Pengembang dapat membuat cabang untuk eksperimen tanpa mengganggu kode utama. Git juga menyimpan riwayat perubahan yang memungkinkan rollback jika ada kesalahan. Selain itu, Git memudahkan berbagi kode secara terdistribusi.

--Mengapa Django Dijadikan Permulaan Pembelajaran?
Django memiliki fitur lengkap dan dokumentasi komprehensif, memudahkan pemula belajar. Konvensi bawaan membuat pengaturan awal sederhana. Django digunakan secara luas dan memiliki fitur keamanan bawaan, memberikan landasan kuat dalam pengembangan aplikasi web.

--Mengapa Model Django Disebut Sebagai ORM?
Model Django disebut ORM karena memetakan kelas Python ke tabel database. ORM memungkinkan interaksi database tanpa menulis SQL manual, memudahkan pengembang. Django ORM juga membuat aplikasi lebih portabel terhadap berbagai jenis database. Ini mempermudah pemrosesan data secara terstruktur dengan sintaks Python.







