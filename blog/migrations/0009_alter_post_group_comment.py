# Generated by Django 4.0 on 2024-07-31 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.CharField(choices=[('jaxon', 'jaxon'), ('ozbekiston', 'ozbekiston'), ('iqtisod', 'iqtisod')], default='ozbekiston', max_length=100),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Foydalanuvchi')),
                ('comment_text', models.TextField(max_length=1000, verbose_name='Kommentariya')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
            options={
                'verbose_name': 'Kommentariya',
                'verbose_name_plural': 'Kommentariyalar',
            },
        ),
    ]
