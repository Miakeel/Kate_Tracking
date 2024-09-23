from rest_framework.response import Response
from rest_framework.decorators import api_view
from Tracking.models import Participant, QrCodeId
from .serializers import ParticipantSerializer
from PIL import Image, ImageOps, ImageFont, ImageDraw
import qrcode

from smtplib import SMTP_SSL, SMTP, SMTPAuthenticationError
from ssl import create_default_context
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#Email Sending 

sender = 'info@fmc2024.com'
subject="FMC Workshop Badge"
password="XL@euro24"
description = """
Dear Attendee,
    
You'll find the acces badge attached to this email
    
Best regards,
FMC Team
"""

@api_view(['GET'])
def getData(request):
    participants = Participant.objects.all()
    serializer = ParticipantSerializer(participants, many=True)
    return Response(serializer.data)

# def using_ssl(counter,maximum):
#     try:
#         server = SMTP_SSL(host='mail.fmc2024.com', port=465, context=create_default_context())
#         server.login(sender, password)
#         server.send_message(msg=msg)
#         server.quit()
#         server.close()
#         print(i,"/",maximum)
#     except SMTPAuthenticationError:
#         print('Login Failed SSL')

@api_view(['POST'])
def addParticipant(request):
    qrCode = QrCodeId.objects.create()
    qrCode.is_used = True
    qrCode.save()
    participant_id = qrCode.id

    # Set the participant_id field manually in the serializer
    serializer = ParticipantSerializer(data=request.data, context={'participant_id': participant_id})

    if serializer.is_valid():
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
        title = serializer.validated_data.get('title')
        page_width = 2480
        page_height = 3508
        qr_border = 5
        qr_width = 500 - qr_border
        qr_height = 500 - qr_border
        page = Image.new('RGB', (page_width, page_height), (255, 255, 255))

        fontBold=ImageFont.truetype('Tracking/management/commands/Swansea-q3pd.ttf',size=125)
        fontRegular=ImageFont.truetype('Tracking/management/commands/Swansea-q3pd.ttf',size=100)

        name=first_name+" "+last_name
        
        qr_img = qrcode.make(participant_id)
        qr_img = qr_img.resize((qr_width, qr_height))
        qr_img = ImageOps.expand(qr_img, border=qr_border, fill='black')

        template = Image.open('Tracking/management/commands/template.png')
        template = template.resize((page_width, page_height))
        page.paste(template, (0, 0))
        page.paste(qr_img, (370, 1000))

        draw =ImageDraw.Draw(page)

        draw.text(((page_width/2 - fontBold.getlength(name))/2,550),name,'black',fontBold)

        draw.text(((page_width/2 - fontRegular.getlength(title))/2,750),title,'black',fontRegular)

        page.save('Tracking/static/QR_Codes/%s_%s_%s.png' % (first_name, last_name, participant_id))
        serializer.validated_data['participant_id'] = participant_id

        #Send Badge Email

        message = MIMEMultipart()
        message['Subject']=subject
        message['From']=sender
        message['To']=serializer.validated_data['email']

        body_part=MIMEText(description)
        message.attach(body_part)

        with open('Tracking/static/QR_Codes/%s_%s_%s.png' % (first_name, last_name, participant_id),'rb') as file:
            message.attach(MIMEImage(file.read(), Name="badge.png"))

        with SMTP_SSL(host='mail.fmc2024.com', port=465, context=create_default_context()) as server:
            try:
                server.login(sender,password)
                server.sendmail(sender, serializer.validated_data['email'], message.as_string())
            except SMTPAuthenticationError:
                print("SMTP Authentication Error")


        serializer.save()
    return Response(serializer.data)