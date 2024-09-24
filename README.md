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


--Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git digunakan untuk melacak perubahan kode, memungkinkan kerja kolaboratif tanpa konflik. Pengembang dapat membuat cabang untuk eksperimen tanpa mengganggu kode utama. Git juga menyimpan riwayat perubahan yang memungkinkan rollback jika ada kesalahan. Selain itu, Git memudahkan berbagi kode secara terdistribusi.

--Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django memiliki fitur lengkap dan dokumentasi komprehensif, memudahkan pemula belajar. Konvensi bawaan membuat pengaturan awal sederhana. Django digunakan secara luas dan memiliki fitur keamanan bawaan, memberikan landasan kuat dalam pengembangan aplikasi web.

--Mengapa Model Django Disebut Sebagai ORM?

Model Django disebut ORM karena memetakan kelas Python ke tabel database. ORM memungkinkan interaksi database tanpa menulis SQL manual, memudahkan pengembang. Django ORM juga membuat aplikasi lebih portabel terhadap berbagai jenis database. Ini mempermudah pemrosesan data secara terstruktur dengan sintaks Python.



=========================================================
TUGAS 3


--Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

langkah 1 : Implementasi Skeleton sebagai Kerangka Views

bikin templates di direktori utama
buatlah berkas main.html dengan isi

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>

```

kemudian buka settings.py yang berada di swift_buy dan tambahkan templates dengan kode ini
```

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
        'APP_DIRS': True,
        ...
    }
]

```

pada main/templates/ ubahlah kode main.html jadi:
```
{% extends 'base.html' %}
{% block content %}

<h1>{{app_name}}</h1>
<p><p>
<h5>Name: {{ name }} </h5>
<p><p>
<h5 >class: {{ class }} </h5>
<p><p>

{% block content %}
{% endblock content %}
    
```
Buat file baru bernama forms.py di direktori utama untuk mendefinisikan struktur form dengan kode dibawah ini:
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category","price"]

```

Mengubah Primary Key Dari Integer Menjadi UUID
Tambahkan baris ini pada berkas models.py di subdirektori main/.
```
# Create your models here.
import uuid  

from django.db import models
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=255)

    @property
    def is_expensive(self):
        return self.price > 1000000
```
eksekusi migrasi model dengan command
```
python manage.py makemigrations
python manage.py migrate
```
Membuat Form Input Data dan Menampilkan Data Product Entry Pada HTML dalam views.py dalam direktori main tambahkan beberapa import berikut
```
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductForm
from main.models import Product
```

buatlah fungsi baru dengan nama register_product yang menerima parameter request yang dapat register data Product Entry secara otomatis ketika data di-submit dari form.
```
def register_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "register_product.html", context)
```

Ubahlah fungsi show_main yang sudah ada pada file views.py menjadi
```
def show_main(request):
    product_entries = Product.objects.all()

    context = {
        'app_name' : 'swift get',
        'npm' : '2306275443',
        'name': 'Zillan Ahmad Ryandi',
        'class' : 'PBP F',
        'product_entries': product_entries
    }

    return render(request, "main.html", context)
```
import fungsi create_product_entry dalam file urls.py pada directory main
```
from main.views import show_main, register_product
```

tambahkan path URL ke dalam variabel urlpatterns pada urls.py seperti di bawah
```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('register-product', register_product, name='register_product'),
]
```

Buat file html baru dengan nama register_product.html pada direktori main/templates. Lalu isi masukkan kode berikut:
```
{% extends 'base.html' %} 
{% block content %}
<h1>Add new product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add product name" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```


Selanjutnya, di file main.html, gunakan kode berikut:
```
{% extends 'base.html' %}
{% block content %}

<h1>{{app_name}}</h1>
<p><p>
<h5>Name: {{ name }} </h5>
<p><p>
<h5 >class: {{ class }} </h5>
<p><p>
    

{% if not product_entries %}
<p>Belum ada data product dalam swiftget.</p>
{% else %}
<table>
  <tr>
    <th>Product name</th>
    <th>description</th>
    <th>price</th>
    <th>category</th>
  </tr>


  {% comment %} Berikut cara memperlihatkan data product di bawah baris ini 
  {% endcomment %} 
  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.name}}</td>
    <td>{{product_entry.description}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.category}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:register_product' %}">
  <button>Add New Product</button>
</a>
{% endblock content %}
```

--Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
pada views.py tambahkan import
```
from django.http import HttpResponse
from django.core import serializers
```
Buat fungsi baru bernama show_xml dan show_json yang menerima parameter request. Di dalam fungsi, simpan hasil query dari seluruh data di ProductEntry ke dalam variabel, lalu kembalikan HttpResponse dengan data yang telah diserialisasi menjadi XML/JSON, serta tambahkan parameter content_type sesuai dengan formatnya, yaitu application/xml atau application/json
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
"Mengembalikan Data Berdasarkan ID dalam Bentuk XML dan JSON. Tambahkan HttpResponse yang berisi data hasil query berdasarkan ID dari ProductEntry, diserialisasi ke dalam format JSON atau XML, dengan content_type diatur ke 'application/xml' atau 'application/json'."
```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

--Membuat routing URL untuk masing-masing views yang telah ditambahkan

Buka urls.py yang ada pada direktori main dan import fungsi berikut
```
from main.views import show_main, register_product, show_xml, show_json, show_xml_by_id, show_json_by_id
```
Tambahkan path URL ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
```
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```
  
--Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery penting dalam platform karena memastikan pertukaran informasi yang efisien antara server, aplikasi, dan pengguna. Ini mendukung konektivitas pengguna, layanan real-time, dan sinkronisasi data agar selalu up-to-date. Data delivery juga memungkinkan integrasi dengan layanan eksternal, serta memastikan pengambilan keputusan berdasarkan data yang akurat. Dengan mekanisme ini, platform dapat beroperasi lebih optimal, menawarkan pengalaman pengguna yang lebih baik, dan menjaga keamanan serta kecepatan pertukaran informasi.



--Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya JSON lebih baik daripada XML dalam banyak kasus, terutama untuk aplikasi web modern, karena beberapa alasan:
Struktur Lebih Sederhana: JSON memiliki format yang lebih ringkas dan mudah dibaca oleh manusia serta mesin, sedangkan XML lebih verbose dengan tag pembuka dan penutup yang membuatnya lebih panjang.
Pemrosesan Lebih Cepat: Karena JSON lebih ringan, parsing JSON biasanya lebih cepat dibandingkan dengan XML. Ini penting untuk aplikasi yang memerlukan kinerja tinggi dan respon cepat.
Integrasi dengan JavaScript: JSON secara native didukung oleh JavaScript, sehingga lebih mudah digunakan dalam aplikasi web, terutama untuk pertukaran data di antara browser dan server.
Lebih Efisien untuk Data Terstruktur: JSON sangat cocok untuk mewakili objek dan array, yang sering digunakan dalam pengembangan aplikasi modern, sementara XML lebih baik untuk dokumen yang sangat terstruktur.
Penanganan Data Lebih Sederhana: JSON memiliki dukungan luas di berbagai bahasa pemrograman modern dan tools API, membuatnya lebih fleksibel dan populer dalam pengembangan aplikasi web.

Karena faktor-faktor ini, JSON menjadi lebih populer dibandingkan XML, terutama dalam konteks web dan aplikasi mobile. Namun, XML masih digunakan dalam kasus tertentu, seperti dokumen yang memerlukan markup yang lebih kompleks atau standar industri lama yang masih memanfaatkan XML.



--Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() pada form Django digunakan untuk memvalidasi data yang diinputkan ke dalam form. Method ini akan memeriksa apakah semua field pada form memenuhi syarat validasi yang telah didefinisikan, seperti panjang karakter, tipe data, dan aturan khusus lainnya. Jika semua data valid, method ini akan mengembalikan nilai True; sebaliknya, jika ada error, akan mengembalikan False dan menyimpan pesan error di atribut errors. Kita memerlukan is_valid() untuk memastikan bahwa data yang diterima dari pengguna sesuai dengan yang diharapkan sebelum diproses lebih lanjut, misalnya disimpan ke database.

--Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Kita membutuhkan csrf_token saat membuat form di Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). CSRF terjadi ketika penyerang memanfaatkan otentikasi pengguna yang valid untuk mengirimkan permintaan berbahaya tanpa sepengetahuan mereka. Dengan menambahkan csrf_token, Django memastikan bahwa setiap permintaan form berasal dari sumber yang sah (yaitu dari situs yang sama) dan bukan dari situs luar yang berbahaya.

Jika tidak menambahkan csrf_token, penyerang dapat membuat halaman berbahaya yang, ketika diakses oleh pengguna yang sedang login, secara otomatis mengirimkan permintaan ke aplikasi web (misalnya, transfer uang, perubahan akun). Ini memungkinkan penyerang untuk mengeksploitasi hak akses pengguna tanpa sepengetahuannya. CSRF token mencegah ini dengan memverifikasi keaslian setiap permintaan POST.



mengakses keempat URL menggunakan Postman
XML by id
![xmlD](https://github.com/user-attachments/assets/38f237fd-ff06-4395-b1b7-8485aba48e62)
JSON by id
![jsonID](https://github.com/user-attachments/assets/956fa8a8-476c-4345-9137-4a2d7e0a58cd)
json
![json](https://github.com/user-attachments/assets/6c4ef73b-9ddd-475d-91ac-2fde37edf8d5)
xml
![xml](https://github.com/user-attachments/assets/08b7bde2-b890-4259-9e5c-b48ee715626c)





=========================================================================

TUGAS 4
-- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
--Membuat registrasi

pada views.py tambahkan kode
```
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```

dan kode
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

kemudian buatlah berkas baru di main/templates bernama register.html dan masukkan kode
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```


