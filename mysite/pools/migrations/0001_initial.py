# Generated by Django 2.2 on 2019-06-02 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_questao', models.CharField(max_length=200)),
                ('fechada', models.BooleanField(default=False)),
                ('data_pub', models.DateField(verbose_name='data publicada')),
            ],
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_opcao', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pools.Questao')),
            ],
        ),
    ]
