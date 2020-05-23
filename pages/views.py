from django.shortcuts import render
from django.views.generic import TemplateView , View
from django.core.mail import send_mail
from allauth.account.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ContactForm

class IndexView(TemplateView):
    template_name = 'pages/home.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('content')
        send_mail(name,msg,email,[''],fail_silently=False)
    return render(request,'pages/contact.html', {'form':form})

class CustomPasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    @property
    def success_url(self):
        return reverse_lazy('pages:home')