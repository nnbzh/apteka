from django.contrib import admin

# Register your models here.
from api.models import Category, Type, Pharmacy, Description, Product, SubCategory, Manufacturer


class CustomModelAdminMixin(object):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdminMixin, self).__init__(model, admin_site)


class Admin(CustomModelAdminMixin, admin.ModelAdmin):
    pass


admin.site.register(Category, Admin)
admin.site.register(Type, Admin)
admin.site.register(Pharmacy, Admin)
admin.site.register(Description, Admin)
admin.site.register(Product, Admin)
admin.site.register(SubCategory, Admin)
admin.site.register(Manufacturer, Admin)

