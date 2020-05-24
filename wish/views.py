from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View , CreateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest , HttpResponse
from django.utils.timezone import datetime
from django.core.mail import send_mail

from apscheduler.schedulers.blocking import BlockingScheduler

from .models import Birthday
from .forms import BirthdayForm

sched = BlockingScheduler()

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

@sched.scheduled_job('cron', hour=00)
def auto_send():
    today = datetime.now()
    obj = Birthday.objects.filter(birth_date__day=today.day,birth_date__month=today.month)
    for i in obj:
        name = i.name
        to_ = i.email
        from_ = i.wisher.email
        message = i.wish
        #print(f"{message} {name} From:{from_} To:{to_}")
        send_mail("Happy Birthday!!",message,from_,[to_],fail_silently=False)
    return HttpResponse("Email Sent")

sched.start()
