from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Quote(models.Model):
    quote_text = models.TextField(max_length=512)
    character = models.ForeignKey(Character, on_delete=models.RESTRICT)

    def __str__(self):
        return self.quote_text

