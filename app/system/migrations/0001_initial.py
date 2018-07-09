# Generated by Django 2.0 on 2018-07-09 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_name', models.CharField(help_text='Enter the name', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_name', models.CharField(help_text='Enter the name', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(help_text='Enter the name', max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Task'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ManyToManyField(to='system.Question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Task'),
        ),
    ]