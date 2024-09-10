from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'swift get'
    }

    return render(request, "main.html", context)