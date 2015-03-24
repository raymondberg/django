# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=14)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnimalRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('liking', models.IntegerField(validators=(django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0)))),
                ('tagalong', models.IntegerField()),
                ('ratee', models.ForeignKey(related_name='of_animal', to='partymaker.Animal')),
                ('rater', models.ForeignKey(related_name='by_animal', to='partymaker.Animal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('zip_code', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='animal',
            name='neighborhood',
            field=models.ForeignKey(blank=True, to='partymaker.Neighborhood', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animal',
            name='ratings',
            field=models.ManyToManyField(related_name='ratings+', through='partymaker.AnimalRating', to='partymaker.Animal'),
            preserve_default=True,
        ),
    ]
