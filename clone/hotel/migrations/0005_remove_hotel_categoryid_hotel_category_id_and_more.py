# Generated by Django 4.1.4 on 2022-12-24 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='categoryid',
        ),
        migrations.AddField(
            model_name='hotel',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hotel.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayir')], max_length=10),
        ),
    ]
