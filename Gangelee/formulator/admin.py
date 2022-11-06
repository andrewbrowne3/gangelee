from django.contrib import admin
from .models import Formulation,Product,Instruction, Raw_Materials
# Register your models here.
admin.site.register(Formulation)
admin.site.register(Product)
admin.site.register(Instruction)
admin.site.register(Raw_Materials)
