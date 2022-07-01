from django.contrib import admin
from .models import Movie, Myrating
from .models import Profile

# Register your models here.
admin.site.site_header = 'Movies'
admin.site.register(Profile)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','genre','director')

class MyratingAdmin(admin.ModelAdmin):
    list_display = ('movie','user','rating')
admin.site.register(Movie,MovieAdmin)
admin.site.register(Myrating,MyratingAdmin)

