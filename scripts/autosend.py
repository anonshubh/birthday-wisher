from django.utils.timezone import datetime
from django.core.mail import send_mail
from django.http import HttpResponse

from wish.models import Birthday

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron',hour=24)
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

sched.start()