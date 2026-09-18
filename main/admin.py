from django.contrib import admin
from .models import Quote, GalleryItem
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display=("text","source","order")
    list_editable=("order",)
@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display=("title","image_url","order")
    list_editable=("order",)
