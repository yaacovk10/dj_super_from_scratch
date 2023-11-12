from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

# # To set a default Category for Product
# default_category, created = Category.objects.create(description='Default Category')
    
class Product(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null= False)
    img = models.ImageField()
 
    def __str__(self):
           return self.desc


# # Now, set the default category in the Product model
# Product._meta.get_field('category').default = default_category
