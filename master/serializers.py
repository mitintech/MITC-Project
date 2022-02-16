from rest_framework import serializers
from .models import *


class streamserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_stream
        fields='__all__'
class streamupdateserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_stream
        fields=['stream_name']


class classserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_class
        fields='__all__'
class classupdateserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_class
        fields=['classname','class_description']


class subjectserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_subject
        fields='__all__'
class subjectupdateserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_subject
        fields=['subject_name','subject_description']


class chapterserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_chapter
        fields='__all__'
class chapterupdateserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_chapter
        fields=['chapter_name','chapter_description']

class typesofquestionserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_typesofquestion
        fields='__all__'
class typesofquestionupdateserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_typesofquestion
        fields=['question_type']

class examserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_exam
        fields='__all__'
class examupdateserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_exam
        fields=['exam_name']