# Generated by Django 5.1 on 2024-08-30 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dados_pessoais',
            name='dd_telefone',
        ),
        migrations.AddField(
            model_name='dados_pessoais',
            name='ddd_telefone',
            field=models.CharField(default='00', max_length=2, verbose_name='ddd'),
        ),
    ]
