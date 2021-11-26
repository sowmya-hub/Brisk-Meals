from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='phone',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='table',
            name='time',
            field=models.CharField(default='', max_length=12),
        ),
    ]
