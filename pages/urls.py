from django.urls import path
from . import views

app_name = 'pages'

urlpatterns=[
    path('',views.IndexView.as_view(),name='home'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('reach-us/',views.contact_view,name='contact'),
]