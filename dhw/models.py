from django.db import models
import uuid

# State Model for db
class State(models.Model):
    state_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    state_name = models.CharField(max_length=100)
    def __str__(self):
        return self.state_name

# District Model for db
class District(models.Model):
    district_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=100)
    def __str__(self):
        return self.district_name


# Child Model for db
class Child(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    child_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    photo = models.ImageField( blank=True, null=True)
    
    def __str__(self):  
        return self.name

