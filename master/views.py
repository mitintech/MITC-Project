from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import *
from .models import *
from transaction.models import *
from  .customresponse import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .serializers import *

# Create your views here.


#%%%%%%%%%%%%%%%%%%%API VIEWS%%%%%%%%%%%%%%%%%%%%%%#
######################################################STREAM###############################################
@api_view(['Post'])
def apistreaminsert(request):
    serializers=streamserializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Inserted successfully",status.HTTP_200_OK,False))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['Get'])
def apistreamsearch(request):
    stream_search = tbl_stream.objects.all()
    if len(stream_search) !=0:
        serializers=streamserializers(stream_search,many=True)
        return Response(customresponse(serializers.data,status.HTTP_200_OK, False))
    return Response(customresponse("Data not Found ", status=status.HTTP_404_NOT_FOUND))

@api_view(['Post'])
def apistreamupdate(request,id):
    stream_update=tbl_stream.objects.get(id=id)
    serializers=streamupdateserializers(instance=stream_update,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Data updated successfully",status=status.HTTP_200_OK))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['DELETE'])
def apistreamdelete(request,id):
    try:
        stream_delete=tbl_stream.objects.get(id=id)
        x = stream_delete.delete()
        if len(x) !=0:
            print(len(x))
            return Response(customresponse("Data Deleted Successfully", status=status.HTTP_200_OK))
        return Response(customresponse("Data not Found Here", status=status.HTTP_404_NOT_FOUND))

    except Exception as e:
        return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


######################################################class###############################################
@api_view(['Post'])
def apiclassinsert(request):
    serializers=classserializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Inserted successfully",status.HTTP_200_OK,False))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['Get'])
def apiclasssearch(request):
    class_search = tbl_class.objects.all()
    if len(class_search) !=0:
        serializers=classserializers(class_search,many=True)
        return Response(customresponse(serializers.data,status.HTTP_200_OK, False))
    return Response(customresponse("Data not Found ", status=status.HTTP_404_NOT_FOUND))

@api_view(['Post'])
def apiclassupdate(request,id):
    class_update=tbl_class.objects.get(id=id)
    serializers=classupdateserializers(instance=class_update,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Data updated successfully",status=status.HTTP_200_OK))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['DELETE'])
def apiclassdelete(request,id):
    try:
        class_delete=tbl_class.objects.get(id=id)
        x = class_delete.delete()
        if len(x) !=0:
            print(len(x))
            return Response(customresponse("Data Deleted Successfully", status=status.HTTP_200_OK))
        return Response(customresponse("Data not Found Here", status=status.HTTP_404_NOT_FOUND))

    except Exception as e:
        return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


######################################################subject###############################################
@api_view(['Post'])
def apisubjectinsert(request):
    serializers=subjectserializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Inserted successfully",status.HTTP_200_OK,False))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['Get'])
def apisubjectsearch(request):
    subject_search = tbl_subject.objects.all()
    if len(subject_search) !=0:
        serializers=subjectserializers(subject_search,many=True)
        return Response(customresponse(serializers.data,status.HTTP_200_OK, False))
    return Response(customresponse("Data not Found ", status=status.HTTP_404_NOT_FOUND))

@api_view(['Post'])
def apisubjectupdate(request,id):
    subject_update=tbl_subject.objects.get(id=id)
    serializers=subjectupdateserializers(instance=subject_update,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Data updated successfully",status=status.HTTP_200_OK))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['DELETE'])
def apisubjectdelete(request,id):
    try:
        subject_delete=tbl_subject.objects.get(id=id)
        x = subject_delete.delete()
        if len(x) !=0:
            print(len(x))
            return Response(customresponse("Data Deleted Successfully", status=status.HTTP_200_OK))
        return Response(customresponse("Data not Found Here", status=status.HTTP_404_NOT_FOUND))

    except Exception as e:
        return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

######################################################chapter###############################################
@api_view(['Post'])
def apichapterinsert(request):
    serializers=chapterserializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Inserted successfully",status.HTTP_200_OK,False))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['Get'])
def apichaptersearch(request):
    chapter_search = tbl_chapter.objects.all()
    if len(chapter_search) !=0:
        serializers=chapterserializers(chapter_search,many=True)
        return Response(customresponse(serializers.data,status.HTTP_200_OK, False))
    return Response(customresponse("Data not Found ", status=status.HTTP_404_NOT_FOUND))

@api_view(['Post'])
def apichapterupdate(request,id):
    chapter_update=tbl_chapter.objects.get(id=id)
    serializers=chapterupdateserializers(instance=chapter_update,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Data updated successfully",status=status.HTTP_200_OK))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['DELETE'])
def apichapterdelete(request,id):
    try:
        chapter_delete=tbl_chapter.objects.get(id=id)
        x = chapter_delete.delete()
        if len(x) !=0:
            print(len(x))
            return Response(customresponse("Data Deleted Successfully", status=status.HTTP_200_OK))
        return Response(customresponse("Data not Found Here", status=status.HTTP_404_NOT_FOUND))

    except Exception as e:
        return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

######################################################typesofquestion###############################################
@api_view(['Post'])
def apitypesofquestioninsert(request):
    serializers=typesofquestionserializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Inserted successfully",status.HTTP_200_OK,False))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['Get'])
def apitypesofquestionsearch(request):
    typesofquestion_search = tbl_typesofquestion.objects.all()
    if len(typesofquestion_search) !=0:
        serializers=typesofquestionserializers(typesofquestion_search,many=True)
        return Response(customresponse(serializers.data,status.HTTP_200_OK, False))
    return Response(customresponse("Data not Found ", status=status.HTTP_404_NOT_FOUND))

@api_view(['Post'])
def apitypesofquestionupdate(request,id):
    typesofquestion_update=tbl_typesofquestion.objects.get(id=id)
    serializers=typesofquestionupdateserializers(instance=typesofquestion_update,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Data updated successfully",status=status.HTTP_200_OK))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['DELETE'])
def apitypesofquestiondelete(request,id):
    try:
        typesofquestion_delete=tbl_typesofquestion.objects.get(id=id)
        x = typesofquestion_delete.delete()
        if len(x) !=0:
            print(len(x))
            return Response(customresponse("Data Deleted Successfully", status=status.HTTP_200_OK))
        return Response(customresponse("Data not Found Here", status=status.HTTP_404_NOT_FOUND))

    except Exception as e:
        return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

######################################################exam###############################################
@api_view(['Post'])
def apiexaminsert(request):
    serializers=examserializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Inserted successfully",status.HTTP_200_OK,False))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['Get'])
def apiexamsearch(request):
    exam_search = tbl_exam.objects.all()
    if len(exam_search) !=0:
        serializers=examserializers(exam_search,many=True)
        return Response(customresponse(serializers.data,status.HTTP_200_OK, False))
    return Response(customresponse("Data not Found ", status=status.HTTP_404_NOT_FOUND))

@api_view(['Post'])
def apiexamupdate(request,id):
    exam_update=tbl_exam.objects.get(id=id)
    serializers=examupdateserializers(instance=exam_update,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(customresponse("Data updated successfully",status=status.HTTP_200_OK))
    return Response(customresponse("invalid data",status=status.HTTP_400_BAD_REQUEST))

@api_view(['DELETE'])
def apiexamdelete(request,id):
    try:
        exam_delete=tbl_exam.objects.get(id=id)
        x = exam_delete.delete()
        if len(x) !=0:
            print(len(x))
            return Response(customresponse("Data Deleted Successfully", status=status.HTTP_200_OK))
        return Response(customresponse("Data not Found Here", status=status.HTTP_404_NOT_FOUND))

    except Exception as e:
        return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)





#%%%%%%%%%%%%%%%%%%NORMAL VIEWS%%%%%%%%%%%%%%%%%%%%%#
###############################################stream##########################################################
def streaminsert(request):
    if request.method=="POST":
        form= streamform(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/streamsearch/")
        return render(request,"streaminsert.html", {'form': form})
    form =streamform()
    return render(request, "streaminsert.html", {'form': form})

def streamsearch(request):
    stream_search= tbl_stream.objects.all()
    return render(request, "streamsearch.html", {'stream_search': stream_search})

def streamupdate(request,id):
    stream_update=tbl_stream.objects.get(stream_id=id)
    form=streamupdateform(request.POST,instance=stream_update)
    print(form.is_valid())
    print("form")
    if form.is_valid():
        tbl_stream.objects.filter(stream_id=id).update(stream_name=request.POST['stream_name'])
        form.save()
        return HttpResponseRedirect('/streamsearch/')
    return render(request,'streamupdate.html',{'stream_update':stream_update})

def streamdelete(redirect,id):
    stream_delete=tbl_stream.objects.get(stream_id=id)
    stream_delete.delete()
    return HttpResponseRedirect("/streamsearch/")

#################################################class###################################################

def classinsert(request):
    stream_insert=tbl_stream.objects.all()
    if request.method=="POST":
        form= classform(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/classsearch/")
        return render(request,"classinsert.html", {'form': form,'stream_insert':stream_insert})
    form =classform()
    return render(request, "classinsert.html", {'form': form, 'stream_insert':stream_insert})

def classsearch(request):
    class_search= tbl_class.objects.all()
    return render(request,"classsearch.html",{'class_search':class_search})

def classupdate(request,id):
    class_update=tbl_class.objects.get(class_id=id)
    stream=tbl_class.objects.filter(class_id=id)
    form=classupdateform(request.POST,instance=class_update)
    print(form.is_valid())
    print("form")
    if form.is_valid():
        tbl_class.objects.filter(class_id=id).update(class_name=request.POST['class_name'])
        tbl_class.objects.filter(class_id=id).update(class_description=request.POST['class_description'])
        form.save()
        return HttpResponseRedirect("/classsearch/")
    return render(request,'classupdate.html',{'class_update':class_update,'stream':stream})

def classdelete(redirect,id):
    class_delete=tbl_class.objects.get(class_id=id)
    class_delete.delete()
    return HttpResponseRedirect("/classsearch/")

#################################################subject###################################################

def subjectinsert(request):
    class_insert = tbl_class.objects.all()
    stream_insert = tbl_stream.objects.all()
    if request.method=="POST":
        form= subjectform(request.POST)
        print(form.is_valid())
        for i in form:
            print(i,i.errors)
        if form.is_valid():
            print("$$$$$$")
            form.save()
            return HttpResponseRedirect("/subjectsearch/")
        return render(request,"subjectinsert.html", {'form': form,'class_insert':class_insert,'stream_insert':stream_insert})
    form =subjectform()
    return render(request, "subjectinsert.html",{'form': form,'class_insert':class_insert,'stream_insert':stream_insert})


def subjectsearch(request):
    subject_search= tbl_subject.objects.all()
    return render(request,"subjectsearch.html",{'subject_search': subject_search})

def subjectupdate(request,id):
    subject_update=tbl_subject.objects.get(subject_id=id)
    stream = tbl_subject.objects.filter(subject_id=id)
    # cls = tbl_subject.objects.filter(subject_id=id)
    form=subjectupdateform(request.POST,instance=subject_update)
    print(form.is_valid())
    print("form")
    if form.is_valid():
        tbl_subject.objects.filter(subject_id=id).update(subject_name=request.POST['subject_name'])
        tbl_subject.objects.filter(subject_id=id).update(subject_description=request.POST['subject_description'])
        form.save()
        return HttpResponseRedirect("/subjectsearch/")
    return render(request,'subjectupdate.html',{'subject_update':subject_update,'stream':stream})

def subjectdelete(redirect,id):
    subject_delete=tbl_subject.objects.get(subject_id=id)
    subject_delete.delete()
    return HttpResponseRedirect("/subjectsearch/")



#################################################chapter###################################################

def chapterinsert(request):
    stream=tbl_stream.objects.all()
    cls=tbl_class.objects.all()
    subject=tbl_subject.objects.all()

    if request.method=="POST":
        form= chapterform(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/chaptersearch/")
        return render(request,"chapterinsert.html", {'form': form,'stream':stream,'cls':cls,'subject':subject})
    form =chapterform()
    return render(request, "chapterinsert.html", {'form': form,'stream':stream,'cls':cls,'subject':subject})

def chaptersearch(request):
    chapter_search= tbl_chapter.objects.all()
    return render(request,"chaptersearch.html",{'chapter_search': chapter_search})

def chapterupdate(request,id):
    chapter_update=tbl_chapter.objects.get(chapter_id=id)
    stream = tbl_chapter.objects.filter(chapter_id=id)
    form=chapterupdateform(request.POST,instance=chapter_update)
    print(form.is_valid())
    print("form")
    if form.is_valid():
        tbl_chapter.objects.filter(chapter_id=id).update(chapter_name=request.POST['chapter_name'])
        tbl_chapter.objects.filter(chapter_id=id).update(chapter_description=request.POST['chapter_description'])
        form.save()
        return HttpResponseRedirect("/chaptersearch/")
    return render(request,'chapterupdate.html',{'chapter_update':chapter_update,'stream':stream})

def chapterdelete(redirect,id):
    chapter_delete=tbl_chapter.objects.get(chapter_id=id)
    chapter_delete.delete()
    return HttpResponseRedirect("/chaptersearch/")


#################################################typesofquestion###################################################

def typesofquestioninsert(request):
    class_insert = tbl_class.objects.all()
    stream_insert = tbl_stream.objects.all()
    subject_insert = tbl_subject.objects.all()
    chapter_insert = tbl_chapter.objects.all()
    if request.method=="POST":
        form = typesofquestionform(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/typesofquestionsearch/")
        return render(request,"typesofquestioninsert.html", {'form': form,'class_insert':class_insert,'stream_insert':stream_insert,'subject_insert':subject_insert,'chapter_insert':chapter_insert})
    form =typesofquestionform()
    return render(request, "typesofquestioninsert.html", {'form': form,'class_insert':class_insert,'stream_insert':stream_insert,'subject_insert':subject_insert,'chapter_insert':chapter_insert})

def typesofquestionsearch(request):
    typesofquestion_search= tbl_typesofquestion.objects.all()
    return render(request,"typesofquestionsearch.html",{'typesofquestion_search': typesofquestion_search})

def typesofquestionupdate(request,id):
    typesofquestion_update=tbl_typesofquestion.objects.get(typesofquestion_id=id)
    stream=tbl_typesofquestion.objects.filter(typesofquestion_id=id)
    form=typesofquestionupdateform(request.POST,instance=typesofquestion_update)
    print(form.is_valid())
    print("form")
    if form.is_valid():
        tbl_typesofquestion.objects.filter(typesofquestion_id=id).update(question_type=request.POST['question_type'])
        form.save()
        return HttpResponseRedirect("/typesofquestionsearch/")
    return render(request,'typesofquestionupdate.html',{'typesofquestion_update':typesofquestion_update,'stream':stream})

def typesofquestiondelete(redirect,id):
    typesofquestion_delete=tbl_typesofquestion.objects.get(typesofquestion_id=id)
    typesofquestion_delete.delete()
    return HttpResponseRedirect("/typesofquestionsearch/")


#################################################exam###################################################

def examinsert(request):
    class_insert = tbl_class.objects.all()
    stream_insert = tbl_stream.objects.all()
    subject_insert = tbl_subject.objects.all()
    chapter_insert = tbl_chapter.objects.all()
    typesofquestion_insert = tbl_typesofquestion.objects.all()
    if request.method=="POST":
        form = examform(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/examsearch/")
        return render(request,"examinsert.html", {'form': form,'class_insert':class_insert,'stream_insert':stream_insert,'subject_insert':subject_insert,'chapter_insert':chapter_insert,'typesofquestion_insert':typesofquestion_insert})
    form =examform()
    return render(request, "examinsert.html", {'form': form,'class_insert':class_insert,'stream_insert':stream_insert,'subject_insert':subject_insert,'chapter_insert':chapter_insert,'typesofquestion_insert':typesofquestion_insert})

def examsearch(request):
    exam_search= tbl_exam.objects.all()
    return render(request,"examsearch.html",{'exam_search': exam_search})

def examupdate(request,id):
    exam_update=tbl_exam.objects.get(exam_id=id)
    stream=tbl_exam.objects.filter(exam_id=id)
    form=examupdateform(request.POST,instance=exam_update)
    print(form.is_valid())
    print("form")
    if form.is_valid():
        tbl_exam.objects.filter(exam_id=id).update(exam_name=request.POST['exam_name'])
        form.save()
        return HttpResponseRedirect("/examsearch/")
    return render(request,'examupdate.html',{'exam_update':exam_update,'stream':stream})

def examdelete(redirect,id):
    exam_delete=tbl_exam.objects.get(exam_id=id)
    exam_delete.delete()
    return HttpResponseRedirect("/examsearch/")

####################################################################################################################################
def frontpage(request):
    if request.method=="GET":
        sub=tbl_subject.objects.all()
        chapter=tbl_chapter.objects.all()
        que=tbl_question.objects.filter(subject_id=sub,chapter_id=chapter)
        # print(que)
        return render(request,'frontpage.html',{'sub':sub,'chapter':chapter,'que':que})

######################################## aditya  code #######################################################################

def chapterwise(request,subject_id,chapter_id):
        print(subject_id)
        print(chapter_id)
        typesofquestion=tbl_typesofquestion.objects.filter(subject_id=subject_id,chapter_id=chapter_id)
        print(typesofquestion)
        return render(request, 'chapterwise.html',{'question_type':typesofquestion,'subject_id':subject_id})


def chapterwisequestion(request, subject_id, chapter_id,typesofquestion_id):
    typesofquestion = tbl_question.objects.filter(subject_id=subject_id, chapter_id=chapter_id,typesofquestion_id=typesofquestion_id)
    print(typesofquestion)
    return render(request, 'chapterwisequestion.html', {'question_type': typesofquestion})