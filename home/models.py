from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=20)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.model}   {self.year}'


class Person(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    email = models.EmailField()


    def __str__(self):
        return self.name
