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



 ===================================================================================
 TUGAS 5

 pertama kita akan memakai tailwind dengan me modif base.html menjadi
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com">
    </script>
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

ke views.py tambahan function untuk edit produk

```
def edit_product(request, id):
    # Get mood entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=mood)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```

ke main/templates dan buat berkas edit_product.html dengan kode
```
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```


tambahkan url patterns edit_product

```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('register-product', register_product, name='register_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    #TUGAS 4
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    #TUGAS 5
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    
```

kemudian tambahkan ke html 
```
<td>
  <a href="{% url 'main:edit_product' product_entry.pk %}">
      <button>
          Edit
      </button>
  </a>
</td>
```

di views.py tambahkan 
```
def delete_Product(request, id):
 
    product = Product.objects.get(pk = id)
   
    product.delete()
    
    return HttpResponseRedirect(reverse('main:show_main'))
```
untuk menambahkan bagian css harus bikin berkas static dan direktori anda harusnya seperti ini
```
project_root/
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── index.js
│   │── videos/
│   │   └── ....
│   ├──  images/
│       └── ....
│	
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── ...
│
├── your_app_name/
│   ├── forms.py
│   ├── views.py
│   └── ...
│
└── manage.py
```

dan juga tambahkan ini ke settings.py
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```

kemudian perbarui login.html dengan kode
```
{% extends 'base.html' %}

{% load static %} 
<!DOCTYPE html>

{% block content %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>
<body>
    <video src="{% static 'videos/Pink_Blue_Green_Gradient_Color_and_Style_Video_Background.mp4' %}" autoplay loop muted></video>
   


    <div class="header">
      
        <button class="button-login"> Get started!
        </button>
        <h2>SwiftGet</h2>
    
    </div>

    <div class="Wrapping">
       
        <div class="formbox">
            <h2>Login</h2>
            <form method="POST" action="">
                {% csrf_token %}


                <div class="inputbox">
                    <span class="icon"></span>
                    {{ form.username }}
                    <label>Username</label>
                </div>
                
                <div class="inputbox">
                    <span class="icon"></span>
                    {{ form.password }}
                    <label>Password</label>
                </div>

                <button type="submit" class="btn login_btn">Login</button>
            </form>
            
            {% if messages %}
            <ul>
                {% for message in messages %}
                <li>{{ message }}</li>
                {% endfor %}
            </ul>
            {% endif %}

            <p>Don't have an account yet? <a href="{% url 'main:register' %}" style="color: purple; text-decoration: underline;">Register Now</a></p>
        </div>
    </div>

    <script src="{% static 'js/index.js' %}"></script>
</body>
</html>
{% endblock %}
```
dan buatlah style.css di static/css dimana dalamnya
```
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
}

body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    z-index: -1;
}

.header {
    font-size: 1.1em;
    font-weight: 500;
    right: 0;
    background: rgba(176, 176, 176, 0.16);
    backdrop-filter: blur(15px);
    position: fixed;
    display: flex;
    box-shadow: 0 0 8px rgba(207, 146, 248, 0.5);
    top: 0;
    width: 100%;
    padding: 30px 150px;
    justify-content: space-between;
    align-items: center;
    z-index: 99;
}

.navigation span {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    position: relative;
    font-size: 1.1em;
    color: rgb(223, 192, 255);
    font-weight: 500;
    text-decoration: none;
    margin-left: 40px;
}

.navigation span::after {
    content: '';
    position: absolute;
    transform: scaleX(1);
    left: 0;
    height: 4px;
    width: 100%;
    bottom: -6px;
    background: rgb(192, 160, 248);
    border-radius: 1em;
    transform-origin: right;
    transform: scaleX(0);
    transition: transform .5s;
}

.navigation span:hover::after {
    transform: scaleX(1);
}

