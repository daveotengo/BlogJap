# Generated by Django 4.0.3 on 2022-03-24 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=50)),
                ('post_content', models.TextField(max_length=225)),
                ('post_status', models.BooleanField(default=False)),
                ('post_image', models.CharField(blank=True, max_length=225, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now_add=True)),
                ('post_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
                ('post_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'post',
                'managed': True,
            },
        ),
    ]