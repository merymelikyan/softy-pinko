from django.contrib import admin
from .models import (
    HeaderText,
    SEO,
    OG
    )



class HeaderTextAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if HeaderText.objects.exists():
            return False
        return super().has_add_permission(request)

admin.site.register(HeaderText, HeaderTextAdmin)
admin.site.register(SEO)
admin.site.register(OG)