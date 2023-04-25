from django.contrib import admin

# Register your models here.
from .models import candidates
from .models import interview
admin.site.register(candidates)
admin.site.register(interview)