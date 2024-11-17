from django.shortcuts import render, redirect
from application.forms import ContactForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()    
    return render(request, 'contact.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def testimonials(request):
    return render(request, 'testimonials.html')


