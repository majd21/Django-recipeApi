# Generated by Django 3.1.2 on 2020-12-21 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipe.recipe'),
        ),
    ]
