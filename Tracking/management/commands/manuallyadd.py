from django.core.management.base import BaseCommand, CommandError
from Tracking.models import Participant, QrCodeId


first_names=["Abdullah", "Marahlah", "Albert", "Noura", "Ahmed"]
last_names=["Alsuwayyid", "Walid", "edward", "Naous", "abdulwahab"]
institutions=["Novartis", "Novartis", "Novartis", "Novartis", "Novartis"]
emails=["abdullah.alsuwayid@novartis.com", "walid.marahleh@novartis.com", "alber.edward@novartis.com", "noura.naous@novartis.com", "ahmed.abdelwahab@novartis.com"]
titles=["Key Account Manager", "Head of Key Account Management", "Medical Advisor", "Brand Manager", "First Line Manager"]
phones=["551121993", "540717616", "561895817", "537274236", "544755661"]
cities=["Riyadh", "Riyadh", "Riyadh", "Riyadh", "Riyadh"]
countries=["Saudi Arabia", "Saudi Arabia", "Saudi Arabia", "Saudi Arabia", "Saudi Arabia"]
scfhs_numbers=["","","","",""]



class Command(BaseCommand):
    
    # help = 'Generates a4 size images with unique uuid4 qrcodes'

    # def add_arguments(self, parser):
    #     parser.add_argument('pages', type=int)

    def handle(self, *args, **options):
    
        for i in range (len(first_names)):
            attendee=Participant.objects.create()
            attendee.first_name=first_names[i]
            attendee.last_name=last_names[i]
            attendee.institution=institutions[i]
            attendee.email=emails[i]
            attendee.title=titles[i]
            attendee.phone=phones[i]
            attendee.city=cities[i]
            attendee.country=countries[i]
            attendee.scfhs_number=scfhs_numbers[i]
            
            qrCode=QrCodeId.objects.create()
            qrCode.is_used=True
            qrCode.save()
            
            attendee.participant_id=qrCode.id
            attendee.save()
        

    