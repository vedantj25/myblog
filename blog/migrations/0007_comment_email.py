# Generated by Django 4.1 on 2022-08-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_snippet_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='abc@xyz.com', max_length=254),
        ),
    ]
