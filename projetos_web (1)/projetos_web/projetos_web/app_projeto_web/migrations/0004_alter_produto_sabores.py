# Generated by Django 5.1.3 on 2024-11-25 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projeto_web', '0003_alter_produto_acucar_alter_produto_carboidratos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='sabores',
            field=models.TextField(max_length=255),
        ),
    ]
