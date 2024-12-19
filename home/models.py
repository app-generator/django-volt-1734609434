# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    phone = models.CharField(max_length=255, null=True, blank=True)
    type = models.TextField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Olts(models.Model):

    #__Olts_FIELDS__
    reseller = models.CharField(max_length=255, null=True, blank=True)
    olt id = models.CharField(max_length=255, null=True, blank=True)
    subscription status = models.BooleanField()
    subscription end date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Olts_FIELDS__END

    class Meta:
        verbose_name        = _("Olts")
        verbose_name_plural = _("Olts")


class Invoice(models.Model):

    #__Invoice_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    client = models.CharField(max_length=255, null=True, blank=True)

    #__Invoice_FIELDS__END

    class Meta:
        verbose_name        = _("Invoice")
        verbose_name_plural = _("Invoice")


class Client(models.Model):

    #__Client_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    service = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Client_FIELDS__END

    class Meta:
        verbose_name        = _("Client")
        verbose_name_plural = _("Client")



#__MODELS__END
