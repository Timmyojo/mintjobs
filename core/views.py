from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_not_required
from django.contrib.auth import authenticate, login, logout
from  .models import Job, User
from  .forms import JobForm, CustomUserCreationForm
from django.contrib import messages
from .filters import JobFilter

# Create your views here.

@login_not_required
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        user = authenticate(email=request.POST['email'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            messages.info(request, 'You have successfully logged in.')
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Email or Password.')
            return redirect('login')
    return render(request, 'login.html')

@login_not_required
def register_page(request):
    form = CustomUserCreationForm()
    if request.user.is_authenticated:
        return redirect('home')

    if   request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if  form.is_valid():
            user = form.save(commit=False)
            form.save()
            login(request, user)
            messages.success(request, 'Your account was Successfully created.')
            return redirect('dashboard')
        else:
            messages.error(request, 'An error has occured during registration.')

    context = {'form': form}
    return render(request, 'register.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, 'User was logged out.')
    return redirect('login')

@login_not_required
def home_page(request):
    jobs = Job.objects.filter(featured=True)

    context = {'jobs':jobs}
    return render(request, 'home.html', context)

def dashboard(request):
    user = request.user

    context = {'user':user}
    return render(request, 'dashboard.html', context)

@login_not_required
def job_page(request, pk):
    jobs = Job.objects.get(id=pk)

    context = {'job':jobs}
    return render(request, 'job.html', context)

@login_not_required
def jobs_page(request):
    jobs = Job.objects.all()

    job_count = jobs.count()

    job_filter = JobFilter(request.GET, queryset=jobs)
    jobs = job_filter.qs

    context = {'jobs':jobs, 'jobcount': job_count, 'jobfilter': job_filter}
    return render(request, 'jobs.html', context)



def job_post(request):
    form = JobForm()

    if request.method  == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.poster = request.user
            form.save()

            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'job-post.html', context)

def job_update(request, pk):
    action = 'update'
    job  = Job.objects.get(id=pk)

    if  request.user != job.poster:
        return HttpResponse(' You are not authorised to view this page')
    form = JobForm(instance=job)

    if request.method  == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {'form': form, 'action': action}
    return render(request, 'job-post.html', context)