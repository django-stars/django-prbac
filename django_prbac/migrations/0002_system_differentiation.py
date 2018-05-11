from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_prbac', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='is_system',
            field=models.BooleanField(
                default=False,
                help_text='Indicates whether or not the role is a system Role or custom',
            ),
        ),
    ]
