# Generated by Django 2.2 on 2019-06-20 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcao',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opcoes', to='pools.Questao'),
        ),
    ]
