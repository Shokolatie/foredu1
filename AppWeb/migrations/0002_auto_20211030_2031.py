# Generated by Django 3.2.8 on 2021-10-30 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VectorWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bis', models.CharField(db_index=True, max_length=20, verbose_name='Направление бизнеса')),
            ],
            options={
                'verbose_name': 'Область бизнеса',
                'verbose_name_plural': 'Области бизнеса',
                'ordering': ['bis'],
            },
        ),
        migrations.AlterModelOptions(
            name='addclient',
            options={'ordering': ['-Add_Time'], 'verbose_name': 'Список клиентов', 'verbose_name_plural': 'Список клиентов'},
        ),
        migrations.AlterField(
            model_name='addclient',
            name='Add_Time',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавления в базу'),
        ),
        migrations.AlterField(
            model_name='addclient',
            name='Company',
            field=models.CharField(max_length=40, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='addclient',
            name='Name',
            field=models.CharField(max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='addclient',
            name='Second_Name',
            field=models.CharField(max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='addclient',
            name='Work_field',
            field=models.CharField(max_length=40, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='addclient',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='контент'),
        ),
        migrations.AlterField(
            model_name='addclient',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='addclient',
            name='vectorWork',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='AppWeb.vectorwork', verbose_name='Направление бизнеса'),
        ),
    ]