.button-login {
    width: 130px;
    height: 35px;
    border-radius: 20px;
    background: transparent;
    border-color: transparent;
    color: rgb(202, 255, 249);
    font-size: 20px;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    border: 2px solid rgb(222, 202, 255);
    transition: 0.5s ease;
    font-weight: 500;
}

.button-login:hover {
    background: rgb(211, 251, 255);
    color: grey;
    transition: 0.5s ease;
}

.Wrapping {
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    width: 400px;
    color: rgb(241, 255, 253);
    height: 440px;
    justify-content: center;
    background: rgba(176, 176, 176, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 10px;
    font-size: 1.1em;
    font-weight: 500;
    display: flex;
    position: relative;
   
    align-items: center;
    overflow: hidden;
    transition: transform .3s ease, height .2s ease, left .5s ease;
    transform: scale(0);
    left: -75em;
}

.inputbox .input {
    font-size: 20px; /* Reduced the font size slightly for better readability */
    color: rgb(241, 255, 253);
    
}

.formbox h2 {
    text-align: center;
}

.Wrapping .formbox {
    width: 100%;
    padding: 40px;
}

.inputbox {
    position: relative;
    width: 100%;
    height: 80px;
    border-bottom: 2px solid rgb(243, 202, 255);
}

.inputbox label {
    position: absolute;
    top: 70%;
    left: 5px;
    transform: translateY(-50%);
    transition: 0.5s;
    pointer-events: none;
}

.inputbox input:focus ~ label,
.inputbox input:valid ~ label {
    color: rgb(214, 144, 255);
    top: 20px;
}

.inputbox input {
    width: 100%;
    height: 100%;
    background: transparent;
    border: none;
    outline: none;
    color: rgb(241, 255, 253);
    font-size: 18px; /* Reduced for better readability */
    padding-top: 40px; /* Added padding to move the input down */

}

.Wrapping.active-popup {
    transform: scale(1);
    left: 0;
}

.btn.login_btn {
    width: 120px; /* Adjust width */
    height: 50px; /* Adjust height */
    font-size: 20px; /* Adjust text size */
    padding: 10px 20px; /* Padding for inside the button */
    border-radius: 10px; /* Rounded corners */
    background-color: rgba(176, 176, 176, 0.1);
    color: white; /* Text color */
    border: none; /* No border */
    cursor: pointer; /* Pointer cursor on hover */
    margin-top: 20px; /* Add margin to move it down */
    transition: background-color 0.3s ease; /* Hover effect transition */
    border: 2px solid rgb(220, 171, 255);
}

.btn.login_btn:hover {
    background: rgb(211, 251, 255);
    color: black; /* Text color */
}


.transparent-image {
    width: 50px; /* Adjust as necessary */
    height: auto;
    /* No need to use positioning here since flexbox takes care of alignment */
}



/* General form wrapper styles ========================================================================================================================*/
```


sekarang register.html perbarui dengan
```


{% extends 'base.html' %}


{% load static %} 

<!DOCTYPE html>

{% block content %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link rel="stylesheet" href="{% static 'css/style2.css' %}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>
<body>
    <video src="{% static 'videos/Pink_Blue_Green_Gradient_Color_and_Style_Video_Background.mp4' %}" autoplay loop muted></video>
   


    <div class="header">
      
       <h1>Register</h1>
     
        <h2>SwiftGet</h2>
    
    </div>



        <div class="register-wrapper">
          <h1 class="register-title">Register</h1>
          <form method="POST" class="register-form">
              {% csrf_token %}


              <div class="form-group">
                <input type="text" name="username" id="id_username" required>
                <label for="id_username">Username</label>
            </div>
            
            <div class="form-group">
                <input type="password" name="password1" id="id_password1" required>
                <label for="id_password1">Password</label>
            </div>
            
            <div class="form-group">
                <input type="password" name="password2" id="id_password2" required>
                <label for="id_password2">Confirm Password</label>
            </div>

              <div class="form-actions">
                  <button type="submit" class="btn-submit">Register</button>
              </div>


          </form>
          {% if messages %}
          <ul class="messages">
              {% for message in messages %}
              <li>{{ message }}</li>
              {% endfor %}
          </ul>
          {% endif %}
        </div>

    

    <script src="{% static 'js/index.js' %}"></script>
</body>
</html>
{% endblock %}
```
buatlah berkas style2.css di static/css dengan isi
```
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
}

body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    z-index: -1;
}

