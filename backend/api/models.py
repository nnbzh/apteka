from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"


class Category(models.Model):
    name = models.CharField(max_length=300)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="types")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"


class Manufacturer(models.Model):
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"


class Description(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="manufacturers")
    end_date = models.DateTimeField(blank=True)
    create_date = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = "Description"
        verbose_name_plural = "Descriptions"


class Product(models.Model):
    name = models.CharField(max_length=300)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="subcategories")
    price = models.IntegerField()
    description = models.OneToOneField(Description, on_delete=models.CASCADE, related_name="description")
    rating = models.FloatField()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Pharmacy(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")

    class Meta:
        verbose_name = "Pharmacy"
        verbose_name_plural = "Pharmacies"
