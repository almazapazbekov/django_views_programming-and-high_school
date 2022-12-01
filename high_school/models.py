from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    class_name = models.CharField(max_length=30, choices=(
        ('a', 'a_class'),
        ('b', 'b_class'),
        ('c', 'c_class')

    ), verbose_name='Название класса')

    def __str__(self):
        return self.name


class Pupil(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


