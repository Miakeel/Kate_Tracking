from django.core.management.base import BaseCommand, CommandError
from Tracking.models import Participant, QrCodeId


first_names=["Omer", "Nada", "Wessam", "Amr", "Mohamed", "Ayman", "Kateem", "Samer", "Sameh", "Saleh", "Stephanie", "Ahmed", "Ramiz", "Ibrahim", "Ahmed", "Thamer", "Turki", "Rabab", "Malak", "Basem", "Sari", "Ghada", "Waleed", "Sherif", "Fahad", "Shaima", "abdulrahman", "Abdullah", "Boshra", "Tahani", "Rameen", "Ahmed", "Azzam"]
last_names=["Bawazir", "Alfudhaili", "Mereani", "Antar", "Bakry", "abdeldayem", "alotaibi", "merhi", "morcos", "Abahussain", "Chaccour", "Zoheir", "Alhemaidhi", "Nabawi", "Al Shammary", "Alanzi", "Albakr", "Alhazmi", "Alowais", "Osama", "Altaki", "Alajmi", "Alghamdi", "El Dosoky", "Aljibali", "alsulami", "Owaid", "Alfadeed", "Alyahya", "Alotaibi", "Zarban", "Jaheen", "alghamdi"]
institutions=["Center for Innovation & Value Research, Alexandria, VA, USA", "University of Utrecht, Amsterdam, Netherlands", "Georgia Institute of Technology", "University Hospital Llandough", "King Abdulaziz Medical City - Jeddah", "Ministry of Health Affairs", "King Faisal Specialist Hospital & Research Centre", "King Saud University Medical City", "Ministry of Health Affairs", "Ministry of Health Affairs", "Ministry of Health Affairs", "Emirates Health Economisc Association", "King Faisal Specialist Hospital & Research Centre", "Prince Sattam Bin Abdulaziz University", "King Abdulaziz Medical City", "King Fahd Medical City", "King Faisal Specialist Hospital & Research Centre", "King Fahd Medical City", "King Faisal Specialist Hospital & Research Centre", "King Abdullah Specialized Children’s Hospital", "King Faisal Specialist Hospital & Research Centre", "King Fahd Armed Forces Hospital", "Dallah Hospital", "Ministry of Health Affairs", "King Faisal Specialist Hospital & Research Centre", "King Abdullah Bin Abdulaziz University Hospital", "Eurolink Alliance", "Eurolink Alliance", "Eurolink Alliance", "Eurolink Alliance", "Hail Cardiac Center - Hail Health Cluster"]
emails=["rick.chapman@valueresearch.org", "k.facey@btinternet.com","" ,"" , "metwalihe@nhga.med.sa", "modaimeghH@mngha.med.sa", "sbalhareth@kfshrc.edu.sa", "aalkoraishi@ksu.edu.sa", "abuesbala@ngha.med.sa", "khanma1@ngha.med.sa", "yousefco@mngha.med.sa","" , "ajazairi@kfshrc.edu.sa", "z.almalki@psau.edu.sa", "","" ,"" ,"" , "hsamarkandi61@kfshrc.edu.sa","" , "mahmed@kfshrc.edu.sa", "e.alharby@live.com","" ,"" , "f_maraiki@hotmail.com","" ,"" ,"" ,"" ,"" ,"" ]
titles=["Gilead Sciences", "Gilead Sciences", "Gilead/Kite", "Gilead Sciences", "Gilead Sciences", "Kyowa Kirin", "Kyowa Kirin", "Kyowa Kirin", "Kyowa Kirin", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "AstraZeneca", "Roche", "Roche", "Roche", "Roche", "Roche", "Takeda", "Takeda", "Takeda", "Takeda"]
# phones=["17037722453", "447894143931","" ,"" , "503375728","" , "504129758","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ]
# cities=["Alexandria", "Glasgow","" ,"" , "Jeddah", "Riyadh", "Riyadh", "Riyadh", "Riyadh", "Riyadh","" , "Dubai", "Riyadh", "Riyadh","" , "Riyadh", "Riyadh", "Riyadh", "Riyadh", "", "Riyadh", "Riyadh","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ]
# countries=["USA", "UK","" ,"" , "KSA", "KSA", "KSA", "KSA", "KSA", "KSA", "KSA", "UAE", "KSA", "KSA", "", "KSA", "KSA", "KSA", "KSA","" , "KSA", "KSA","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ]
# scfhs_numbers=["", "","" ,"" , "09JP0281626", "04RP11997", "04RP3446", "10RP0351188", "05RP44352", "09JP0284330", "10RP0343901", "", "02RP3345", "09RP0274281","" ,"" , "04RP3372","" , "14RP0031262","" , "10RP0307561", "09JP0280879","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ]



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
            # attendee.email=emails[i]
            attendee.title=titles[i]
            # attendee.phone=phones[i]
            # attendee.city=cities[i]
            # attendee.country=countries[i]
            # attendee.scfhs_number=scfhs_numbers[i]
            
            qrCode=QrCodeId.objects.create()
            qrCode.is_used=True
            qrCode.save()
            
            attendee.participant_id=qrCode.id
            attendee.save()
        

    