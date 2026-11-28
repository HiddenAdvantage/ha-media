from PIL import Image, ImageDraw, ImageFont, ImageFilter
src=Image.open('base2.png').convert('RGB')
bg=src.resize((1440*1920//1440*0+1440,1920)).crop((180,0,1260,1920)).filter(ImageFilter.GaussianBlur(40))
from PIL import ImageEnhance
bg=ImageEnhance.Brightness(bg).enhance(0.55)
canvas=bg.copy(); canvas.paste(src,(0,200))
grad=Image.new('L',(1080,1920),0);gd=ImageDraw.Draw(grad)
for y in range(1100,1920):
    gd.line([(0,y),(1080,y)],fill=int(min(200,(y-1100)*0.5)))
canvas=Image.composite(Image.new('RGB',(1080,1920),(0,0,0)),canvas,grad)
f=ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf',56)
def frame(lines,name,top):
    im=canvas.copy();d=ImageDraw.Draw(im);y=top
    for l in lines:
        w=d.textlength(l,font=f);d.text(((1080-w)/2,y),l,font=f,fill='white');y+=76
    im.save(name)
h=["Why does your calendar","say sales and your","screen say sports?"]
r=["It's not a time problem.","It's the one task","you walk around."]
frame(h,'g1.png',1480)
frame(h+[''] +r,'g2.png',1330)
