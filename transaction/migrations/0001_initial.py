# Generated by Django 4.0a1 on 2022-02-11 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.BigIntegerField()),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=20)),
                ('reenter_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.BigIntegerField()),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=20)),
                ('reenter_password', models.CharField(max_length=20)),
                ('registration_code', models.IntegerField()),
                ('class_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_class')),
                ('stream_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_stream')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_result',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_number', models.IntegerField()),
                ('total_question', models.IntegerField()),
                ('correct_answer', models.IntegerField()),
                ('wrong_answer', models.IntegerField()),
                ('skipped_questions', models.IntegerField()),
                ('out_of_marks', models.IntegerField()),
                ('obtained_marks', models.IntegerField()),
                ('total_marks', models.IntegerField()),
                ('chapter_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_chapter')),
                ('class_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_class')),
                ('stream_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_stream')),
                ('student_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transaction.tbl_student')),
                ('subject_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_subject')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('sr_number', models.IntegerField()),
                ('question', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('correct_answer', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('marks', models.CharField(max_length=10)),
                ('chapter_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_chapter')),
                ('class_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_class')),
                ('stream_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_stream')),
                ('subject_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_subject')),
                ('typesofquestion_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_typesofquestion')),
            ],
        ),
    ]