from django.contrib import admin
from .models import AddClient, VectorWork


class AddClientAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Second_Name', 'Company', 'Work_field', 'content', 'email', 'Add_Time', 'vectorWork')
    list_display_links = ('Name', 'Second_Name')
    search_fields = ('Company', 'Work_field')


admin.site.register(AddClient, AddClientAdmin)
admin.site.register(VectorWork)


# Register your models here.
