from django.db import models

CATS = (
    ('APP', 'Apps and Sides'),
    ('ENT', 'Entree'),
    ('DES', 'Dessert'),
    ('SOS', 'Soups and Salads'),
    ('SPE', 'Special'),
    ('DNK', 'Soft Drink'),
    ('BAR', 'Bar Drink')
)

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=3, choices=CATS)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    def __str__(self):
        return self.name

class Table(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    bill = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    grat15 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    grat18 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    grat20 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    dtg = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Table {self.number}'
    
class Cover(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    seat = models.IntegerField
    items = models.ManyToManyField(Item)
    subtot = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    def __str__(self):
        return f'Table {self.table} Seat {self.seat}'
