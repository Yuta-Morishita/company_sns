from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField()
    good = models.IntegerField()
    read = models.IntegerField()
    readtext = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '掲示板'
        verbose_name_plural = '掲示板'
