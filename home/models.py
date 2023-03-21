from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    views = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})


class Comment(models.Model):
    name = models.CharField(max_length=200, default='anonymous')
    email = models.EmailField(max_length=240)
    comment = models.TextField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name + ' || ' + self.email
    
