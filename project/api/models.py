from django.db import models

class Students(models.Model):
    student_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100, default='Enter Username', editable=True)
    first_name = models.CharField(max_length=100, default='Enter First Name', editable=True)
    last_name = models.CharField(max_length=100, default='Enter Last Name', editable=True)
    email = models.EmailField(max_length = 254, default='Enter Email', editable=True)


class Teachers(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100, default='Enter Username', editable=True)
    first_name = models.CharField(max_length=100, default='Enter First Name', editable=True)
    last_name = models.CharField(max_length=100, default='Enter Last Name', editable=True)
    email = models.EmailField(max_length = 254, default='Enter Email', editable=True)
    


class Classes(models.Model):
    class_id = models.IntegerField(primary_key=True)
    teacher_id = models.ForeignKey(Teachers , on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=200, default='Class Name', editable=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['class_id', 'teacher_id'], name='Classes_primary_key'
            )
        ]


class Student_Classes(models.Model):
    class_id = models.ForeignKey(Classes , on_delete = models.DO_NOTHING)
    student_id = models.ForeignKey(Students , on_delete = models.DO_NOTHING)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['class_id', 'student_id'], name='Student_Classes_primary_key'
            )
        ]


class Sessions(models.Model):
    session_id = models.IntegerField(primary_key=True)
    class_id = models.ForeignKey(Classes , on_delete = models.DO_NOTHING)
    note = models.FileField()
    voice = models.FileField()
    homework = models.FileField()
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['session_id', 'class_id'], name='Sessions_primary_key'
            )
        ]
