# Generated by Django 2.1.5 on 2019-09-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageurl', models.ImageField(upload_to='Images/')),
                ('Tname', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Teams',
            },
        ),
    ]
