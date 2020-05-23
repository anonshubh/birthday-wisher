from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View , CreateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest

from .models import Birthday
from .forms import BirthdayForm

class BirthdayListView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        obj = Birthday.objects.filter(wisher=request.user)
        return render(request,'wish/list.html',{'object_list':obj})

class BirthdayUpdateView(LoginRequiredMixin,View):
    def get(self,request,slug,*args,**kwargs):
        obj = get_object_or_404(Birthday,slug=slug)
        form = BirthdayForm(instance=obj)
        return render(request,'wish/update.html',{'object':obj,'form':form})
    
    def post(self,request,slug,*args,**kwargs):
        obj = get_object_or_404(Birthday,slug=slug)
        form = BirthdayForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('wish:list')
        return HttpResponseBadRequest


class BirthdayAddView(LoginRequiredMixin,CreateView):
    form_class = BirthdayForm
    template_name = 'wish/add.html'
    success_url = reverse_lazy('wish:list')

    def form_valid(self, form):
        form.instance.wisher = self.request.user
        obj = super(BirthdayAddView,self).form_valid(form)
        return obj

class BirthdayDeleteView(LoginRequiredMixin,DeleteView):
    model = Birthday
    template_name = 'wish/delete.html'
    success_url = reverse_lazy('wish:list')

