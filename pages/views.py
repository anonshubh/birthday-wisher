from django.shortcuts import render
from django.views.generic import TemplateView , View

class IndexView(TemplateView):
    template_name = 'pages/home.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ContactView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'pages/contact.html',{})
