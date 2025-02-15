from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('DVD', 'DVD'),
        ('VHS', 'VHS'),
        ('Equipos de Video', 'Equipos de Video'),
    ]
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=300, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    picture = models.ImageField(upload_to="catalogo_images")

    def __str__(self):
        return self.name

class DVD(Product):
    year = models.DateField(auto_now=False, auto_now_add=False, null=False)
    GENRE_TYPES = [
        ('Acción', 'Acción'),
        ('Aventura', 'Aventura'),
        ('Terror', 'Terror'),
        ('Ciencia ficción', 'Ciencia ficción'),
        ('Comedia', 'Comedia'),
        ('Drama', 'Drama'),
    ]
    genre = models.CharField(max_length=30, choices=GENRE_TYPES, null=False)

class VHS(Product):
    year = models.DateField(auto_now=False, auto_now_add=False, null=False)
    VHS_TYPE = [
        ('Película', 'Película'),
        ('Música', 'Música'),
        ('Documental', 'Documental'),
        ('Audible', 'Audible'),
    ]
    type = models.CharField(max_length=30, choices=VHS_TYPE, null=False)

class VideoEquipments(Product):
    year = models.DateField(auto_now=False, auto_now_add=False, null=False)

class Client(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=30)
    phone = models.IntegerField(default=1, null=False)
    adress = models.CharField(max_length=100, null=False)
    PAYMENT_METHOD = {
        ('Tarjeta de crédito', 'Tarjeta de crédito'),
        ('Tarjeta de débito', 'Tarjeta de débito'),
    }
    payment = models.CharField(max_length=30, choices=PAYMENT_METHOD, null=False)
    
    def __str__(self):
        return self.name

class Purchase(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)