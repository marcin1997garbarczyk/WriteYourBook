from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
def myStories(request):
    return render(request, 'mystories.html')

def story(request, id):
    return render(request, 'storyPage.html')