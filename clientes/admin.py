from clientes.models import *
from django.contrib import admin

class ClienteAdmin(admin.ModelAdmin):
	list_filter = ['categoria']
	search_fields = ['nombre','telefonos']
	list_display = ['nombre','telefonos']


admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Cliente, ClienteAdmin)