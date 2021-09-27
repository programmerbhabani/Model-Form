from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentModel
from django.contrib import messages
# Insert and Save function.
def showindex(request):
    if request.method == 'POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            # fm.save()
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            res=StudentModel(name=nm,email=em,password=pw).save()
            messages.success(request,'Data Save Successfully')

    else:
        fm = StudentForm()
    fm = StudentForm()# Submit the blank form.
    stu=StudentModel.objects.all()
    return render(request,'addshow.html',{'form':fm,'student_data':stu})
# Delete function.
def deleterecord(request,id):
    if request.method == 'POST':
        recorde=StudentModel.objects.get(pk=id)#id comes from dynamic url
        recorde.delete()
        return redirect('Home')

#Update function.
def updaterecord(request,id):
    if request.method == 'POST':
        recorde=StudentModel.objects.get(pk=id)
        form=StudentForm(request.POST,instance=recorde)
        if form.is_valid():
            form.save()

    else:
        recorde = StudentModel.objects.get(pk=id)
        form = StudentForm(instance=recorde)
    return render(request,'update.html',{'data':form})