.header {
    font-size: 1.1em;
    font-weight: 500;
    right: 0;
    background: rgba(176, 176, 176, 0.16);
    backdrop-filter: blur(15px);
    position: fixed;
    display: flex;
    box-shadow: 0 0 8px rgba(207, 146, 248, 0.5);
    top: 0;
    width: 100%;
    padding: 30px 150px;
    justify-content: space-between;
    align-items: center;
    z-index: 99;
}





.register-wrapper {
    width: 400px;
    color: rgb(241, 255, 253);
    margin: 50px auto;
    background-color: rgba(255, 255, 255, 0.1);
    padding: 40px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    backdrop-filter: blur(10px);
}


    

/* Title styling */
.register-title {
    text-align: center;
    margin-bottom: 20px;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    font-size: 24px;
    
}

/* Form group styling */
.form-group {
    position: relative;
    margin-bottom: 15px;
    width: 100%;
    height: 80px;
    border-bottom: 2px solid rgb(243, 202, 255);
}

.form-group label {
    position: absolute;
    top: 70%;
    left: 5px;
    transform: translateY(-50%);
    transition: 0.5s;
    pointer-events: none;
}

.form-group input:focus ~ label,
.form-group input:valid ~ label {
    top: 20px; /* Adjust this for how far you want the label to move */
    font-size: 15px; /* Make the label smaller when focused */
    color: rgb(214, 144, 255);
}

.form-group input {
    width: 100%;
    height: 100%;
    background: transparent;
    border: none;
    outline: none;
    color: rgb(241, 255, 253);
    font-size: 18px; /* Reduced for better readability */
    padding-top: 40px; /* Added padding to move the input down */
}

/* Submit button styling */
.btn-submit {
    width: 100%;
    padding: 12px;
    font-size: 16px;
    font-weight: bold;
    color: white;
    background-color: rgb(100, 149, 237); /* You can change this to your preferred color */
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.btn-submit:hover {
    background-color: rgb(65, 105, 225); /* Darker shade on hover */
}

/* Messages styling */
.messages {
    margin-top: 20px;
    color: rgb(255, 120, 120);
}

.messages li {
    list-style: none;
    background: rgba(255, 120, 120, 0.1);
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
}
```


lalu perbarui main.html menjadi
```
{% extends 'base.html' %}
{% load static %} 
<!DOCTYPE html>

{% block content %}
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Register</title>
        <link rel="stylesheet" href="{% static 'css/style3.css' %}">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    </head>
    <body>
      <!-- <img src="{% static 'images/406914-Fluid_gradient_wallpaper_design.jpg' %}" alt="Fluid Gradient Wallpaper"> -->
      <video src="{% static 'videos/Pink_Main.mp4' %}" autoplay loop muted></video>
      


        <div class="header">

          <div class="login-info">
            <h5>Last Login: {{ last_login }}</h5>
          </div>

          <div class="user-info">
            <h5>Class: {{ class }}</h5>
          </div>

          
          <div class="user-info">
            <h5>NPM: 2306275443</h5>
          </div>

          <div class="actions">
            <a href="{% url 'main:register_product' %}">
              <button class="btn-add">Add New Product</button>
            </a>
          </div>

        

          

          {% include 'navbar.html' %}

        </div>

        <div class="product-container">
          {% if not product_entries %}
            <p>No product data available in SwiftGet.</p>
          {% else %}
            <div class="scrollable-area">
              <table class="product-table">
                <thead>
                  <tr>
                    <!-- <th>Product Name</th>
                    <th>Description</th>
                    <th>Price</th>
                    <th>Category</th>
                    <th>Actions</th> -->
                  </tr>
                </thead>
                <tbody>
                  {% for product_entry in product_entries %}
                  
                    <!-- <td>{{ product_entry.name }}</td>
                    <td>{{ product_entry.description }}</td>
                    <td>{{ product_entry.price }}</td>
                    <td>{{ product_entry.category }}</td> -->
               
                    {% include 'card_product.html' with product_entry=product_entry %}
                  
                  {% endfor %}
                </tbody>
              </table>
            </div>
          {% endif %}
        </div>
        <script src="{% static 'js/index.js' %}"></script>
    </body>
    </html>

{% endblock %}

```
buatlah berkas baru style3.css di static/css
```
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
}

