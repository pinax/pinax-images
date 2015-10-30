# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.utils.timezone
import pinax.images.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('image', models.ImageField(upload_to=pinax.images.models.image_upload_to)),
                ('original_filename', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(related_name='images', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImageSet',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(related_name='image_sets', to=settings.AUTH_USER_MODEL)),
                ('primary_image', models.ForeignKey(to='images.Image', on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='image_set',
            field=models.ForeignKey(related_name='images', to='images.ImageSet'),
        ),
    ]
