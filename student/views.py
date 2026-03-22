from django.shortcuts import render ,redirect
from .models import Student, Attendance

def student_home(request):
    
    students_data = Student.objects.all()
    attendance = Attendance.objects.all()
   # student_data = student.object.filter()

    data = {
        "students_data": students_data,
        "attendance": attendance
    }
    
    return render(request, "student/student_home.html", data)

def add_student(request): 

  if request.method == "POST":
    student_name = request.POST.get("input_name")
    student_email = request.POST.get("input_email")
    student_phone_number = request.POST.get("input_phone")

    Student.objects.create(
       name = student_name,
       email = student_email,
       phone_number = student_phone_number
    )
    
    return redirect("student_home")

  return render(request, "student/add_student.html")

def delete_student(request, student_id):
   
   my_student = Student.objects.get(id = student_id)

   my_student.delete()

   return redirect("student_home")

def update_student(request, student_id):
    
    student = Student.objects.get(id = student_id)
    if request.method == "POST":        
      student.name = request.POST.get("input_name")
      student.email = request.POST.get("input_email")
      student.phone_number = request.POST.get("input_phone")
      student.save()
      return redirect("student_home")

    parameters = {
       "student": student
    }
    
    return render( request,"student/update_student.html", parameters)


   