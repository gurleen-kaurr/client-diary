from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=150)
    client_address = models.TextField()
    client_area = models.CharField(max_length=100 ,null=True, blank=True)
    client_phno = models.IntegerField(max_length=10, unique=True)
    client_service_date = models.DateField()
    client_paymentmode =  models.CharField(max_length=20, choices=[('cash', 'Cash'), ('card', 'Card')])
    client_staff = models.CharField(max_length=100, default= "self")

    def __str__(self):
        return self.client_name
