from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10)
    description = models.TextField()

class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.IntegerField()
    semester = models.IntegerField()
    course_id = models.IntegerField()
