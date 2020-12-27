from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Schedule
from .forms import ScheduleForm
from datetime import datetime
from django.contrib import messages


def index(request):
    if request.POST:
        data = ScheduleForm(request.POST)  #ata form er obj create korchi seii obj taka akta dic ka store kora rakta hoi
        if data.is_valid():
            data.save()
            messages.success(request, 'Schedule added !')
            return redirect('Home')
        else:
            messages.warning(request, 'Something went wrong !')
            return redirect('Home')

    # -------------------------------------------------------------------------
    context = {
        'schedules': Schedule.objects.all(),  # list of objects ... [obj1, obj2]
        'form': ScheduleForm(),#aiii khana form ta store kora cha 
        'date': datetime.today()
    }
    return render(request, 'index.html', context)


def update(request, pk):
    obj = Schedule.objects.get(id=pk)#list of obj using ids

    if request.POST:
        data = ScheduleForm(request.POST, instance=obj)
        if data.is_valid():
            data.save()
            messages.success(request, 'Schedule updated !')
            return redirect('Home')
        else:
            messages.warning(request, 'Something went wrong !')
            return redirect('Home')

    context = {
        'schedules': Schedule.objects.all(),  # list of objects ... [obj1, obj2]
        'form': ScheduleForm(instance=obj),
        'date': datetime.today()
     }

    return render(request, 'index.html', context)


def delete(request, pk):
    obj = Schedule.objects.get(id=pk)
    if request.POST:
        obj.delete()
        messages.success(request, 'Schedule has been removed !')
        return redirect('Home')

    return render(request, 'delete_confirm.html', {'object': obj})
