# Generated by Django 3.2.11 on 2022-10-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20221014_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='status',
            field=models.CharField(choices=[('free', 'Cвободен'), ('in_work', 'В работе'), ('on_the_way', 'В пути')], default='free', max_length=255, verbose_name='Статус ТС'),
        ),
    ]