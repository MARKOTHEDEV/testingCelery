from django.db import models

# Create your models here.


class TestingME(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self) -> str:
        return f'Hello world {self.id}'