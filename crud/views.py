from django.shortcuts import render, redirect
from .models import Member

# Create your views here.

def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/index.html', context)

def create(request):
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'], dob=request.POST['dob'], age=request.POST['age'], gender=request.POST['gender'], mobilenumber=request.POST['mobilenumber'], address=request.POST['address'], emailid=request.POST['emailid'], password=request.POST['password'], placedetails=request.POST['placedetails'],pincode=request.POST['pincode'])
    member.save()
    return redirect('/')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.dob=request.POST['dob']
    member.age=request.POST['age']
    member.gender=request.POST['gender']
    member.mobilenumber=request.POST['mobilenumber']
    member.address=request.POST['address']
    member.emailid=request.POST['emailid']
    member.password=request.POST['password']
    member.placedetails=request.POST['placedetails']
    member.pincode=request.POST['pincode']
    member.save()
    return redirect('/crud/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')
