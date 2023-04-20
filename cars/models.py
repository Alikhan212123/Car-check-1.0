from django.db import models

class Car(models.Model):
    number = models.CharField(
        max_length=10,
        verbose_name="Номер машины"

    )
    make = models.CharField(
        max_length=50,
        verbose_name="Бренд машины"

        )
    model = models.CharField(
        max_length=50,
        verbose_name="Модель машины"

        )
    year = models.CharField(
        max_length=50,
        verbose_name="Год выпуска"
    )

    def __str__(self):
        return self.number