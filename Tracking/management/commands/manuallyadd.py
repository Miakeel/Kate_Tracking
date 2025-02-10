from django.core.management.base import BaseCommand, CommandError
from Tracking.models import Participant, QrCodeId


first_names=["Dr Abdullah", "Dr Waleed", "Dr Marwah", "Dr Sarah", "Dr Azzah", "Dr Amnah", "Dr Mastourah", "Dr Haya", "Dr Asma", "Dr Turki", "Dr Mai", "Dr Huda", "Dr Mutaz", "Dr Ghazi", "Dr Ashwaq", "Dr A", "Dr Bashayar", "Dr Khalid"]
last_names=["Alshabr", "alotaibi", "naqety", "Abutaily", "AlKhayrat", "Bashraheel", "Al-Otaibi", "Alturki", "Alshehri", "alharbi", "Alramih", "Alsoweih", "jabbary", "Alnafiai", "alrawaibah", "Ghamdi", "alrawaibah", "Almalki"]
# institutions=["Center for Innovation & Value Research, Alexandria, VA, USA", "University of Utrecht, Amsterdam, Netherlands", "Georgia Institute of Technology", "University Hospital Llandough", "King Abdulaziz Medical City - Jeddah", "Ministry of Health Affairs", "King Faisal Specialist Hospital & Research Centre", "King Saud University Medical City", "Ministry of Health Affairs", "Ministry of Health Affairs", "Ministry of Health Affairs", "Emirates Health Economisc Association", "King Faisal Specialist Hospital & Research Centre", "Prince Sattam Bin Abdulaziz University", "King Abdulaziz Medical City", "King Fahd Medical City", "King Faisal Specialist Hospital & Research Centre", "King Fahd Medical City", "King Faisal Specialist Hospital & Research Centre", "King Abdullah Specialized Children’s Hospital", "King Faisal Specialist Hospital & Research Centre", "King Fahd Armed Forces Hospital", "Dallah Hospital", "Ministry of Health Affairs", "King Faisal Specialist Hospital & Research Centre", "King Abdullah Bin Abdulaziz University Hospital", "Eurolink Alliance", "Eurolink Alliance", "Eurolink Alliance", "Eurolink Alliance", "Hail Cardiac Center - Hail Health Cluster"]
emails=["Ph.alshabr@hotmail.com", "Awaleed@ksu.edu.sa", "Mnaqety@ksu.edu.sa", "sarahabutaily@hotmail.com", "azzahalkhairat@gmail.com", "Amnah.salem77@gmail.com", "Mastourah432@gmail.com", "haya.alturki1@gmail.com", "asmaalshihri@gmail.com", "lampard882009@windowslive.com", "maialramih@gmail.com", "Halsoweih@gmail.com", "Mfaljabbary@gmail.com", "ghazi.f@hotmail.com", "Aalrwaibaa@psmmc.med.sa", "aaaghamdi7@gmail.com", "Bashayar.alrawaibah@gmail.com", "khaalmalki@outlook.com"]
titles=["Gilead Sciences", "Gilead Sciences", "Gilead/Kite", "Gilead Sciences", "Gilead Sciences", "Kyowa Kirin", "Kyowa Kirin", "Kyowa Kirin", "Kyowa Kirin", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "Roche", "Roche", "Roche", "Roche", "Roche", "Takeda", "Takeda", "Takeda", "Takeda"]
# phones=["17037722453", "447894143931","" ,"" , "503375728","" , "504129758","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ]
# cities=["Alexandria", "Glasgow","" ,"" , "Jeddah", "Riyadh", "Riyadh", "Riyadh", "Riyadh", "Riyadh","" , "Dubai", "Riyadh", "Riyadh","" , "Riyadh", "Riyadh", "Riyadh", "Riyadh", "", "Riyadh", "Riyadh","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ]
# countries=["USA", "UK","" ,"" , "KSA", "KSA", "KSA", "KSA", "KSA", "KSA", "KSA", "UAE", "KSA", "KSA", "", "KSA", "KSA", "KSA", "KSA","" , "KSA", "KSA","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ]
scfhs_numbers=["14RP0035721", "10-R-T-0299718", "06RP44533", "18-RP0017921", "18 GP 0021914", "18GP0015985", "18RP0017679", "19073079", "18AP0001690","" ,"" , "12-R-P-0006357","" , "11RT0042269", "10RP0333694", "10RP0310590", "19145581", "18RP0021498"]



class Command(BaseCommand):
    
    # help = 'Generates a4 size images with unique uuid4 qrcodes'

    # def add_arguments(self, parser):
    #     parser.add_argument('pages', type=int)

    def handle(self, *args, **options):
    
        for i in range (len(first_names)):
            attendee=Participant.objects.create()
            attendee.first_name=first_names[i]
            attendee.last_name=last_names[i]
            # attendee.institution=institutions[i]
            attendee.email=emails[i]
            attendee.title="Delegate"
            # attendee.phone=phones[i]
            # attendee.city=cities[i]
            # attendee.country=countries[i]
            attendee.scfhs_number=scfhs_numbers[i]
            
            qrCode=QrCodeId.objects.create()
            qrCode.is_used=True
            qrCode.save()
            
            attendee.participant_id=qrCode.id
            attendee.save()
        

    