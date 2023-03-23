from django.contrib import admin

from engine.models import Schema, Data


class DataAdmin(admin.ModelAdmin):
    list_display = ('data_name', 'data_type', 'order', 'created_at')


class SchemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


admin.site.register(Schema, SchemaAdmin)
admin.site.register(Data, DataAdmin)
