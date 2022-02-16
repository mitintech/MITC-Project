from .models import *
from .forms import *
from django import forms


class studentfrom(forms.ModelForm):
    class Meta:
        model=tbl_student
        fields=['name','email','mobile_number','dob','password','reenter_password','registration_code','class_id','stream_id']
class studentupdatefrom(forms.ModelForm):
    class Meta:
        model=tbl_student
        fields=['name','email','mobile_number','dob','password','reenter_password','registration_code']






class teacherform(forms.ModelForm):
    class Meta:
        model=tbl_teacher
        fields="__all__"
class teacherupdateform(forms.ModelForm):
    class Meta:
        model=tbl_teacher
        fields=['name','email','mobile_number','dob','password','reenter_password']




class questionform(forms.ModelForm):
    class Meta:
        model = tbl_question
        fields = "__all__"
class questionupdateform(forms.ModelForm):
    class Meta:
        model = tbl_question
        fields =['question','option1','option2','option3','option4','correct_answer','description','marks']



class resultform(forms.ModelForm):
    class Meta:
        model = tbl_result
        fields = "__all__"
class resultupdateform(forms.ModelForm):
    class Meta:
        model = tbl_result
        fields = ['question_number','total_question','correct_answer','wrong_answer','skipped_questions','out_of_marks','obtained_marks','total_marks']



class groupform(forms.ModelForm):
    class Meta:
        model=tbl_group
        fields = "__all__"
class groupupdateform(forms.ModelForm):
    class Meta:
        model = tbl_group
        fields = ['group_name']


class sopform(forms.ModelForm):
    class Meta:
        model=tbl_sop
        fields = ['grp_id','sop']
class sopupdateform(forms.ModelForm):
    class Meta:
        model = tbl_sop
        fields = ['sop']

class practicalquestionsform(forms.ModelForm):
    class Meta:
        model = tbl_practicalquestions
        fields = "__all__"


class practicalquestionsupdateform(forms.ModelForm):
    class Meta:
        model = tbl_practicalquestions
        fields = ['practical_questions','showcode','output','sop']