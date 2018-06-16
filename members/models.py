from django.db import models

class Member(models.Model):
    cell = models.CharField(max_length=50)
    name=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pics=models.ImageField(default='homepage/image/background.png')

    def __str__(self):
        return self.name + '-' +self.cell
