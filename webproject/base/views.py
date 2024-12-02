from django.shortcuts import render 
from django.views.generic import ListView , UpdateView , DeleteView
from base.models import Course
from django.urls import reverse_lazy

# Create your views here.
class course_view(ListView):
    template_name = 'course.html'
    model = Course
    context_object_name = 'course'

def course_idseacrh(request):
    search = request.GET.get('id','')
    course = Course.objects.filter(cid__icontains=search)
    return render(request,'course_ids.html',{'course':course})

def course_nameseacrh(request):
    search = request.GET.get('name',None)
    course = Course.objects.filter(name=search)
    return render(request,'course_name.html',{'course':course})

class course_update(UpdateView):
    model = Course
    fields = ['cid','name','teacher']
    context_object_name = 'form'
    template_name = 'edit.html'
    success_url = reverse_lazy('FunctionB')

class course_delete(DeleteView):
    model = Course
    template_name = 'delete.html'
    context_object_name = 'course'
    success_url = reverse_lazy('FunctionA')