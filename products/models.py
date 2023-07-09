from django.db import models


class Products(models.Model):
    """
    The Database model containing the products scheme
    """
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(default=False, null=True, blank=True)
    in_stock = models.BooleanField(default=True, null=True)
    quantity = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.title)
