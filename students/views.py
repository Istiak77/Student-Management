from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Student
from .forms import StudentForm


class StudentListView(ListView):
    model = Student
    template_name = 'students/index.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/add.html'

    def form_valid(self, form):
        new_student = form.save()
        return render(self.request, self.template_name, {
            'form': StudentForm(),
            'success': True 
        })


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/edit.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        return render(self.request, self.template_name, {
            'form': form,
            'success': True
        })


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/view_student.html'
    context_object_name = 'student'