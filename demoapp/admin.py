# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Business)
admin.site.register(User)
admin.site.register(Viewer)
admin.site.register(Contact)
admin.site.register(Listing)
admin.site.register(Financial)
admin.site.register(DataType)
