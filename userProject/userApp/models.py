from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.DecimalField(max_digits=3, decimal_places=1)
    profession = models.CharField(max_length=40)
    sal = models.DecimalField(max_digits=10, decimal_places=3)
    email = models.EmailField(max_length=254)

    #returns the string represenation of the object when the object is called
    def __str__(self):
        return self.name+self.age+self.profession+self.sal+self.email
    