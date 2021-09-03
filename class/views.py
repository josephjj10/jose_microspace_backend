from django.shortcuts import render

# Create your views here.
from . models import student
def Create_register(request):
    register = student.objects.create(
        username = "joseph jose",
        age = "18",
        email = "josephjosejj10@gmail.com",
    )

    context = {
        "data":register,
    }

    return render(request,"index.html",context)