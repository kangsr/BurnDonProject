# Generated by Django 3.2.7 on 2021-09-25 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goldMoney', models.IntegerField(null=True)),
                ('currentMoney', models.IntegerField(null=True)),
                ('salary', models.IntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('beforeExpense', models.IntegerField(null=True)),
                ('afterExpense', models.IntegerField(null=True)),
            ],
        ),
    ]