# Generated by Django 4.0 on 2024-07-26 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.CharField(choices=[('jaxon', 'jaxon'), ('ozbekiston', 'ozbekiston'), ('iqtisod', 'iqtisod')], default='ozbekiston', max_length=100),
        ),
    ]
