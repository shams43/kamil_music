from django.db import models


class Janr(models.Model):
    janr = models.CharField(max_length=999)
    description = models.CharField(max_length=999)
    def __str__(self):
        return self.janr

class Author(models.Model):
    Authors = models.CharField(max_length=999)
    janr = models.ForeignKey(to=Janr, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.Authors

class Song(models.Model):
    song = models.CharField(max_length=999)
    janr = models.ForeignKey(to=Janr, on_delete=models.PROTECT, null=True)
    Authors = models.ForeignKey(to=Author, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.song