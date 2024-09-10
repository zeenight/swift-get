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