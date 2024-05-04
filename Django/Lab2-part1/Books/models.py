from django.db import models

# Create your models here.
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    publish=models.DateTimeField(auto_now_add=True)
    version=models.IntegerField(default=1)
    latest_version=models.DateTimeField(auto_now=True)
    image=models.CharField(max_length=200,null=True)

    author=models.ForeignKey(to='auther.Author',on_delete=models.CASCADE)
   

