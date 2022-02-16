from django.db import models

# Create your models here.

class tbl_stream(models.Model):
    stream_id=models.AutoField(primary_key=True)
    stream_name=models.CharField(max_length=100)
    def __str__(self):
        return self.stream_name

class tbl_class(models.Model):
    class_id=models.AutoField(primary_key=True)
    stream_id=models.ForeignKey(tbl_stream,on_delete=models.CASCADE,null=True,blank=True)
    class_name=models.CharField(max_length=100)
    class_description=models.CharField(max_length=200)
    def __str__(self):
        return self.class_name


class tbl_subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    stream_id = models.ForeignKey(tbl_stream,on_delete=models.CASCADE, null=True, blank=True)
    class_id = models.ForeignKey(tbl_class, on_delete=models.CASCADE,null=True, blank=True)
    subject_name = models.CharField(max_length=100)
    subject_description = models.CharField(max_length=200)
    def __str__(self):
        return self.subject_name


class tbl_chapter(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    stream_id = models.ForeignKey(tbl_stream,on_delete=models.CASCADE, null=True, blank=True)
    class_id = models.ForeignKey(tbl_class, on_delete=models.CASCADE,null=True, blank=True)
    subject_id = models.ForeignKey(tbl_subject,on_delete=models.CASCADE, null=True, blank=True)
    chapter_name = models.CharField(max_length=100)
    chapter_description = models.CharField(max_length=200)
    def __str__(self):
        return self.chapter_name

class tbl_typesofquestion(models.Model):
    typesofquestion_id = models.AutoField(primary_key=True)
    stream_id = models.ForeignKey(tbl_stream,on_delete=models.CASCADE, null=True, blank=True)
    class_id = models.ForeignKey(tbl_class, on_delete=models.CASCADE,null=True, blank=True)
    subject_id = models.ForeignKey(tbl_subject,on_delete=models.CASCADE, null=True, blank=True)
    chapter_id = models.ForeignKey(tbl_chapter,on_delete=models.CASCADE, null=True, blank=True)
    question_type = models.CharField(max_length=100)
    def __str__(self):
        return self.question_type

class tbl_exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    stream_id = models.ForeignKey(tbl_stream,on_delete=models.CASCADE, null=True, blank=True)
    class_id = models.ForeignKey(tbl_class, on_delete=models.CASCADE,null=True, blank=True)
    subject_id = models.ForeignKey(tbl_subject,on_delete=models.CASCADE, null=True, blank=True)
    chapter_id = models.ForeignKey(tbl_chapter,on_delete=models.CASCADE, null=True, blank=True)
    typesofquestion_id = models.ForeignKey(tbl_typesofquestion,on_delete=models.CASCADE, null=True, blank=True)
    exam_name = models.CharField(max_length=100)
    def __str__(self):
        return self.exam_name

class tbl_group(models.Model):
    group_id=models.AutoField(primary_key=True)
    group_name=models.CharField(max_length=100)
    def __str__(self):
        return self.group_name

class tbl_sop(models.Model):
    sop_id=models.AutoField(primary_key=True)
    grp_id= models.ForeignKey(tbl_group,on_delete=models.CASCADE, null=True, blank=True)
    sop=models.CharField(max_length=100)
    def __str__(self):
        return self.sop