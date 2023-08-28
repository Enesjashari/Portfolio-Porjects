# Generated by Django 4.2.4 on 2023-08-19 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.CharField(default=' ', max_length=1000, primary_key=True, serialize=False)),
                ('name', models.CharField(default=' ', max_length=1000)),
                ('authors', models.CharField(default=' ', max_length=1000)),
                ('title', models.CharField(default=' ', max_length=1000)),
                ('comments', models.CharField(default=' ', max_length=1000)),
                ('journal_ref', models.CharField(default=' ', max_length=1000)),
                ('doi', models.CharField(default=' ', max_length=1000)),
                ('report_no', models.CharField(default=' ', max_length=1000)),
                ('categories', models.CharField(default=' ', max_length=1000)),
                ('license', models.CharField(default=' ', max_length=1000)),
                ('abstract', models.CharField(default=' ', max_length=1000)),
                ('authors_parsed', models.CharField(default=' ', max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='paper',
            name='authors',
            field=models.ManyToManyField(default=' ', to='app.author'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
