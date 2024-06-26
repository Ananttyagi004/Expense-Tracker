# Generated by Django 5.0.1 on 2024-03-26 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('Cateogry', models.CharField(choices=[('food', 'Food'), ('housing', 'Housing'), ('transportation', 'Transportation'), ('utilities', 'Utilities'), ('entertainment', 'Entertainment'), ('healthcare', 'Healthcare'), ('education', 'Education'), ('clothing', 'Clothing'), ('other', 'Other')], max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
