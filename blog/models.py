from django.db import models
from django.conf import settings
from django.utils import timezone
#This imports other code into here. 

# Create your models here: Database
#Create Post model here with objects inside: Model = Post Object=author,title, text, etc. 
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text= models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    #define methods
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title