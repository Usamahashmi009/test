from django.contrib import admin
from .forms import StockCreateForm,AddItemCompanyForm,AddItemSizeForm,AddVenderForm
from .models import Stock,Company,ItemSize,Vender


class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['item_size', 'quantity','rate','company']
   form = StockCreateForm
   list_filter = ['category']
   search_fields = ['category', 'item_name']




class CompanycreateAdmin(admin.ModelAdmin):
   list_display = ['name']
   form = AddItemCompanyForm


class ItemcreateAdmin(admin.ModelAdmin):
   list_display= ['name']
   form = AddItemSizeForm

class VendorcreateAdmin(admin.ModelAdmin):
   list_display= ['name']
   form = AddVenderForm


admin.site.register(Stock,StockCreateAdmin)

admin.site.register(Company,CompanycreateAdmin)

admin.site.register(ItemSize,ItemcreateAdmin)

admin.site.register(Vender,VendorcreateAdmin)