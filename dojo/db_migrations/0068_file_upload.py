# Generated by Django 2.2.17 on 2020-12-17 22:30

from django.db import migrations, models
import dojo.models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0067_max_dupes'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('file', models.FileField(upload_to=dojo.models.UniqueUploadNameProvider('uploaded_files'))),
            ],
        ),
        migrations.AddField(
            model_name='engagement',
            name='files',
            field=models.ManyToManyField(blank=True, editable=False, to='dojo.FileUpload'),
        ),
        migrations.AddField(
            model_name='finding',
            name='files',
            field=models.ManyToManyField(blank=True, editable=False, help_text='Files(s) related to the flaw.', to='dojo.FileUpload', verbose_name='Files'),
        ),
        migrations.AddField(
            model_name='test',
            name='files',
            field=models.ManyToManyField(blank=True, editable=False, to='dojo.FileUpload'),
        ),
    ]