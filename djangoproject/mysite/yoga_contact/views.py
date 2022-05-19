from django.shortcuts import render
from mysite.settings import EMAIL_HOST_USER
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Contact


# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        email = request.POST['email']
        if Contact.objects.filter(email=email).exists():
            return render(request, 'yoga_contact/failed.html')
        elif form.is_valid():
            form.save(commit=False)
            name = str(form['name'].value())
            recipient = str(form['email'].value())
            subject = f'Welcome to Yoga Blog {name}!'
            message = 'We received your contact details and we hope you are enjoying our content!'
            send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
            receiver_detail = {'recipient': recipient, 'name': name}
            return render(request, 'yoga_contact/success.html', receiver_detail)
    form = ContactForm()
    context = {'form': form}
    return render(request, 'yoga_contact/contact.html', context)