html {

    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden; /* Prevents scrolling on the entire page */
}
video {
    position: fixed; /* Changed from absolute to fixed */
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
}
body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    z-index: -1;
    overflow: hidden; /* Prevents extra scrolling */
}

.user-info {
    margin-right: 20px; /* Adds spacing between the user-info sections */
  }
  
  .actions {
    margin-left: auto; /* Pushes the button to the far right */
  }

  .header {
    font-size: 1.1em;
    font-weight: 500;
    background: rgba(176, 176, 176, 0.16);
    backdrop-filter: blur(15px);
    position: fixed;
    display: flex;
    box-shadow: 0 0 8px rgba(207, 146, 248, 0.5);
    top: 0;
    width: 100%;
    padding: 20px 50px; /* Adjusted for better spacing */
    justify-content: space-between;
    align-items: center;
    z-index: 99;
}

.navigation span {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    position: relative;
    font-size: 1.1em;
    color: rgb(223, 192, 255);
    font-weight: 500;
    text-decoration: none;
    margin-left: 40px;
}

.navigation span::after {
    content: '';
    position: absolute;
    transform: scaleX(1);
    left: 0;
    height: 4px;
    width: 100%;
    bottom: -6px;
    background: rgb(192, 160, 248);
    border-radius: 1em;
    transform-origin: right;
    transform: scaleX(0);
    transition: transform .5s;
}

.navigation span:hover::after {
    transform: scaleX(1);
}

.button-login {
    width: 130px;
    height: 35px;
    border-radius: 20px;
    background: transparent;
    border-color: transparent;
    color: rgb(202, 255, 249);
    font-size: 20px;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    border: 2px solid rgb(222, 202, 255);
    transition: 0.5s ease;
    font-weight: 500;
}

.button-login:hover {
    background: rgb(211, 251, 255);
    color: grey;
    transition: 0.5s ease;
}

