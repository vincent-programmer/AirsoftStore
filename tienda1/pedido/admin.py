from django.contrib import admin

from pedido.models import Category,Articulos

from mptt.admin import DraggableMPTTAdmin

# Register your models here.
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Articulos,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Articulos,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

class ProductoAdmin(admin.ModelAdmin):
    #list_display=("nombre", "categoria", "precio")
    search_fields=("nombre", "category")
    list_filter=("category","autor")
admin.site.register(Category, CategoryAdmin)
admin.site.register(Articulos, ProductoAdmin)