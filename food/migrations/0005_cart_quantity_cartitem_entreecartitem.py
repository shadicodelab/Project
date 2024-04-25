# Generated by Django 5.0.2 on 2024-04-25 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_cart_entrees'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('appetizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.appetizer')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.cart')),
            ],
        ),
        migrations.CreateModel(
            name='EntreeCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.cart')),
                ('entree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.entree')),
            ],
        ),
    ]