.Wrapping {
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    width: 400px;
    color: rgb(241, 255, 253);
    height: 440px;
    justify-content: center;
    background: rgba(176, 176, 176, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 10px;
    font-size: 1.1em;
    font-weight: 500;
    display: flex;
    position: relative;
   
    align-items: center;
    overflow: hidden;
    transition: transform .3s ease, height .2s ease, left .5s ease;
    transform: scale(0);
    left: -75em;
}



.actions {
    display: flex;
    justify-content: center; /* Center the buttons horizontally */
    gap: 20px; /* Add space between the buttons */
    margin-top: 20px;
}

/* General button styling */
button {
    padding: 12px 24px; /* Add padding for a more substantial look */
    font-size: 16px; /* Increase font size */
    font-weight: bold;
    border: none;
    border-radius: 8px; /* Rounded corners */
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
}

/* Add New Product button style */

/* Logout button style */
.btn-logout {
    background-color: #dc3545; /* Red color for logout action */
    color: white;
}
.btn-add {
    background-color: rgb(214, 103, 248,0.9); /* Green color for add action */
    color: rgb(255, 255, 255);
}

.btn-add:hover {
    background-color: rgba(247, 220, 255, 0.9);/* Darker green on hover */
    color:  rgb(214, 103, 248);
    transform: scale(1.05); /* Slightly larger on hover */
}

.btn-logout:hover {
    background-color: #c82333; /* Darker red on hover */
    transform: scale(1.05); /* Slightly larger on hover */
}

/* Adding shadow to buttons */
button {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

button:active {
    transform: scale(0.98); /* Slight click effect */
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
}

.user-info {
    margin-left: 200px; /* Adjust the value as needed */
}

.product-container {
    position: relative;
    z-index: 1;
    height: 100%; /* Full height of the viewport */
    display: flex;
    justify-content: center;
    align-items: flex-start; /* Align content to the top, but allow space with margin */
    margin-top: 50px; /* Add margin to move the container down */
}

.scrollable-area {
    width: 100%;
    max-width: 1200px; /* Adjust the max-width according to your layout */
    height: 80vh; /* Adjust height to make this area scrollable */
    overflow-y: auto; /* Allows vertical scrolling */
    padding: 20px;
    box-sizing: border-box;
}

.scrollable-area {
    width: 100%;
    max-width: 1200px; /* Adjust the max-width according to your layout */
    height: 80vh; /* Adjust height to make this area scrollable */
    overflow-y: auto; /* Allows vertical scrolling */
    padding: 20px;
    box-sizing: border-box;
}

/* Scrollbar styles for WebKit browsers (e.g., Chrome, Safari) */
.scrollable-area::-webkit-scrollbar {
    width: 12px; /* Width of the scrollbar */
}

.scrollable-area::-webkit-scrollbar-track {
    background: rgba(255, 192, 203, 0.2); /* Pink transparent track */
    border-radius: 10px; /* Rounded corners */
}

.scrollable-area::-webkit-scrollbar-thumb {
    background-color: rgba(255, 192, 203, 0.6); /* Pink semi-transparent thumb */
    border-radius: 10px; /* Rounded corners */
    border: 2px solid rgba(255, 255, 255, 0.3); /* Adds a light border for better visibility */
}

/* For Firefox (scrollbar styles) */
.scrollable-area {
    scrollbar-width: thin; /* Thin scrollbar */
    scrollbar-color: rgba(255, 192, 203, 0.6) rgba(255, 192, 203, 0.2); /* Thumb and track colors */
}

.product-table th, .product-table td {
    padding: 10px;
    border-bottom: 1px solid #ddd;
}
```
kemudian perbarui register_product.html 
```
{% extends 'base.html' %}
{% load static %}

{% block content %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register Product</title>
    <link rel="stylesheet" href="{% static 'css/style4.css' %}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
     
</head>
<body>
    <div class="video-container">
        <!-- Background video -->
        <video src="{% static 'videos/Pink_Main.mp4' %}" autoplay loop muted></video>

        <div class="header">
          <button class="button-login">Get started!</button>
          <h2>SwiftGet</h2>
          {% include 'navbar.html' %}
      </div>

        <!-- Content that goes on top of the video -->
        <div class="content">
            <!-- Header with navigation -->
            <!-- Form to add a new product -->
            <h1>Add New Product</h1>

            <form method="POST">
                {% csrf_token %}
                <div class="Wrapper">
                    <div class="form-group">
                        <label for="id_name">Product Name</label>
                        {{ form.name }}
                    </div>

                    <div class="form-group">
                        <label for="id_description">Description</label>
                        {{ form.description }}
                    </div>

                    <div class="form-group">
                        <label for="id_price">Price</label>
                        {{ form.price }}
                    </div>

                    <div class="form-group">
                        <label for="id_category">Category</label>
                        {{ form.category }}
                    </div>

                    <div class="form-group">
                        <input type="submit" value="Add Product" class="btn btn-primary">
                    </div>
                </div>
            </form>
        </div>
    </div>

    <script src="{% static 'js/index.js' %}"></script>
</body>
</html>
{% endblock %}

```
sekaligus tambahkan berkas edit_product.html dengan isi
```

{% extends 'base.html' %}
{% load static %}

{% block content %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register Product</title>
    <link rel="stylesheet" href="{% static 'css/style4.css' %}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
     
</head>
<body>
    <div class="video-container">
        <!-- Background video -->
        <video src="{% static 'videos/Pink_Main.mp4' %}" autoplay loop muted></video>

        <div class="header">
          <button class="button-login">Get started!</button>
          <h2>SwiftGet</h2>
          {% include 'navbar.html' %}
      </div>

        <!-- Content that goes on top of the video -->
        <div class="content">
            <!-- Header with navigation -->
            <!-- Form to add a new product -->
            <h1>edit Product</h1>

            <form method="POST">
                {% csrf_token %}
                <div class="Wrapper">
                    <div class="form-group">
                        <label for="id_name">Product Name</label>
                        {{ form.name }}
                    </div>

                    <div class="form-group">
                        <label for="id_description">Description</label>
                        {{ form.description }}
                    </div>

                    <div class="form-group">
                        <label for="id_price">Price</label>
                        {{ form.price }}
                    </div>

                    <div class="form-group">
                        <label for="id_category">Category</label>
                        {{ form.category }}
                    </div>

                    <div class="form-group">
                        <input type="submit" value="Edit Product" class="btn btn-primary">
                    </div>
                </div>
            </form>
        </div>
    </div>

    <script src="{% static 'js/index.js' %}"></script>
</body>
</html>
{% endblock %}

```
dan style4.css dibuat di static/css
```
.video-container {
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: hidden;
}
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
}
video {
    position: fixed; /* Changed from absolute to fixed */
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
}

html {

    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden; /* Prevents scrolling on the entire page */
}
body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    z-index: -1;
}
/* Style the video to cover the entire container */

/* Position the content over the video */
.content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white; /* Text color for contrast */
    z-index: 2;   /* Make sure content is above the video */
}

.header h2, .header button {
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 15px;
}
.header {
    font-size: 1.1em;
    font-weight: 500;
    right: 0;
    background: rgba(176, 176, 176, 0.16);
    backdrop-filter: blur(15px);
    position: fixed;
    display: flex;
    box-shadow: 0 0 8px rgba(207, 146, 248, 0.5);
    top: 0;
    width: 100%;
    padding: 30px 150px;
    justify-content: space-between;
    align-items: center;
    z-index: 99;
}

.Wrapper {
    width: 100%;                /* Makes the form responsive */
    max-width: 800px;            /* Increase the max width to 800px or any value you prefer */
    margin: 0 auto;              /* Centers the form horizontally */
    padding: 20px;
    background-color: rgba(249, 249, 249, 0.5);
    border-radius: 8px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);  /* Soft shadow for depth */
    color: palevioletred;
}

