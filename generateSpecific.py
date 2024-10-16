from PIL import Image, ImageOps, ImageFont, ImageDraw
import qrcode

first_name="Faris"
last_name="Al-Rifar"
participant_id="d9ad980d-1e6f-4f89-ba83-29a425766b4e"
title="Pharmacist"

page_width = 2480
page_height = 3508

qr_border = 5
qr_width = 500 - qr_border
qr_height = 500 - qr_border

page = Image.new('RGB', (page_width, page_height), (255, 255, 255))

fontBold=ImageFont.truetype('Tracking/management/commands/Swansea-q3pd.ttf',size=125)
fontRegular=ImageFont.truetype('Tracking/management/commands/Swansea-q3pd.ttf',size=100)

qr_img=qrcode.make(participant_id)
qr_img = qr_img.resize((qr_width, qr_height))
qr_img = ImageOps.expand(qr_img, border=qr_border, fill='black')

template = Image.open('Tracking/management/commands/template.png')
template = template.resize((page_width, page_height))
page.paste(template,(0,0))
name=first_name+" "+last_name
            
page.paste(qr_img,(370,1000))

draw = ImageDraw.Draw(page)

draw.text(((page_width/2 - fontBold.getlength(name))/2,550),name,'black',fontBold)

draw.text(((page_width/2 - fontRegular.getlength(title))/2,750),title,'black',fontRegular)


            
page.save('Tracking/static/QR_Codes/%s_%s_%s.png' % (first_name, last_name,participant_id))