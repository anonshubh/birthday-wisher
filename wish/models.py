from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.utils.encoding import smart_str
from django.urls import reverse

User = get_user_model()

class Birthday(models.Model):
    wisher = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='name',unique=True)
    birth_date = models.DateField('Birthday',help_text='Valid Format: YYYY-MM-DD')
    wish = models.TextField()
    email = models.EmailField(help_text="Email of Receiver")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return smart_str(self.name)
    
    def get_absolute_url(self):
        return reverse('wish:detail',kwargs={'slug':slug})




