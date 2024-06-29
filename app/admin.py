from django.contrib import admin
from .models import (
    HeaderText, 
    FooterText, 
    TreeBlocks, 
    LeftBlock, 
    RightBlock,
    WorkProcessMain,
    WorkProcessChild
    )
from .admin_hooks import (
    HeaderTextAdmin, 
    FooterTextAdmin, 
    TreeBlocksAdmin, 
    LeftBlockAdmin, 
    RightBlockAdmin
    )
                    
class WorkProcessChildInline(admin.TabularInline):
    model = WorkProcessChild
    extra = 1


class WorkProcessMainAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if WorkProcessMain.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def save_model(self, request, obj, form, change):
        if not change and WorkProcessMain.objects.count() >= 1:
            from django.core.exceptions import ValidationError
            raise ValidationError('You cannot add more than 1 items.')
        super().save_model(request, obj, form, change)

    inlines = [WorkProcessChildInline]
    list_display = ('title', 'description')

admin.site.register(HeaderText, HeaderTextAdmin)
admin.site.register(FooterText, FooterTextAdmin)
admin.site.register(TreeBlocks, TreeBlocksAdmin)
admin.site.register(LeftBlock, LeftBlockAdmin)
admin.site.register(RightBlock, RightBlockAdmin)
admin.site.register(WorkProcessMain, WorkProcessMainAdmin)
