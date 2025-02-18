from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='category',
            field=models.TextField(choices=[('P', 'Smart Phone'), ('L', 'Laptops'), ('M', 'Machines'), ('T', 'Tablet'), ('O', 'Others')], default='P', max_length=1),
        ),
    ]
