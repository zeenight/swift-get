from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275443',
        'name': 'Zillan Ahmad Ryandi',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)