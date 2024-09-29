from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        # اسم مستعار
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255)
    description = models.TextField(max_length=3500)

    inventory = models.PositiveIntegerField(default=0)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.PositiveIntegerField(default=0)
    offers = models.PositiveIntegerField(default=0)
    new_price = models.PositiveIntegerField(default=0)

    # date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.name


class ProductFeatures(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='features')

    def __str__(self):
        return f'{self.name}: {self.value}'


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_file = models.ImageField(upload_to='product_images/%Y/%m/%d/')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created'])]

    def __str__(self):
        return self.title
