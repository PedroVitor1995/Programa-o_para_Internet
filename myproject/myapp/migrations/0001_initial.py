# Generated by Django 2.2 on 2019-05-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=30)),
                ('segundo_nome', models.CharField(max_length=30)),
                ('data_pub', models.DateField()),
                ('tam_roupa', models.CharField(choices=[('P', 'Pequena'), ('M', 'Media'), ('G', 'Grande')], max_length=1, null=True)),
            ],
        ),
    ]