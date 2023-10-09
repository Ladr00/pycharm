# Generated by Django 4.2.5 on 2023-10-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_category_alter_news_options_alter_news_content_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='фото'),
        ),
    ]
