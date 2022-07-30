from django.contrib import admin
from django.utils.html import format_html

from test_app.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "type", "status")
    fields = ("first_name", "last_name", "age", "type", "social_url")

    def full_name(self, instance):
        if instance.social_url:
            return format_html(f'<a href= "{instance.social_url}"> {instance.first_name}{instance.last_name}</a>')
        else:
            return f'{instance.first_name} {instance.last_name}'