/* Form group styles */
.form-group {
    margin-bottom: 20px;  /* Space between form fields */
    display: flex;
    flex-direction: column;  /* Labels and inputs stacked vertically */
    color: palevioletred;
}

/* Label styles */
.form-group label {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 8px;
    color: #333;
}

/* Input field styles */
.form-group input[type="text"],
.form-group textarea,
.form-group select {
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 100%;
    box-sizing: border-box;
    transition: border-color 0.3s;
    color: palevioletred;
}

/* Input hover and focus styles */
.form-group input[type="text"]:focus,
.form-group textarea:focus,
.form-group select:focus {
    border-color: #fdbdff;  /* Border color on focus */
    outline: none;
    color: palevioletred;
}

/* Submit button styles */
.btn {
    background-color: #dfabd6;
    color: white;
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
    color: rgb(255, 255, 255);
}

/* Hover effect for the button */
.btn:hover {
    background-color: #f5bef0;
    color: palevioletred;
}

```
#**1. Urutan Prioritas Pengambilan CSS Selector**
Ketika ada beberapa CSS selector yang mengatur elemen HTML yang sama, urutan prioritas (specificity) ditentukan berdasarkan aturan berikut:

Inline CSS: Gaya yang langsung ditulis di elemen (misalnya, style="...") memiliki prioritas tertinggi.
ID Selector: Selector yang menggunakan ID (#) memiliki prioritas lebih tinggi dibandingkan class atau elemen.
Class, pseudo-class, dan attribute selectors: Selector yang menggunakan class (.classname), pseudo-class (:hover), atau attribute ([type="text"]) memiliki prioritas lebih tinggi dibandingkan tag elemen.
Element Selector: Selector yang mengacu pada elemen HTML langsung (div, p, h1) memiliki prioritas terendah.
Important Rule: Jika ada properti yang menggunakan !important, aturan ini akan menimpa aturan lain, kecuali ada selector lain yang juga menggunakan !important dan memiliki specificity lebih tinggi.


#**2. Pentingnya Responsive Design dalam Pengembangan Aplikasi Web**
Responsive design adalah konsep yang penting karena:

Pengalaman Pengguna (UX): Pengguna mengakses aplikasi dari berbagai perangkat (desktop, tablet, smartphone) dengan ukuran layar berbeda. Responsive design memastikan bahwa tampilan aplikasi tetap nyaman dan mudah digunakan di semua perangkat.
Optimisasi SEO: Mesin pencari seperti Google memberikan preferensi kepada situs yang mobile-friendly, yang artinya responsive design dapat membantu meningkatkan ranking SEO.
Adaptabilitas: Aplikasi dengan responsive design tidak memerlukan versi terpisah untuk perangkat yang berbeda, sehingga mempermudah pengelolaan konten dan meningkatkan efisiensi.
Contoh aplikasi yang sudah menerapkan responsive design:

Google: Menampilkan desain yang menyesuaikan dengan perangkat pengguna

Contoh web yang tidak menerapkan responsive design:

https://dequeuniversity.com/library/responsive/1-non-responsive

#**3. Perbedaan Margin, Border, dan Padding**
Margin: Area luar elemen yang menciptakan jarak antara elemen dengan elemen lainnya.

Contoh Implementasi
```
.box {
  margin: 20px;
}
```
Border: Garis yang mengelilingi elemen di antara margin dan padding.

Contoh Implementasi
```
.box {
  border: 2px solid black;
}
```
Padding: Ruang antara konten elemen dan border elemen.

Contoh Implementasi
```
.box {
  padding: 10px;
}
```
Ketiganya berada pada model kotak CSS (CSS box model) dengan urutan: Margin di bagian terluar, Border di tengah, dan Padding di bagian dalam, dekat dengan konten elemen.



#**4. Konsep Flexbox dan Grid Layout Beserta Kegunaannya**
##Flexbox (Flexible Box Layout)

Konsep: Flexbox dirancang untuk mengatur tata letak elemen dalam satu dimensi (baik secara horizontal atau vertikal). Elemen di dalam flex container dapat secara otomatis menyesuaikan ukuran dan posisinya sesuai dengan ruang yang tersedia.
Kegunaan: Flexbox digunakan untuk membuat tata letak yang responsif dan dinamis, seperti menyusun item dalam baris atau kolom, sentralisasi elemen, atau mengatur ruang antar elemen.

##Grid Layout

Konsep: Grid layout dirancang untuk tata letak dua dimensi (baris dan kolom). Dengan grid, kita dapat dengan mudah membuat desain halaman yang kompleks dengan mengatur area konten dalam grid cells.
Kegunaan: Grid cocok digunakan untuk tata letak yang lebih rumit, seperti halaman dashboard, di mana elemen-elemen perlu diatur dalam kolom dan baris yang teratur.
Contoh Implementasi:

Perbandingan: Flexbox lebih baik untuk tata letak linier (satu dimensi), sedangkan Grid lebih fleksibel untuk tata letak yang melibatkan kolom dan baris (dua dimensi).