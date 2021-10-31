from django.db import models
# Модель добавляющая клиента в базу


class AddClient(models.Model):
    Name = models.CharField(max_length=20, verbose_name='Имя')
    Second_Name = models.CharField(max_length=20, verbose_name='Фамилия')
    Company = models.CharField(max_length=40, verbose_name='Компания')
    Work_field = models.CharField(max_length=40, verbose_name='Область')
    content = models.TextField(null=True, blank=True, verbose_name='контент')
    email = models.EmailField(max_length=254, verbose_name='Email')
    Add_Time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавления в базу')
    vectorWork = models.ForeignKey('VectorWork', null=True, on_delete=models.PROTECT, verbose_name='Направление бизнеса')

    class Meta:
        verbose_name_plural = 'Список клиентов'
        verbose_name = 'Список клиентов'
        ordering = ['-Add_Time']
        unique_together = ('email')



class VectorWork(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Направление бизнеса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Области бизнеса'
        verbose_name = 'Область бизнеса'
        ordering = ['name']




