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

    def __str__(self):
        return str(self.title)
