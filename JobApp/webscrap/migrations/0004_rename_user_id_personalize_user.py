from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webscrap', '0003_rename_name_tags_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalize',
            old_name='user_id',
            new_name='user',
        ),
    ]
