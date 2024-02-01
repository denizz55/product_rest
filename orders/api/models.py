from django.db import models

# Create your models here.

class Orders(models.Model):
    oder_date = models.DateTimeField(auto_now_add=True)
    cust = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    prod = models.ForeignKey('products', related_name='products', on_delete=models.CASCADE)
    quantite = models.IntegerField()
    price = models.FloatField()

    class Meta:
        ordering = ['order_date']

class Products(models.Model):
    Title = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'products'