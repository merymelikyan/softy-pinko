from django.contrib import admin
from .models import (
    HeaderText, 
    FooterText, 
    TreeBlocks,
    LeftBlock,
    RightBlock
)


class HeaderTextAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if HeaderText.objects.count() >= 6:
            return False
        return super().has_add_permission(request)
    
    def save_model(self, request, obj, form, change):
        if not change and HeaderText.objects.count() >= 6:
            from django.core.exceptions import ValidationError
            raise ValidationError('You cannot add more than 6 items.')
        super().save_model(request, obj, form, change)


class FooterTextAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if FooterText.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    
    def save_model(self, request, obj, form, change):
        if not change and FooterText.objects.count() >= 1:
            from django.core.exceptions import ValidationError
            raise ValidationError('You cannot add more than 1 items.')
        super().save_model(request, obj, form, change)


class TreeBlocksAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if TreeBlocks.objects.count() >= 3:
            return False
        return super().has_add_permission(request)
    
    def save_model(self, request, obj, form, change):
        if not change and TreeBlocks.objects.count() >= 3:
            from django.core.exceptions import ValidationError
            raise ValidationError('You cannot add more than 3 items.')
        super().save_model(request, obj, form, change)


class LeftBlockAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if LeftBlock.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    
    def save_model(self, request, obj, form, change):
        if not change and LeftBlock.objects.count() >= 1:
            from django.core.exceptions import ValidationError
            raise ValidationError('You cannot add more than 1 items.')
        super().save_model(request, obj, form, change)


class RightBlockAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if RightBlock.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    
    def save_model(self, request, obj, form, change):
        if not change and RightBlock.objects.count() >= 1:
            from django.core.exceptions import ValidationError
            raise ValidationError('You cannot add more than 1 items.')
        super().save_model(request, obj, form, change)
