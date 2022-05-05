# Generated by Django 3.1.6 on 2022-04-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('python', 'Python'), ('java', 'Java'), ('c++', 'C++')], default='python', max_length=6)),
                ('title', models.CharField(max_length=250)),
                ('code', models.TextField()),
                ('inp', models.TextField()),
                ('output', models.TextField()),
            ],
        ),
    ]
