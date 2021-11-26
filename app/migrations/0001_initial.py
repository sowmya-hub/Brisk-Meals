from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('subject', models.TextField(default='')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=230)),
                ('email', models.EmailField(max_length=254)),
                ('time', models.IntegerField(default='')),
                ('phone', models.TextField(default='')),
                ('people', models.IntegerField(default='')),
                ('message', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
