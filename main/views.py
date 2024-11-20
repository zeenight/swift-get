from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
#TUGAS4
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import reverse
from django.http import HttpResponseRedirect

#TUGAS 6
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    # product_entries = Product.objects.filter(user=request.user)

    context = {
        'app_name' : 'swift get',
        'npm' : '2306275443',
        'name': request.user.username,
        'class' : 'PBP F',
        # 'product_entries': product_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def register_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
        

    context = {'form': form}
    return render(request, "register_product.html", context)

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


#TUGAS 4

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
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)



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

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

#TUGAS 5

def edit_product(request, id):
    
    product = Product.objects.get(pk = id)

   
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
 
    product = Product.objects.get(pk = id)
   
    product.delete()
    
    return HttpResponseRedirect(reverse('main:show_main'))



#TUGAS 6

#   name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.IntegerField()
#     category = models.CharField(max_length=255)
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = strip_tags(request.POST.get("price"))
    category = strip_tags(request.POST.get("category"))
    user = request.user

    # mood = strip_tags(request.POST.get("mood")) # strip HTML tags!
    # feelings = strip_tags(request.POST.get("feelings")) # strip HTML tags!

    new_product = Product(
        name=name, description=description,
        price=price,category=category,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)



@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_product = Product.objects.create(
            user=request.user,
            name=data["name"],
            description=data["description"],
            price=int(data["price"]),
            category=(data["category"]),
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)