# Generated by Django 3.2.11 on 2022-01-14 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_alter_transacao_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contas.categoria'),
        ),
    ]
