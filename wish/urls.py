from django.urls import path
from .views import BirthdayListView,BirthdayAddView,BirthdayUpdateView,BirthdayDeleteView

app_name = 'wish'

urlpatterns=[
    path('',BirthdayListView.as_view(),name='list'),
    path('new/',BirthdayAddView.as_view(),name='add'),
    path('change/<slug:slug>/',BirthdayUpdateView.as_view(),name='update'),
    path('remove/<slug:slug>/',BirthdayDeleteView.as_view(),name='delete'),
]