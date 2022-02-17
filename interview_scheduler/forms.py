from django import forms
from .models import Student, Interviewer

class DateInput(forms.DateInput):
    input_type = 'date'

class StudentsForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date', 'from_date', 'to_date']
        widgets = {
            'date': DateInput(),
        }
        labels = {
            "from_date": "From",
            "to_date": "To"
        }

class InterviewerForm(forms.ModelForm):

    class Meta:
        model = Interviewer
        fields = ['first_name', 'last_name', 'date', 'from_date', 'to_date']
        widgets = {
            'date': DateInput(),
        }
        labels = {
            "from_date": "From",
            "to_date": "To"
        }