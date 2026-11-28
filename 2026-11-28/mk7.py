from PIL import Image, ImageDraw, ImageFont
src=Image.open('base7.png').convert('RGB')
# soft dark scrim behind the text zone only (no blur, no new background)
ov=Image.new('RGBA',src.size,(0,0,0,0));d=ImageDraw.Draw(ov)
import math
for y in range(150,760):
    t=(y-150)/610
    a=int(165*math.sin(math.pi*t)**1.5)
    d.line([(0,y),(1080,y)],fill=(0,0,0,a))
base=Image.alpha_composite(src.convert('RGBA'),ov).convert('RGB')
f=ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf',52)
def frame(lines,name,top=330):
    im=base.copy();dd=ImageDraw.Draw(im);y=top
    for l in lines:
        w=dd.textlength(l,font=f);dd.text(((1080-w)/2,y),l,font=f,fill='white');y+=70
    im.save(name)
frame(["Why does your calendar","say sales and your","screen say sports?"],'h1.png')
frame(["It's not a time problem.","It's the one task","you walk around."],'h2.png')
