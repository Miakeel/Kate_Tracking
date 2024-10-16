from django.core.management.base import BaseCommand, CommandError
from Tracking.models import Participant, QrCodeId


first_names=["Laila", "Hind", "Hussain", "Mansour","Stephanie", "Saleh", "Ahmed", "Malak", "Basem", "Sari", "Ibrahim", "Ramiz", "Ahmed", "Ghadah", "Waleed", "Turki", "Thamer", "Rabab"]
last_names=["Abu Esba", "Al Modeimegh", "Al Omar", "Khan","Chaccour", "Abahussain", "Zoheir", "Alowais", "Osama", "Altaki", "Nabawi", "Alhemaidi", "Alshammari", "Alajmi", "Alghamdi", "Albakr", "Alanazi", "Alhazmi"]
institutions=["Ministry of National Guard Health Affairs", "Ministry of National Guard Health Affairs", "King Saud University", "Ministry of National Guard Health Affairs","AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca"]
emails=["abuesbala@ngha.med.sa", "modaimeghH@mngha.med.sa", "halomar@ksu.edu.sa", "khanma1@ngha.med.sa","stephanie.chaccour@astrazeneca.com","saleh.abahussain@astrazeneca.com","ahmed.zoheir@astrazeneca.com","malak.alowais@astrazeneca.com","basem.abdelaal@astrazeneca.com","sari.altaki1@astrazeneca.com","Ibrahim.Nabawi@astrazeneca.com","ramiz.alhemaidhi@astrazeneca.com","ahmed.alshammari@astrazeneca.com","ghadah.alajmi@astrazeneca.com","waleed.alghamdi@astrazeneca.com","turki.albakr@astrazeneca.com","thamer.alanazi@astrazeneca.com","rabab.alhazmi@astrazeneca.com"]
titles=["Workshop Chair", "Workshop Chair", "Speaker", "Speaker","Market Access & Diagnostic Head", "Market Access Head", "Market Access Head - Oncology", "Market Access Senior Manager", "Market Access Manager", "Market Access Manager", "Market Access Manager", "Market Access Manager", "Market Access Manager", "Health Economics & Payer Evidence Manager", "Market Access Manager", "Market Access Manager", "Market Access Manager", "Market Access Manager"]
phones=["966-55-681-0142", "966-50-319-1586","", "966-53-429-8907","971 505841518", "966 506729716", "971 551235268", "966 545544426", "966 504174253", "971 529988822", "966 569154444", "966 546032772", "966 503208889", "966 557557001", "966 555583433", "966 595934831", "966 562818719", "966 548131698"]
cities=["Riyadh", "Riyadh", "Riyadh", "Riyadh","Dubai", "Riyadh", "Dubai", "Riyadh", "Riyadh", "Dubai", "Riyadh", "Riyadh", "Riyadh", "Riyadh", "Jeddah", "Riyadh", "Riyadh", "Riyadh"]
countries=["KSA", "KSA", "KSA", "KSA","UAE", "KSA", "UAE", "KSA", "KSA", "UAE", "KSA", "KSA", "KSA", "KSA", "KSA", "KSA", "KSA", "KSA"]
scfhs_numbers=["05RP44352", "04RP11997", "08RP0051425", "09JP0284330","","","","","","","","","","","","","",""]



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
        

    