from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=60)
    def __str__(self):
        return f"{self.course_name}"
class Books(models.Model):
    book_name = models.CharField(max_length=60)
    author_name= models.CharField(max_length=60)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.book_name}"
class Student(models.Model):
    s_name = models.CharField(max_length=50)

    s_phone = models.BigIntegerField()
    s_sem = models.IntegerField()
    s_password = models.CharField(max_length=50)
    s_course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.s_name}"

class Issue_book(models.Model):
    stu_name = models.ForeignKey(Student,on_delete=models.CASCADE)
    bo_name = models.ForeignKey(Books,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
