from django.contrib import admin
from .models import People, TGPeople


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = "name", "phone_number", "created_at", "updated_at"
    search_fields = "name", "phone_number"
    list_filter = "created_at", "updated_at"


@admin.register(TGPeople)
class PeopleAdmin(admin.ModelAdmin):
    list_display = "id", "name", "created_at", "updated_at"
    search_fields = "name",
    list_filter = "created_at", "updated_at"
