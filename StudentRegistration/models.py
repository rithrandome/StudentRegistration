from django.db import models


class StudentInfo(models.Model):
    HOBBIES_CHOICES = (
        ('Drawing', 'Drawing'),
        ('Singing', 'Singing'),
        ('Dancing', 'Dancing'),
        ('Cooking', 'Cooking'),
        ('Others', 'Others')
    )

    COURSE_APPLIED_CHOICES = (('Computer Science Engg', 'Computer Science Engg'), ('Electronics and Communication Engg', 'Electronics and Communication Engg'),
                              ('Mechanical Engg', 'Mechanical Engg'), ('Electrical and Electronics Engg', 'Electrical and Electronics Engg'),
                              ('Instrumentation and Control Engg', 'Instrumentation and Control Engg'), ('Chemical Engg', 'Chemical Engg'),
                              ('Metalurgy Engg', 'Metalurgy Engg'), ('Production Engg', 'Production Engg'), ('Civil Engg', 'Civil Engg'))

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    First_name = models.CharField(max_length=200, default='')
    Last_name = models.CharField(max_length=200, default='')
    Email = models.EmailField(default='')
    Mobile_number = models.CharField(max_length=10, default='')
    id = models.CharField(max_length=9, primary_key=True, default='')
    Gender = models.CharField(max_length=30, choices=GENDER_CHOICES, default='')
    Date_of_birth = models.DateField(blank=True, null=True, default='')
    Address = models.TextField(max_length=500, default='')
    Pin_code = models.CharField(max_length=10, default='')
    City = models.CharField(max_length=50, default='')
    State = models.CharField(max_length=50, default='')
    Country = models.CharField(max_length=50, default='')
    Hobbies = models.TextField(max_length=200, default='')
    Course_applied = models.CharField(max_length=50, choices=COURSE_APPLIED_CHOICES, default='')

    def __str__(self):
        return self.First_name

