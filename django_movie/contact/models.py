from django.db import models

# Create your models here.


class Contact(models.Model):

    email = models.EmailField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
