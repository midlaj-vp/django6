from django.shortcuts import render,redirect
from.models import election
from.forms import add_details
# Create your views here.
def election_1(request):
    abc=election.objects.all()
    return render(request,'election.html',{'a':abc})
def add_1(request):
    if request.method=='POST':
        form=add_details(request.POST)
        if form.is_valid():
            form.save()
            return redirect('abc')
    else:
        form=add_details()
        return render(request,'add.html',{'form':form})    