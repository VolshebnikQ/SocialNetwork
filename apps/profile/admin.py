from django.apps import apps
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext, gettext_lazy as _

from .models import User, Friend


# Redefining models in other applications
# !!! ЗАКОММЕНТИРОВАТЬ ПРИ МИГРАЦИЯХ !!!
# apps.get_model('account.EmailAddress')._meta.app_label = 'profile'
# apps.get_model('auth.Group')._meta.app_label = 'profile'


class UserAdmin(admin.ModelAdmin):
    """Registering a custom model in the admin panel."""
    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        'get_image'
    ]
    list_display_links = ('username',)
    ordering = ('username',)
    readonly_fields = ['get_image', ]
    search_fields = ['username']
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password')}),
        (_('Personal info'),
            {'fields': (
                'first_name',
                'last_name',
                'birthday',
                'sex',
                'city',
                'email',
                'phone_number',
                'about')}),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'), }),
        (_('Important dates'), {
            'fields': (
                'last_login',
                'date_joined')}),
        (_('Avatar'), {
            'fields': (
                'avatar',)}),
    )

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.avatar.url} width="60px" height="auto"'
        )

    get_image.short_description = 'Avatar'


admin.site.register(User, UserAdmin)
admin.site.register(Friend)
