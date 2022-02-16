import os

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import *
from .models import *
from  .customresponse import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .serializers import *
from random import sample

############API VIEWS#####################
#####################################################STREAM###############################################
@api_view(['Post'])
def apistudentinsert(request):
    serializers=studentserializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Inserted successfully",status.HTTP_200_OK,False))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['Get'])
def apistudentsearch(request):
    student_search = tbl_student.objects.all()
    if len(student_search) !=0:
        serializers=studentserializers(student_search,many=True)
        return Response(customresponse(serializers.data,status.HTTP_200_OK, False))
    return Response(customresponse("Data not Found ", status=status.HTTP_404_NOT_FOUND))

@api_view(['Post'])
def apistudentupdate(request,id):
    student_update=tbl_student.objects.get(id=id)
    serializers=studentupdateserializers(instance=student_update,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Data updated successfully",status=status.HTTP_200_OK))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['DELETE'])
def apistudentdelete(request,id):
    try:
        student_delete=tbl_student.objects.get(id=id)
        x = student_delete.delete()
        if len(x) !=0:
            print(len(x))
            return Response(customresponse("Data Deleted Successfully", status=status.HTTP_200_OK))
        return Response(customresponse("Data not Found Here", status=status.HTTP_404_NOT_FOUND))

    except Exception as e:
        return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################################################

@api_view(['Post'])
def apiteacherinsert(request):
    serializers=teacherserializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Inserted successfully",status.HTTP_200_OK,False))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['Get'])
def apiteachersearch(request):
    teacher_search = tbl_teacher.objects.all()
    if len(teacher_search) !=0:
        serializers=teacherserializers(teacher_search,many=True)
        return Response(customresponse(serializers.data,status.HTTP_200_OK, False))
    return Response(customresponse("Data not Found ", status=status.HTTP_404_NOT_FOUND))

@api_view(['Post'])
def apiteacherupdate(request,id):
    teacher_update=tbl_teacher.objects.get(id=id)
    serializers=teacherupdateserializers(instance=teacher_update,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Data updated successfully",status=status.HTTP_200_OK))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['DELETE'])
def apiteacherdelete(request,id):
    try:
        teacher_delete=tbl_teacher.objects.get(id=id)
        x = teacher_delete.delete()
        if len(x) !=0:
            print(len(x))
            return Response(customresponse("Data Deleted Successfully", status=status.HTTP_200_OK))
        return Response(customresponse("Data not Found Here", status=status.HTTP_404_NOT_FOUND))

    except Exception as e:
        return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)



############################################################################




@api_view(['Post'])
def apiquestioninsert(request):
    serializers=questionserializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Inserted successfully",status.HTTP_200_OK,False))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['Get'])
def apiquestionsearch(request):
    question_search = tbl_question.objects.all()
    if len(question_search) !=0:
        serializers=questionserializers(question_search,many=True)
        return Response(customresponse(serializers.data,status.HTTP_200_OK, False))
    return Response(customresponse("Data not Found ", status=status.HTTP_404_NOT_FOUND))

@api_view(['Post'])
def apiquestionupdate(request,id):
    question_update=tbl_question.objects.get(id=id)
    serializers=questionupdateserializers(instance=question_update,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Data updated successfully",status=status.HTTP_200_OK))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['DELETE'])
def apiquestiondelete(request,id):
    try:
        question_delete=tbl_question.objects.get(id=id)
        x = question_delete.delete()
        if len(x) !=0:
            print(len(x))
            return Response(customresponse("Data Deleted Successfully", status=status.HTTP_200_OK))
        return Response(customresponse("Data not Found Here", status=status.HTTP_404_NOT_FOUND))

    except Exception as e:
        return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)







@api_view(['Post'])
def apiresultinsert(request):
    serializers=resultserializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Inserted successfully",status.HTTP_200_OK,False))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['Get'])
def apiresultsearch(request):
    result_search = tbl_result.objects.all()
    if len(result_search) !=0:
        serializers=resultserializers(result_search,many=True)
        return Response(customresponse(serializers.data,status.HTTP_200_OK, False))
    return Response(customresponse("Data not Found ", status=status.HTTP_404_NOT_FOUND))

@api_view(['Post'])
def apiresultupdate(request,id):
    result_update=tbl_result.objects.get(id=id)
    serializers=resultupdateserializers(instance=result_update,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Data updated successfully",status=status.HTTP_200_OK))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['DELETE'])
def apiresultdelete(request,id):
    try:
        result_delete=tbl_result.objects.get(id=id)
        x = result_delete.delete()
        if len(x) !=0:
            print(len(x))
            return Response(customresponse("Data Deleted Successfully", status=status.HTTP_200_OK))
        return Response(customresponse("Data not Found Here", status=status.HTTP_404_NOT_FOUND))

    except Exception as e:
        return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)







def studentinsert(request):
    class_insert=tbl_class.objects.all()
    stream_insert=tbl_stream.objects.all()
    form = studentfrom()
    if request.method=="POST":
        form= studentfrom(request.POST)
        print(form)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponseRedirect("/studentsearch/")
        return render(request,"studentinsert.html", {'form': form,'class_insert':class_insert,'stream_insert':stream_insert})
    return render(request, "studentinsert.html", {'form': form,'class_insert':class_insert,'stream_insert':stream_insert})

def studentsearch(request):
    student_search=tbl_student.objects.all()
    return render(request,"studentsearch.html",{'student_search':student_search})


def studentupdate(request,id):
    student_update=tbl_student.objects.get(student_id=id)
    stream=tbl_student.objects.filter(student_id=id)
    form=studentupdatefrom(request.POST,instance=student_update)
    if form.is_valid():
        studentupdatefrom.objects.filter(student_id=id).update(student_update=request.POST['name'])
        studentupdatefrom.objects.filter(student_id=id).update(student_update=request.POST['email'])
        studentupdatefrom.objects.filter(student_id=id).update(student_update=request.POST['mobile_number'])
        studentupdatefrom.objects.filter(student_id=id).update(student_update=request.POST['dob'])
        studentupdatefrom.objects.filter(student_id=id).update(student_update=request.POST['password'])
        studentupdatefrom.objects.filter(student_id=id).update(student_update=request.POST['reenter_password'])
        studentupdatefrom.objects.filter(student_id=id).update(student_update=request.POST['registration_code'])
        form.save()
        return HttpResponseRedirect("/studentsearch/")
    return render(request,'studentupdate.html',{'student_update':student_update,'stream':stream})

def studentdelete(request,id):
    student_delete=tbl_student.objects.filter(student_id=id)
    student_delete.delete()
    return HttpResponseRedirect("/studentsearch/")
#####################################3

def teacherinsert(request):
    form = teacherform()
    if request.method=="POST":
        form= teacherform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/teachersearch/")
        return render(request,"teacherinsert.html", {'form': form})

    return render(request, "teacherinsert.html", {'form': form})

def teachersearch(request):
    teacher_search=tbl_teacher.objects.all()
    return render(request,"teachersearch.html",{'teacher_search':teacher_search})


def teacherupdate(request,id):
    teacher_update=tbl_teacher.objects.get(teacher_id=id)
    form=teacherupdateform(request.POST,instance=teacher_update)
    if form.is_valid():
        teacherupdateform.objects.filter(teacher_id=id).update(teacher_update=request.POST['name'])
        teacherupdateform.objects.filter(teacher_id=id).update(teacher_update=request.POST['email'])
        teacherupdateform.objects.filter(teacher_id=id).update(teacher_update=request.POST['mobile_number'])
        teacherupdateform.objects.filter(teacher_id=id).update(teacher_update=request.POST['dob'])
        teacherupdateform.objects.filter(teacher_id=id).update(teacher_update=request.POST['password'])
        teacherupdateform.objects.filter(teacher_id=id).update(teacher_update=request.POST['reenter_password'])
        form.save()
        return HttpResponseRedirect("/teachersearch/")
    return render(request,'teacherupdate.html',{'teacher_update':teacher_update})

def teacherdelete(request,id):
    teacher_delete=tbl_teacher.objects.filter(teacher_id=id)
    teacher_delete.delete()
    return HttpResponseRedirect("/teachersearch/")

##################################

def questioninsert(request):
    class_insert = tbl_class.objects.all()
    stream_insert = tbl_stream.objects.all()
    subject_insert = tbl_subject.objects.all()
    chapter_insert = tbl_chapter.objects.all()
    typesofquestion_insert = tbl_typesofquestion.objects.all()
    form = questionform()
    if request.method=="POST":
        form= questionform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/questionsearch/")
        return render(request,"questioninsert.html", {'form': form ,'class_insert':class_insert,'stream_insert':stream_insert,'subject_insert':subject_insert,'chapter_insert':chapter_insert,'typesofquestion_insert':typesofquestion_insert})

    return render(request, "questioninsert.html", {'form': form,'class_insert':class_insert,'stream_insert':stream_insert,'subject_insert':subject_insert,'chapter_insert':chapter_insert,'typesofquestion_insert':typesofquestion_insert})

def questionsearch(request):
    question_search=tbl_question.objects.all()
    return render(request,"questionsearch.html",{'question_search':question_search})


def questionupdate(request,id):
    question_update=tbl_question.objects.get(question_id=id)
    stream=tbl_question.objects.filter(question_id=id)
    form=questionupdateform(request.POST,instance=question_update)
    if form.is_valid():
        tbl_question.objects.filter(question_id=id).update(question_update=request.POST['question'])
        tbl_question.objects.filter(question_id=id).update(question_update=request.POST['option1'])
        tbl_question.objects.filter(question_id=id).update(question_update=request.POST['option2'])
        tbl_question.objects.filter(question_id=id).update(question_update=request.POST['option3'])
        tbl_question.objects.filter(question_id=id).update(question_update=request.POST['option4'])
        tbl_question.objects.filter(question_id=id).update(question_update=request.POST['correct_answer'])
        tbl_question.objects.filter(question_id=id).update(question_update=request.POST['description'])
        tbl_question.objects.filter(question_id=id).update(question_update=request.POST['marks'])
        form.save()
        return HttpResponseRedirect("/questionsearch/")
    return render(request,'questionupdate.html',{'question_update':question_update,'stream':stream})

def questiondelete(request,id):
    question_delete=tbl_student.objects.filter(question_id=id)
    question_delete.delete()
    return redirect("/questionview/")

##############################################

def resultinsert(request):
    form = resultform()
    if request.method=="POST":
        form= resultform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data inserted")
        return render(request,"resultinsert.html", {'form': form})

    return render(request, "resultinsert.html", {'form': form})

def resultsearch(request):
    result_search=tbl_result.objects.all()
    return render(request,"resultsearch.html",{'result_search':result_search})


def resultupdate(request,id):
    result_update=tbl_result.objects.get(result_id=id)
    form=resultupdateform(request.POST,instance=result_update)
    if form.is_valid():
        tbl_result.objects.filter(result_id=id).update(result_update=request.POST['question_number'])
        tbl_result.objects.filter(result_id=id).update(result_update=request.POST['total_question'])
        tbl_result.objects.filter(result_id=id).update(result_update=request.POST['correct_answer'])
        tbl_result.objects.filter(result_id=id).update(result_update=request.POST['wrong_answer'])
        tbl_result.objects.filter(result_id=id).update(result_update=request.POST['skipped_questions'])
        tbl_result.objects.filter(result_id=id).update(result_update=request.POST['out_of_marks'])
        tbl_result.objects.filter(result_id=id).update(result_update=request.POST['obtained_marks'])
        tbl_result.objects.filter(result_id=id).update(result_update=request.POST['total_marks'])
        form.save()
        return HttpResponse('Updated Successfully')
    return render(request,'resultupdate.html',{'result_update':result_update})

def resultdelete(request,id):
    result_delete=tbl_result.objects.filter(result_id=id)
    result_delete.delete()
    return redirect("/resultview/")








def groupinsert(request):
    if request.method=="POST":
        form= groupform(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/groupview/")
        return render(request,"groupinsert.html", {'form': form})
    form =groupform()
    return render(request, "groupinsert.html", {'form': form})

def groupview(request):
    group_view= tbl_group.objects.all()
    return render(request, "groupview.html", {'group_view': group_view})

def groupupdate(request,id):
    print("dsds")
    group_update=tbl_group.objects.get(group_id=id)
    form=groupupdateform(request.POST,instance=group_update)
    if form.is_valid():
        tbl_group.objects.filter(group_id=id).update(group_name=request.POST['group_name'])
        form.save()
        return HttpResponseRedirect("/groupview/")
    return render(request,'groupupdate.html',{'group_update':group_update})

def groupdelete(request,id):
    group_delete=tbl_group.objects.get(group_id=id)
    group_delete.delete()
    print("eee")
    return HttpResponseRedirect("/groupview/")




def sopinsert(request):
    group_insert=tbl_group.objects.all()
    print("#########3333333")
    if request.method=="POST":
        print("rrr")
        form= sopform(request.POST)
        print("rrr")
        print(form.is_valid())
        if form.is_valid():
            print("rrr")
            form.save()
            return HttpResponseRedirect("/sopview/")
        return render(request,"sopinsert.html", {'form': form,'group_insert':group_insert})
    form =sopform()
    return render(request,"sopinsert.html", {'form': form,'group_insert':group_insert})

def sopview(request):
    practicaltables_view= tbl_sop.objects.all()
    return render(request, "sopview.html", {'practicaltables_view': practicaltables_view})

def sopupdate(request,id):
    practicaltables_update=tbl_sop.objects.get(sop_id=id)
    group_insert=tbl_sop.objects.filter(sop_id=id)
    form=sopupdateform(request.POST,instance=practicaltables_update)
    print(form.is_valid())
    print("form")
    if form.is_valid():
        tbl_sop.objects.filter(sop_id=id).update(sop=request.POST['sop'])
        form.save()
        return HttpResponseRedirect("/sopview/")
    return render(request,'sopupdate.html',{'practicaltables_update':practicaltables_update,'group_insert':group_insert})

def sopdelete(redirect,id):
    practicaltables_delete=tbl_sop.objects.get(sop_id=id)
    practicaltables_delete.delete()
    return HttpResponseRedirect("/sopview/")



def practicalquestionsinsert(request):
    group_insert = tbl_group.objects.all()
    class_insert=tbl_class.objects.all()
    sop_insert=tbl_sop.objects.all()
    if request.method=="POST":
        form= practicalquestionsform(request.POST, request.FILES)
        for i in form:
            print(i,i.errors)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/practicalquestionsview/")
        return render(request,"practicalquestionsinsert.html", {'form': form,'group_insert':group_insert,'class_insert':class_insert,'sop_insert':sop_insert})
    form =practicalquestionsform()
    return render(request, "practicalquestionsinsert.html", {'form': form,'group_insert':group_insert,'class_insert':class_insert,'sop_insert':sop_insert})

def practicalquestionsview(request):
    practicalquestions_view= tbl_practicalquestions.objects.all()
    return render(request, "practicalquestionsview.html", {'practicalquestions_view':practicalquestions_view})

def practicalquestionsupdate(request,id):
    group_insert = tbl_group.objects.all()
    class_insert = tbl_class.objects.all()
    practicalquestions_update=tbl_practicalquestions.objects.get(practicalquestions_id=id)
    if request.method == "POST":
        form=practicalquestionsform(request.POST,instance=practicalquestions_update)
        print(form.is_valid())
        print("form")
        if form.is_valid():
            tbl_practicalquestions.objects.filter(practicalquestions_id=id).update(practical_questions=request.POST['practical_questions'])
            tbl_practicalquestions.objects.filter(practicalquestions_id=id).update(sop=request.POST['sop'])
            path = "media/showcode"
            path1="media/output"

            print(practicalquestions_update.showcode.path)
            if len(request.FILES) != 0:

                    if len(practicalquestions_update.showcode) > 0:
                            print(practicalquestions_update.showcode.path)

                            os.remove(practicalquestions_update.showcode.path)
                            practicalquestions_update.showcode = request.FILES['showcode']

                    practicalquestions_update.save()
                    if len(request.FILES) != 0:

                        if len(practicalquestions_update.output) > 0:
                            print(practicalquestions_update.output.path)

                            os.remove(practicalquestions_update.output.path)
                            practicalquestions_update.output = request.FILES['output']

                        practicalquestions_update.save()
                    form.save()
        return HttpResponseRedirect("/practicalquestionsview/")
    return render(request,'practicalquestionsupdate.html',{'practicalquestions_update':practicalquestions_update,'group_insert':group_insert,'class_insert':class_insert})

def practicalquestionsdelete(redirect,id):
    practicalquestions_delete=tbl_practicalquestions.objects.get(practicalquestions_id=id)
    practicalquestions_delete.delete()
    return HttpResponseRedirect("/practicalquestionsview/")




# Create your views here.
def index(request):
    return render(request, 'home.html')


def fnebook(request):
    subjectall = tbl_subject.objects.all()
    chapterall = tbl_chapter.objects.all()
    questionall = tbl_typesofquestion.objects.all()
    subject=request.GET.get('subject_id')
    chapter=request.GET.get('chapter_id')
    question=request.GET.get('typesofquestion_id')

    # num_entities = tbl_question.objects.all().count()
    # rand_entities = sample((1, num_entities), 2)
    sample_entities = tbl_question.objects.filter(subject_id=subject,chapter_id=chapter,typesofquestion_id=question)
    print(sample_entities)

    return render(request,'ebook.html',{'subjectall':subjectall,'chapterall':chapterall,'questionall':questionall,'subject':subject,'chapter':chapter,'question':questionall, 'pool':sample_entities})

def load_courses(request):
    subject_id = request.GET.get('subject')
    question = tbl_question.objects.all()
    chapter = tbl_chapter.objects.filter(subject_id=subject_id).order_by('chapter_name')
    return render(request, 'courses_dropdown_list_options.html', {'subject': subject_id, 'chapter': chapter, 'question': question})




def questionpaper(request):
    num_entities = tbl_question.objects.all().count()
    rand_entities = sample((1, num_entities), 2)
    sample_entities = tbl_question.objects.filter(question_id__in=rand_entities).values()
    print(sample_entities)

    # pdf = render_to_pdf('questionpaper.html',{'pool':sample_entities})
    return render(request, "questionpaper.html", {'pool':sample_entities})


def gcfilterview(request):
    grp_id = request.GET.get('grp_id')
    cls_id = request.GET.get('cls_id')
    group= tbl_group.objects.all()
    cls= tbl_class.objects.all()

    # prac=tbl_practicalquestions.objects.filter(grp_id=group,cls_id=cls).values_list('sop')
    prac = tbl_practicalquestions.objects.filter(grp_id=grp_id, cls_id=cls_id)

    print(prac)

    return render(request, "slectgrp.html", {'group':group,'cls':cls,'prac':prac})


def practical(request):
    print("qqq")
    grp_id = request.GET.get('grp_id')
    cls_id = request.GET.get('cls_id')
    # prac1 = tblpracticalquestions.objects.filter(prac1=grp_id)
    prac = tbl_practicalquestions.objects.filter( grp_id=grp_id,cls_id=cls_id)
    print(prac)

    return render(request, "practical.html", {'prac':prac})