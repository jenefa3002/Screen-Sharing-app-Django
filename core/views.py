from django.shortcuts import render

def screenshare_view(request):
    return render(request, 'core/screenshare.html')