pindah ke urls.py pada main dan tambahkan import 
```
from main.views import register
```

urls patterns ditambahkan juga
```
 urlpatterns = [
     ...
     path('register/', register, name='register'),
 ]
```

pindah ke views.py pada main dan tambahkan
```
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
```

kemudian tambahkan function dibawah ini
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

```

lalu pindah ke main/templates dan buat berkas login.html
masukkan kode
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```


pindah ke urls.py dan tambahkan import
```
from main.views import login_user
```
serta menambahkan di urlpatterns
```
path('login/', login_user, name='login'),
```



balik ke views.py dan tambahkan import 
```
from django.contrib.auth import logout
```
dan masukkan function ini ke views.py
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

kemudian Bukalah berkas main.html yang ada pada direktori main/templates dan
 tambahkan potongan kode di bawah ini setelah hyperlink tag untuk Add New Mood Entry.
```
...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
...
```
pindah ke urls.py pada main dan tambahkan import 
```
from main.views import logout_user
```
dan tambahkan urlpattern
```
   path('logout/', logout_user, name='logout'),
```

sekarang bagian untuk menggunakan data dari cookies

buka views.py pada main
dan tambahkan import
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
dan jadikan function login user menjadi 
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
setelah itu jadikan show_main menjad \i 
```
def show_main(request):
    product_entries = Product.objects.all()

    context = {
        'app_name' : 'swift get',
        'npm' : '2306275443',
        'name': 'Zillan Ahmad Ryandi',
        'class' : 'PBP F',
        'product_entries': product_entries
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
```
dan update logout user menjadi
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
lalu tambahkan kode ini di main.html agar bisa dilihat sesi terakhir login
```
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

sekarang bangian mengkonek product dengan user

pertama tambahkan import pada models.py
```
from django.contrib.auth.models import User
```
update di models.py menjadi 
```
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=255)
```
lalu ke views.py update register product menjadi
```
def register_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
        

    context = {'form': form}
    return render(request, "register_product.html", context)
```
terakhir pada fungsi show_main tambhakan context
```

    context = {
         'name': request.user.username,
         ...
    }
```
lakukan  
```python manage.py makemigrations
``` 
kemudian inputkan 1 dua kali

lalu di settings.py import os
```
import os
```
dan ganti debug menjadi
```
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```

--Apa perbedaan antara HttpResponseRedirect() dan redirect()

HttpResponseRedirect() adalah kelas yang mengembalikan respons HTTP dengan status redirect (302) ke URL yang diberikan. redirect() adalah shortcut di Django yang otomatis menggunakan HttpResponseRedirect dan menerima argumen berupa URL atau view name.

--Jelaskan cara kerja penghubungan model Product dengan User!

Menggunakan ForeignKey atau OneToOneField untuk menghubungkan model Product dengan model User, sehingga produk bisa terkait dengan pengguna yang membuat atau memilikinya.

 --Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

 Authentication memverifikasi identitas pengguna, sementara authorization mengontrol akses pengguna ke sumber daya. Saat login, Django mengotentikasi pengguna. Django menggunakan middleware AuthenticationMiddleware untuk mengimplementasi authentication dan authorization.

 --Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

 Django menggunakan session cookies untuk mengingat pengguna yang telah login. Cookies juga digunakan untuk preferensi pengguna, namun tidak semua cookies aman karena bisa rentan terhadap serangan, seperti XSS.
