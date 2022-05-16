from django.shortcuts import render
from .forms import ContactForm


# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'yoga_contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'yoga_contact/contact.html', context)
