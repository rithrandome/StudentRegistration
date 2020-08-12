from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import StudentInfoForm, RegisterUserForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import StudentInfo
from django.db.models import Q
from django.contrib import messages


@login_required(login_url='/login/')
def add_StudentInfo(request):

    template = "StudentRegistration/registration.html"

    if request.method == 'POST':
        form = StudentInfoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form is submitted...")
            messages.success(request, 'Student Info is saved successfully !')
            return render(request, 'StudentRegistration/registration.html', {'form': form})
    else:
        form = StudentInfoForm()
    return render(request, template, {'form': form})


def UserLogin(request):

    if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return render(request, 'StudentRegistration/registration.html')
        # else:
        #     return render(request, "StudentRegistration/user_login.html",
        #                   {'error_message': 'Incorrect username and / or password.'})
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('StudentRegistration:add_StudentInfo')
    else:
        form = AuthenticationForm()
    return render(request, "StudentRegistration/user_login.html", {'form': form})

def UserLogout(request):
    logout(request)
    return redirect('StudentRegistration:login_user')

def UserRegister(request):

    template = 'StudentRegistration/user_register.html'

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            else:
                form.save()
                return redirect('/login/')
        #
        #
        # form = RegisterUserForm(request.POST)
        # if form.is_valid():
        #     if User.objects.filter(username=form.cleaned_data['username']).exists():
        #         return render(request, template, {
        #             'form': form,
        #             'error_message': 'Username already exists.'
        #         })
        #     elif User.objects.filter(email=form.cleaned_data['email']).exists():
        #         return render(request, template, {
        #             'form': form,
        #             'error_message': 'Email already exists.'
        #         })
        #     elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
        #         return render(request, template, {
        #             'form': form,
        #             'error_message': 'Passwords do not match.'
        #         })
        #     else:
        #         # Create the user:
        #         user = User.objects.create_user(
        #             form.cleaned_data['username'],
        #             form.cleaned_data['email'],
        #             form.cleaned_data['password']
        #         )
        #
        #         user.save()
        #         return redirect('/login/')
    else:
        form = RegisterUserForm()
    return render(request, template, {'form': form})


@login_required(login_url='/login/')
def search_StudentDetails(request):
    if request.method == 'GET':
        students = StudentInfo.objects.all()
        return render(request, 'StudentRegistration/search_student.html', {'Students': students})
    elif request.method == 'POST':
        search = request.POST['search']

        if search:
            match = StudentInfo.objects.filter(Q(id__istartswith=search) |
                                               Q(Mobile_number__istartswith=search) |
                                               Q(First_name__istartswith=search)
                                               )
            if match:
                return render(request, 'StudentRegistration/search_student.html', {'sr': match})
            else:
                messages.error(request, 'No Result Found')
        else:
            return redirect('/searchStudentDetails/')

    return render(request, "StudentRegistration/search_student.html")

def StudentList(request):
    students = StudentInfo.objects.all()
    return render(request, 'StudentRegistration/search_student.html', {'Students': students})

def delete_StudentDetails(request, pk):
    print('delete something..')
    student = get_object_or_404(StudentInfo, pk=pk)
    student.delete()
    messages.info(request, 'Student info deleted successfully !')
    return redirect('/searchStudentDetails/')

def edit_StudentDetails(request, pk):

    template = 'StudentRegistration/registration.html'
    print('something')
    student = get_object_or_404(StudentInfo, pk=pk)
    if request.method == 'POST':
        form = StudentInfoForm(request.POST, instance=student)
        print(form.is_valid())
        if form.is_valid():
            print(form)
            student = form.save(commit=True)
            student.save()
            messages.success(request, 'Student Info updated successfully !')
            return redirect('/searchStudentDetails/')
    else:
        form = StudentInfoForm(instance=student)

    return render(request, template, {'form': form, 'student': student})




