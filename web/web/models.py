from django.db import models


class ArtistQuote(models.Model):

    name = models.CharField(max_length=64, verbose_name="nome programmatico", primary_key=True)
    title = models.CharField(max_length=128, verbose_name="titolo")
    body = models.TextField()
    main_avatar = models.ImageField(verbose_name="avatar artista", null=True, blank=True)
    sub_avatar = models.ImageField(verbose_name="avatar opera", null=True, blank=True)
    artist = models.CharField(max_length=64, verbose_name="artista")

    def __str__(self):
        return f"{self.title} ({self.artist})"


class Project(models.Model):

    name = models.CharField(max_length=64, verbose_name="nome programmatico", primary_key=True)
    title = models.CharField(max_length=128, verbose_name="titolo")
    body = models.TextField()
    main_img = models.ImageField(verbose_name="avatar artista", null=True, blank=True)
    tags = models.CharField(max_length=256, verbose_name="tags separate da ','")

    def __str__(self):
        return self.title
