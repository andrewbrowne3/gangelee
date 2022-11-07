from django.db import models
import uuid

# Create your models here.

Line_type = ( 
    ('Raw', 'Raw'),
    ('Stage', 'Stage'),
    ('Instr', 'Instr'),
    )


class Product(models.Model):
    Name = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    Formulation =models.ForeignKey('Formulation', blank=True, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.Name


class Formulation(models.Model):
    Code = models.IntegerField(max_length=20, unique=True)
    Total_Formation_Weight = models.IntegerField(max_length=200)
    Line_type = models.CharField(max_length=200, choices=Line_type)
    #Ingredient =models.CharField(max_length=200) 
    #purpose = models.CharField(max_length=200)
    Raw_Materials = models.ManyToManyField('Raw_Materials',blank=True)
    Quantity = models.CharField(max_length=200)
    percentage_weight = models.CharField(max_length=200)
    unit_cost =models.CharField(max_length=200)
    instruction_id = models.OneToOneField('Instruction', on_delete=models.PROTECT,blank=True,null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    Product =models.ForeignKey('Product',on_delete=models.CASCADE,blank=True,null=True)

    def actual_weight(self):
        return (float(0.01) * float(self.percentage_weight)) * float(self.Total_Formation_Weight)

    def __str__(self):
        return f'{self.Code}'

    

class Raw_Materials(models.Model):
    Name = models.CharField(max_length=200)
    Purpose = models.CharField(max_length=200)
    #Formulation = models.ForeignKey(Formulation,on_delete=models.CASCADE,blank=True, null=True)
    #she wants the code to have integers and letters because she wants to put the type of material it is like s for surfectant 
    Code = models.IntegerField(max_length=20, unique=True, blank=True,null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.Name


class Instruction(models.Model):
    #step = models.CharField(max_length=200)
    instructions = models.CharField(max_length=200)
    special_notes = models.CharField(max_length=200)
    formulation_field =  models.OneToOneField(
        Formulation,
        on_delete=models.CASCADE
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return f"instructions for formulation {self.formulation_field}"
