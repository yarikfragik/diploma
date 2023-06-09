from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscrap', '0004_rename_user_id_personalize_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=100)),
                ('username', models.CharField(default='', max_length=100)),
                ('query', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
