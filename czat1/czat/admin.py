from django.contrib import admin
from czat import models  # importujemy nasz model

# Register your models here.
# -*- coding: utf-8 -*-
# czatpro/czat/admin.py
# rejestrujemy model Wiadomosc w panelu administracyjnym
admin.site.register(models.Wiadomosc)
