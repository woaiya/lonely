# Generated by Django 2.2.4 on 2019-09-09 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20190909_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendmodels',
            name='recommend_graphic_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='myblog.GraphicRecordModels', verbose_name='图文博客ID'),
        ),
    ]