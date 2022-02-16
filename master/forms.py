from django import forms
from .models import *

class streamform(forms.ModelForm):
    class Meta:
        model=tbl_stream
        fields = "__all__"
class streamupdateform(forms.ModelForm):
    class Meta:
        model = tbl_stream
        fields = ['stream_name']


class classform(forms.ModelForm):
    class Meta:
        model=tbl_class
        fields = "__all__"

class classupdateform(forms.ModelForm):
    class Meta:
        model = tbl_class
        fields = ['class_name','class_description']


class subjectform(forms.ModelForm):
    class Meta:
        model=tbl_subject
        # fields = ['stream_id','class_id','subject_name','subject_description',]
        fields = "__all__"

class subjectupdateform(forms.ModelForm):
    class Meta:
        model = tbl_subject
        fields = ['subject_name','subject_description']


class chapterform(forms.ModelForm):
    class Meta:
        model=tbl_chapter
        fields = "__all__"
class chapterupdateform(forms.ModelForm):
    class Meta:
        model = tbl_chapter
        fields = ['chapter_name','chapter_description']


class typesofquestionform(forms.ModelForm):
    class Meta:
        model=tbl_typesofquestion
        fields = "__all__"
class typesofquestionupdateform(forms.ModelForm):
    class Meta:
        model = tbl_typesofquestion
        fields = ['question_type']


class examform(forms.ModelForm):
    class Meta:
        model=tbl_exam
        fields = "__all__"
class examupdateform(forms.ModelForm):
    class Meta:
        model = tbl_exam
        fields = ['exam_name']
