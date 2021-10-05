from django.contrib import admin
from .models import Page, Post, Package, PostPackage, BulkDiscount, Promo 

# Register your models here.
admin.site.register(Page)
admin.site.register(Post)
admin.site.register(Package)
admin.site.register(PostPackage)
admin.site.register(BulkDiscount)
admin.site.register(Promo)