from django.shortcuts import render

# Create your views here.
#view for the home page
def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

#view for the about page
def about(request):
    context = locals()
    template = 'about.html'
    return render(request, template, context)

