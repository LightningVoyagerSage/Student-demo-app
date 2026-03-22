from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)


class Attendance(models.Model):

    SUBJECT_CHOICE = (
        ("Hindi", "Hindi"),
        ("Science", "Science"),
        ("Maths", "Maths")

    )

    STATUS_CHOICE = (
        ("Present", "Present"),
        ("Absent", "Absent")
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=15, choices=SUBJECT_CHOICE)
    data = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)