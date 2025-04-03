from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Player(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
