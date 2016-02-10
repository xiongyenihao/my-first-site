from django.shortcuts import render

def show_home(request):
    return render(request, 'storyofart/homepage.html')