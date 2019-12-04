from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=64)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=100,default=29.99)
    sale_price=models.DecimalField(decimal_places=2,max_digits=100,null=True)
    slug=models.SlugField(max_length=64,unique_for_date="added")
    added=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('-added',)

    def __unicode__(self):
        return self.title

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=True)
    image=models.ImageField(upload_to='static/image/')
    featured=models.BooleanField(default=False)
    thumbnail=models.BooleanField(default=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)

    def __unicode__(self):
        return self.product.title
