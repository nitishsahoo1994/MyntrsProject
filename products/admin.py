from django.contrib import admin
from products.models import Product,ProductImage

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'added'
    list_display = ['title','description','price','slug','added','updated','active']
    prepopulated_fields = {'slug':('title',),}
    search_fields = ('title','description')
    list_editable = ('price','active')
    list_filter = ('price','active')
    readonly_fields = ('added','updated')
    class Meta:
        model=Product


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
