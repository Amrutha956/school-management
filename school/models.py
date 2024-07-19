from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    


class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Mark(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(validators=[MinValueValidator(1), MaxValueValidator(100)], max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.student.first_name} - {self.subject.name}: {self.marks_obtained}"


