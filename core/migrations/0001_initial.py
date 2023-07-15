# Generated by Django 4.2.3 on 2023-07-03 20:51

from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='cat', unique=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(default='blank', upload_to='category')),
                ('description', models.TextField(blank=True)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_categories', to='core.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
