from django.shortcuts import render
from .models import Product, Formulation, Raw_Materials
# Create your views here.


def ProductsPage(request):
    x = Product.objects.all()
    return render(request, 'Formulator/Products.html',{'products':x})


def ProductInformation(request, pk):
    productObj = Product.objects.get(id=pk)
    y = Formulation.objects.all()
    FormulationObj = Formulation.objects.filter(Product=productObj)
    context = {'product':productObj, 'formulation':FormulationObj,'formulations':y} 
    return render(request, 'Formulator/ProductInformation.html',context)

def FormulationInformation(request, pk):
    FormulationObject = Formulation.objects.get(id=pk)
    Raw_Materials = FormulationObject.Raw_Materials.all()
   # IngredientObj = Ingredient.objects.filter(formulation=FormulationObject)
    context = {'formulation':FormulationObject}
    return render(request, 'Formulator/FormulationInformation.html',context)