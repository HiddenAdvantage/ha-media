from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
src=Image.open('base5.png').convert('RGB')
bg=src.resize((1440,1920)).crop((180,0,1260,1920)).filter(ImageFilter.GaussianBlur(40))
bg=ImageEnhance.Brightness(bg).enhance(0.5)
canvas=bg.copy(); canvas.paste(src,(0,540))
f=ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf',52)
def frame(lines,name,top=312):
    im=canvas.copy();d=ImageDraw.Draw(im);y=top
    for l in lines:
        w=d.textlength(l,font=f);d.text(((1080-w)/2,y),l,font=f,fill='white');y+=70
    im.save(name)
frame(["Why does your calendar","say sales and your","screen say sports?"],'h1.png')
frame(["It's not a time problem.","It's the one task","you walk around."],'h2.png')
