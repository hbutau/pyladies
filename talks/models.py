from django.db import models
from markitup.fields import MarkupField

class Talk_Type(models.Model):

    talk_types = (
        ('S', "Short_Talk"),
        ('L', "Long_Talk"),
         ('T', "Tutorial"),
    )

    name = models.CharField(choices=talk_types, max_length=1)

    def __str__(self):
        return u"%s" % (self.name)

class Proposal(models.Model):

    title = models.CharField(max_length=1024)
    abstract = MarkupField(help_text="Describe what your talk is about")
    talk_type = models.ForeignKey(Talk_Type)

    def __str__(self):
        return self.title
