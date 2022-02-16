from django.db import models
from master.models import *


class tbl_student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.BigIntegerField()
    dob = models.DateField()
    password = models.CharField(max_length=20)
    reenter_password = models.CharField(max_length=20)
    class_id = models.ForeignKey(tbl_class, on_delete=models.CASCADE, null=True, blank=True)
    stream_id = models.ForeignKey(tbl_stream, on_delete=models.CASCADE, null=True, blank=True)
    registration_code = models.IntegerField()
    def __str__(self):
        return self.name


class tbl_teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.BigIntegerField()
    dob = models.DateField()
    password = models.CharField(max_length=20)
    reenter_password = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class tbl_question(models.Model):
    question_id = models.AutoField(primary_key=True)
    sr_number = models.IntegerField()
    stream_id = models.ForeignKey(tbl_stream, on_delete=models.CASCADE, null=True, blank=True)
    class_id = models.ForeignKey(tbl_class, on_delete=models.CASCADE, null=True, blank=True)
    subject_id = models.ForeignKey(tbl_subject, on_delete=models.CASCADE, null=True, blank=True)
    chapter_id = models.ForeignKey(tbl_chapter, on_delete=models.CASCADE, null=True, blank=True)
    typesofquestion_id = models.ForeignKey(tbl_typesofquestion, on_delete=models.CASCADE, null=True, blank=True)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100, null=True, blank=True)
    option2 = models.CharField(max_length=100, null=True, blank=True)
    option3 = models.CharField(max_length=100, null=True, blank=True)
    option4 = models.CharField(max_length=100, null=True, blank=True)
    correct_answer = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    marks = models.CharField(max_length=10)
    def __str__(self):
        return self.question


class tbl_result(models.Model):
    result_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(tbl_student, on_delete=models.CASCADE, null=True, blank=True)
    stream_id = models.ForeignKey(tbl_stream, on_delete=models.CASCADE, null=True, blank=True)
    class_id = models.ForeignKey(tbl_class, on_delete=models.CASCADE, null=True, blank=True)
    subject_id = models.ForeignKey(tbl_subject, on_delete=models.CASCADE, null=True, blank=True)
    chapter_id = models.ForeignKey(tbl_chapter, on_delete=models.CASCADE, null=True, blank=True)
    question_number = models.IntegerField()
    total_question = models.IntegerField()
    correct_answer = models.IntegerField()
    wrong_answer = models.IntegerField()
    skipped_questions = models.IntegerField()
    out_of_marks = models.IntegerField()
    obtained_marks = models.IntegerField()
    total_marks = models.IntegerField()
    def __str__(self):
        return self.question_number

class tbl_practicalquestions(models.Model):
    practicalquestions_id=models.AutoField(primary_key=True)
    sop=models.ForeignKey(tbl_sop, on_delete=models.CASCADE, null=True, blank=True)
    practical_questions=models.CharField(max_length=100)
    showcode=models.FileField(upload_to="showcode")
    output=models.FileField(upload_to="output")
    grp_id = models.ForeignKey(tbl_group, on_delete=models.CASCADE, null=True, blank=True)
    cls_id=models.ForeignKey(tbl_class,on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.practical_questions