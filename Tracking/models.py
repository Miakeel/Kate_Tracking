from django.db import models
import uuid
import datetime

# Create your models here.
class Participant(models.Model):
    # Base Data
    first_name=models.CharField(null=False, max_length=50)
    last_name=models.CharField(null=False, max_length=50)
    institution=models.CharField(null=False, max_length=50)
    email=models.EmailField(null=False, max_length=50)
    title=models.CharField(null=False, max_length=50)
    phone=models.CharField(blank=True)
    city=models.CharField(null=False, max_length=50)
    country=models.CharField(null=False, max_length=50)
    scfhs_number=models.CharField(null=True, max_length=50, blank=True)
    participant_id=models.UUIDField(unique=True,null=True,blank=True)
    inside=models.BooleanField(default=False)
    attended=models.BooleanField(default=False)
    
    # Functional Data
    SPONSOR="SP"
    SPEAKER="SR"
    DELEGATE="DG"
    ATENDEE_CHOICES={
        SPONSOR: "Sponsor",
        SPEAKER: "Speaker",
        DELEGATE: "Delegate"
    }


    participant_type=models.CharField( max_length=2, choices=ATENDEE_CHOICES, default=DELEGATE)


class QrCodeId(models.Model):
    id = models.UUIDField(primary_key=True, blank=True ,unique=True, default=uuid.uuid4)
    is_used = models.BooleanField(default=False)

class Entry(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    exit = models.BooleanField(default=False)