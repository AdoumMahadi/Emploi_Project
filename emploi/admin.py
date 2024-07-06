from django.contrib import admin

# Register your models here.
from .models import Emploi

# admin.site.register(Emploi)


@admin.register(Emploi)
class BlogEmploi(admin.ModelAdmin):
    list_display = ('title', 'date_emploi_fixee',)


# admin.site.register(Emploi, BlogEmploi)
