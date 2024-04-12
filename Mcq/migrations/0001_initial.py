# Generated by Django 5.0.4 on 2024-04-10 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approver_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=255)),
                ('subject_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=255)),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mcq.subject')),
            ],
        ),
        migrations.CreateModel(
            name='SubTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_topic_name', models.CharField(max_length=255)),
                ('topic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mcq.topic')),
            ],
            options={
                'unique_together': {('topic_name', 'sub_topic_name')},
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('options', models.TextField()),
                ('opt_values', models.TextField()),
                ('correct_options', models.TextField(max_length=255)),
                ('selective_cnt', models.CharField(max_length=255)),
                ('difficulty', models.CharField(max_length=255)),
                ('explanation', models.TextField()),
                ('reference', models.TextField()),
                ('source', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('visibility_flag', models.BooleanField(default=True)),
                ('approver_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mcq.approver')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mcq.subject')),
                ('sub_topic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mcq.subtopic')),
                ('topic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mcq.topic')),
            ],
        ),
    ]
