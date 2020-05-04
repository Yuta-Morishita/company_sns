from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(null=True, blank=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    goodtext = models.CharField(max_length=200, null=True, blank=True)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '掲示板'
        verbose_name_plural = '掲示板'
