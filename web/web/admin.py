from django.contrib import admin

from web.models import ArtistQuote, Project

@admin.register(ArtistQuote)
class ArtistQuoteAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'title', 'body', 'artist')
    

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'title', 'body', 'tags')
    
