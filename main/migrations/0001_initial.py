# Generated by Django 3.2.5 on 2021-09-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromWho', models.CharField(max_length=30, verbose_name='Kim tarafından ')),
                ('description', models.CharField(max_length=135, verbose_name='Açıklama')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Paylaşılma zamanı')),
                ('likeCount', models.IntegerField(verbose_name='Beğeni sayısı')),
                ('commentCount', models.IntegerField(verbose_name='Yorum sayısı')),
            ],
        ),
    ]