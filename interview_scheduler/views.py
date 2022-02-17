from django.shortcuts import render
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from .models import Student, Interviewer
from .forms import StudentsForm, InterviewerForm
from django.views.generic import CreateView, ListView
# Create your views here.


# Contains 3 buttons to navigate to various pages.
def homepage(request):
    return render(request, "homepage.html")


# Class based views to add student information and availabilty to models
class StudentAdd(CreateView):
    model = Student
    template_name = 'student_form.html'
    form_class = StudentsForm


    def form_valid(self, form):
        student = Student()
        student.first_name = form.cleaned_data['first_name']
        student.last_name = form.cleaned_data['last_name']
        student.date = form.cleaned_data['date']
        student.from_date = form.cleaned_data['from_date']
        student.to_date = form.cleaned_data['to_date']
        student.save()

        return redirect('student')


# Class based views to add interviewer information and availabilty to models.
class InterviewerAdd(CreateView):
    model = Interviewer
    template_name = 'interviewer_form.html'
    form_class = InterviewerForm


    def form_valid(self, form):
        interviewer = Interviewer()
        interviewer.first_name = form.cleaned_data['first_name']
        interviewer.last_name = form.cleaned_data['last_name']
        interviewer.date = form.cleaned_data['date']
        interviewer.from_date = form.cleaned_data['from_date']
        interviewer.to_date = form.cleaned_data['to_date']
        interviewer.save()

        return redirect('interviewer')


# Class based view to list the timings available for student and interviewer to conduct the interview.
class ScheduleView(ListView):
    template_name ='scheduleview.html'
    context_object_name = 'schedule'
    model = Interviewer

    def get_context_data(self, **kwargs):
        context = super(ScheduleView, self).get_context_data(**kwargs)
        interviewer = Interviewer.objects.all()
        student =  Student.objects.all()
        context.update({'interviewer' : interviewer})
        context.update({'student':student})
        return context

    def get_queryset(self):
        result = super(ScheduleView, self).get_queryset()
        s = self.request.GET.get('s')
        i = self.request.GET.get('i')
        a = []
        c = []
        result = ''
        time_dict = {'13':'1', '14':'2', '15':'3', '16':'4', '17':'5', '18':'6', '19' : '7'}
        if s and i:
            i_ob = Interviewer.objects.filter(id = i).values('from_date', 'to_date', 'date')
            s_ob = Student.objects.filter(id = s).values('from_date', 'to_date', 'date')

            for k in i_ob:
                student_from_date = k['from_date']
                student_to_date = k['to_date']
                student_date = k['date']
            for j in s_ob:
                interviewer_from_date = j['from_date']
                interviewer_to_date = j['to_date']
                interviewer_date = j['date']
                
            for i in range(int(student_from_date), int(student_to_date)):
                k = i+1
                if str(i) in time_dict.keys():
                    i = time_dict[str(i)]
                if str(k) in time_dict.keys():
                    k = time_dict[str(k)]
                    print("k", k)
                a.append((int(i), int(k)))
            
            for i in range(int(interviewer_from_date), int(interviewer_to_date)):
                k = i+1
                print(time_dict.keys())
                if str(i) in time_dict.keys():
                    i = time_dict[str(i)]
                if str(k) in time_dict.keys():
                    k = time_dict[str(k)]
                    print("k", k)
                c.append((int(i), int(k)))
    
            if str(interviewer_date) == str(student_date):
                result = [sub_list for sub_list in a if sub_list in c]
            else: 
                result = 'The timings of both student and interviewer does not match'
        return result
