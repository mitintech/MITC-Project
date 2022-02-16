from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import *
from transaction.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('streaminsert/',apistreaminsert),
    path('streamsearch/', apistreamsearch),
    path('streamupdate/<int:id>', apistreamupdate),
    path('streamdelete/<int:id>', apistreamdelete),

    path('classinsert/',apiclassinsert),
    path('classsearch/', apiclasssearch),
    path('classupdate/<int:id>', apiclassupdate),
    path('classdelete/<int:id>', apiclassdelete),

    path('subjectinsert/', apisubjectinsert),
    path('subjectsearch/', apisubjectsearch),
    path('subjectupdate/<int:id>', apisubjectupdate),
    path('subjectdelete/<int:id>', apisubjectdelete),

    path('chapterinsert/', apichapterinsert),
    path('chaptersearch/', apichaptersearch),
    path('chapterupdate/<int:id>', apichapterupdate),
    path('chapterdelete/<int:id>', apichapterdelete),

    path('typesofquestioninsert/', apitypesofquestioninsert),
    path('typesofquestionsearch/', apitypesofquestionsearch),
    path('typesofquestionupdate/<int:id>', apitypesofquestionupdate),
    path('typesofquestiondelete/<int:id>', apitypesofquestiondelete),

    path('examinsert/', apiexaminsert),
    path('examsearch/', apiexamsearch),
    path('examupdate/<int:id>', apiexamupdate),
    path('examdelete/<int:id>', apiexamdelete),


    path('studentinsert/', apistudentinsert),
    path('studentsearch/', apistudentsearch),
    path('studentupdate/<int:id>', apistudentupdate),
    path('studentdelete/<int:id>',apistudentdelete),

    path('teacherinsert/',apiteacherinsert),
    path('teachersearch/',apiteachersearch),
    path('teacherupdate/<int:id>', apiteacherupdate),
    path('teacherdelete/<int:id>',apiteacherdelete),

    path('questioninsert/',apiquestioninsert),
    path('questionsearch/',apiquestionsearch),
    path('questionupdate/<int:id>',apiquestionupdate),
    path('questiondelete/<int:id>',apiquestiondelete),

    path('resultinsert/',apiresultinsert),
    path('resultsearch/', apiresultsearch),
    path('resultupdate/<int:id>', apiresultupdate),
    path('resultdelete/<int:id>',apiresultdelete),


]
