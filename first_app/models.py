from django.db import models

class SecondModel(models.Model):
    cifra = models.IntegerField(verbose_name='Поля с цифрой')

    def __str__(self):
        return f'{self.cifra}'

class FirstModel(models.Model):
    name = models.CharField(verbose_name='Первое имя', max_length=100)
    second = models.ManyToManyField(SecondModel, blank=True)
    new = models.OneToOneField(SecondModel, related_name='new', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
