from rest_framework import serializers
from .models import *


class studentserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_student
        fileds='__all__'
class studentupdateserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_student
        fields=['name','email','mobile_number','dob','password','reenter_password','class_id','stream_id','registration_code']




class teacherserializers(serializers.ModelSerializer):
    class Meta:
        model = tbl_teacher
        fileds = '__all__'
class teacherupdateserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_teacher
        fields = ['name', 'email', 'mobile_number', 'dob', 'password', 'reenter_password']



class questionserializers(serializers.ModelSerializer):
    class Meta:
        model = tbl_question
        fileds = '__all__'
class questionupdateserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_question
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_answer','description','marks']


class resultserializers(serializers.ModelSerializer):
    class Meta:
        model = tbl_result
        fileds = '__all__'
class resultupdateserializers(serializers.ModelSerializer):
    class Meta:
        model=tbl_result
        fields = ['question_number', 'total_question', 'correct_answer', 'wrong_answer', 'skipped_questions', 'out_of_marks','obtained_marks','total_marks']

