from django.utils.translation import gettext as _
from django.db import models
from django.contrib.auth.models import User

class manytomany3foreignkey(models.Model):
    titleforeignkey = models.CharField(_("Title"), max_length=80, default="", blank=False, null=False)

    def __str__(self):
        return str(self.titleforeignkey)


class manytomany3manytomany(models.Model):
    titlemanytomany = models.CharField(_("Title"), max_length=80, default="", blank=False, null=False)

    def __str__(self):
        return str(self.titlemanytomany)

class manytomany3(models.Model):
    title1 = models.CharField(_("Title"), max_length=80, default="", blank=False, null=False)
    title2 = models.CharField(_("Title2"), max_length=80, default="", blank=False, null=False)
    manytomany_link = models.ManyToManyField(manytomany3manytomany, default=None, blank=True, null=True)
    foreignkey_link = models.ForeignKey(manytomany3foreignkey, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return str(self.title1)
