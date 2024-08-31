from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import  Job, User

class JobForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['poster', 'featured']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Job Title'
        self.fields['jobtype'].label = 'Job Type'
        self.fields['level'].label = 'Job Level'
        self.fields['workplace'].label = 'Workplace Type'
        self.fields['description'].label = 'Job Description'
        self.fields['perks'].label = 'Job Perks'
        self.fields['link'].label = 'Application link or Email'
        self.fields['company'].label = 'Company Name'
        self.fields['hearaboutus'].label = 'How did  you hear about us'

class CustomUserCreationForm(UserCreationForm):
    usable_password = None
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password1', 'password2']