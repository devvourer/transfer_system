# Generated by Django 3.2.2 on 2021-05-08 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('USD', 'Us dollars'), ('EUR', 'Euro'), ('GBP', 'Uk pounds'), ('BTC', 'Bitcoin'), ('RUB', 'Rubles')], default='EUR', max_length=3)),
                ('balance', models.DecimalField(decimal_places=2, default=10, max_digits=9)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
