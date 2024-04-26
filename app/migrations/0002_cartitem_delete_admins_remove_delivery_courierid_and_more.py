# Generated by Django 4.2.11 on 2024-03-30 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.menuitems')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Admins',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='CourierID',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='OrderID',
        ),
        migrations.DeleteModel(
            name='DeliveryAreas',
        ),
        migrations.DeleteModel(
            name='Couriers',
        ),
        migrations.DeleteModel(
            name='Delivery',
        ),
    ]
