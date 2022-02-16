# Generated by Django 4.0a1 on 2022-02-11 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_chapter',
            fields=[
                ('chapter_id', models.AutoField(primary_key=True, serialize=False)),
                ('chapter_name', models.CharField(max_length=100)),
                ('chapter_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_class',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=100)),
                ('class_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_stream',
            fields=[
                ('stream_id', models.AutoField(primary_key=True, serialize=False)),
                ('stream_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_description', models.CharField(max_length=200)),
                ('class_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_class')),
                ('stream_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_stream')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_typesofquestion',
            fields=[
                ('typesofquestion_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_type', models.CharField(max_length=100)),
                ('chapter_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_chapter')),
                ('class_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_class')),
                ('stream_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_stream')),
                ('subject_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_subject')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_exam',
            fields=[
                ('exam_id', models.AutoField(primary_key=True, serialize=False)),
                ('exam_name', models.CharField(max_length=100)),
                ('chapter_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_chapter')),
                ('class_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_class')),
                ('stream_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_stream')),
                ('subject_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_subject')),
                ('typesofquestion_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_typesofquestion')),
            ],
        ),
        migrations.AddField(
            model_name='tbl_class',
            name='stream_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_stream'),
        ),
        migrations.AddField(
            model_name='tbl_chapter',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_class'),
        ),
        migrations.AddField(
            model_name='tbl_chapter',
            name='stream_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_stream'),
        ),
        migrations.AddField(
            model_name='tbl_chapter',
            name='subject_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_subject'),
        ),
    ]