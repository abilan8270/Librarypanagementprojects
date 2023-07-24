# Create your views here.
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache, cache_control

from libraryapp.models import Course, Student, Books, Issue_book


# Create your views here.

def login_fun(request):
    return render(request,'login.html',{'data':''})


def logdata_fun(request):
    Name = request.POST['txtname']
    Password = request.POST['txtpass']
    s_name = request.POST['txtname']
    s_password = request.POST['txtpass']
    user1 = authenticate(username=Name, password=Password)
    if user1 is not None:
        if user1.is_superuser:
            return redirect('ahome')

        else:
            return render(request, 'login.html', {'data': 'not match'})
    elif Student.objects.filter(Q(s_name=s_name) & Q(s_password=s_password)).exists():
        request.session['S_name'] = s_name

        return render(request,'stu_home.html',{'studata': request.session['S_name']})
    else:
        return render(request, 'login.html', {'data': 'check name and password'})


def admin_fun(request):
    return render(request,'admin.html',{'data':''})


def admindata_fun(request):
    Name = request.POST['txtname']
    Email = request.POST['txtemail']
    Password = request.POST['txtpass']

    if User.objects.filter(Q(username=Name) | Q(email=Email)).exists():
        return render(request, 'admin.html', {'data': 'Username Email is alredy exists'})
    else:
        u1 = User.objects.create_superuser(username=Name, email=Email,password=Password)
        u1.save()
        return redirect('log')


def student_fun(request):
    course = Course.objects.all()
    return render(request, 'student.html', {'course_data': course})


def studentdata_fun(request):
    s1 = Student()
    s1.s_name = request.POST['txtname']
    s1.s_phone = request.POST['txtpho']
    s1.s_sem = request.POST['txtsam']
    s1.s_password = request.POST['txtpass']
    s1.s_course = Course.objects.get(course_name = request.POST['ddlcourse'])
    s1.save()
    return redirect('log')

def shome_fun(request):
    return render(request,'stu_home.html')


def adminhome_fun(request):
    return render(request,'admin_home.html')


def addbook_fun(request):
    course = Course.objects.all()
    return render(request,'addbook.html', {'course_data': course})


def addbookdata_fun(request):
    b1 = Books()
    b1.book_name = request.POST['txtbook']
    b1.author_name = request.POST['txtauthor']
    b1.course_id= Course.objects.get(course_name = request.POST['ddlcourse'])
    b1.save()
    return redirect('add')


def display_fun(request):
    b1 = Books.objects.all()
    return render(request,'displaybook.html',{'bdata':b1})


def update_fun(request,id):
    b1 = Books.objects.get(id=id)
    course = Course.objects.all()
    if request.method == 'POST':
        b1.book_name = request.POST['txtbook']
        b1.author_name = request.POST['txtauthor']
        b1.course_id = Course.objects.get(course_name=request.POST['ddlcourse'])
        b1.save()
        return redirect('disp')
    return render(request, 'update.html', {'bdata': b1,'course_data':course})


def del_fun(request,id):
    b1 = Books.objects.get(id=id)
    b1.delete()
    return redirect('disp')


def logout_fun(request):
    logout(request)
    return redirect('log')


def assing_fun(request):
    course = Course.objects.all()
    student = Student.objects.all()
    book = Books.objects.all()
    return render(request,'Assingbook.html',{'course_data':course,'stud_data':student,'book_data':book})


def assingdata_fun(request):
    stud = Student.objects.filter(Q(s_sem=request.POST['txtsam']) & Q (s_course=Course.objects.get(course_name = request.POST['ddlcourse'])))
    book = Books.objects.filter(course_id=Course.objects.get(course_name=request.POST['ddlcourse']))
    return render(request,'Assingbook.html',{'stud_data':stud,'book_data':book})


def issueddisplay_fun(request):
    i1 =Issue_book.objects.all()
    return render(request, 'issuedbook.html', {'bdata': i1})


def stuissue_fun(request):
    a1 = Issue_book.objects.filter(stu_name=Student.objects.get(s_name=request.session['S_name']))
    return render(request, 'studentissuebook.html', {'ddata': a1})


def slogout_fun(request):
    return redirect('log')


def assreadadata_fun(request):
    i1 = Issue_book()
    i1.stu_name=Student.objects.get(s_name=request.POST['textname'])
    i1.bo_name = Books.objects.get(book_name=request.POST['txtbook'])
    i1.start_date=request.POST['txtsdate']
    i1.end_date=request.POST['txtedate']
    i1.save()
    return redirect('ass')


def assingupdate_fun(request,id):
    i1 = Issue_book.objects.get(id=id)
    s1 = Student.objects.get(id=i1.stu_name_id)
    b1 = Books.objects.filter(course_id=s1.s_course)
    if request.method == 'POST':
        i1.stu_name = Student.objects.get(s_name=request.POST['textname'])
        i1.bo_name = Books.objects.get(book_name=request.POST['txtbook'])
        i1.start_date = request.POST['txtsdate']
        i1.end_date = request.POST['txtedate']
        i1.save()
        return redirect('iss')
    return render(request,'update2.html',{'issdata':i1,'bdata':b1})


def assingdelet_fun(request,id):
    i1 = Issue_book.objects.get(id=id)
    i1.delete()
    return redirect('iss')


def studentprofile_fun(request):
    s1 = Student.objects.get(s_name=request.session['S_name'])
    return render(request, 'student_profile.html', {'data': s1})


def updateprof_fun(request,id):
    s1 = Student.objects.get(id=id)
    if request.method == 'POST':
        s1.s_name = request.POST['txtname']
        s1.s_phone = request.POST['txtpho']
        s1.s_sem = request.POST['txtsam']
        s1.s_password = request.POST['txtpass']
        s1.save()
        return redirect('stpro')
    return render(request, 'student_update.html', {'data': s1})