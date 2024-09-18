from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=21)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=33)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    have = models.BooleanField(default=True)
    created_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Comment(models.Model):
    name = models.CharField(max_length=33)
    test = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.product}'


