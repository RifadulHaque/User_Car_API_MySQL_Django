from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.DecimalField(max_digits=3, decimal_places=1)
    profession = models.CharField(max_length=40)
    sal = models.DecimalField(max_digits=10, decimal_places=3)
    email = models.EmailField(max_length=50)

    #returns the string represenation of the object when the object is called
    def __str__(self):
        return 'name: '+self.name+'age: '+self.age+'profession: '+self.profession+ 'salary: '+self.sal+'email: '+self.email

class Car(models.Model):
    car_name = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    user = models.ForeignKey(User,related_name='cars',on_delete=models.CASCADE) #on_delete is used for cascade which will delte the book when the auher is deleted

    #returns the string represenation of the object when the object is called
    def __str__(self):
        return 'name: '+self.car_name+'brand: '+self.brand+'year: '+self.year