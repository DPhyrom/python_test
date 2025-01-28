from django.db import models

    
#category model
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    

#product model
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='productImages/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Cat_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categoryID')

    def __str__(self):
        return self.name
