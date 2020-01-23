from PIL import Image

from pyautogui import click, typewrite

import time

from automagica import *
from pywinauto import Application

paint = OpenPaint()


im = Image.open('0.png') 

X_total = im.size[0]
Y_total = im.size[1]
XY_total = X_total * Y_total

if X_total > Y_total:
    nova_largura  = 70
    nova_altura = int(nova_largura * (Y_total / X_total))
else:
    nova_altura = 70
    nova_largura  = int(nova_altura * (X_total / Y_total))

im= im.resize((nova_largura, nova_altura), Image.ANTIALIAS)

im = im.convert(mode='P', colors=16)
rgb_im = im.convert('RGB')

X_total = im.size[0]
Y_total = im.size[1]
XY_total = X_total * Y_total

instructions = []

x=1
y=1

while x < X_total-1:
    x = x + 1
    y = 1
    while y < Y_total-1:
        r, g, b = rgb_im.getpixel((x, y))
        instructions.append([4*x+30,4*y+165,r,g,b,3*r+4*g+6*b])
        y = y + 1

instructions.sort(key=lambda x: x[5], reverse=True) #ordenou

print(instructions)
#(121, 636)
def seletor_de_cores(r,g,b):
    click(1103,88) #seleciona paleta de cores
    time.sleep(1)
    typewrite(str(r)) #R
    click(872, 442)
    time.sleep(1)
    typewrite(str(g)) #G
    click(879, 464)
    time.sleep(1)
    typewrite(str(b)) #B
    click(880, 480)
    click(493, 507) #SAIR 'OK'
 
    return

color = 1

#Janela Selecionar pintura
#click(1097, 88)


#Selecione a ferramenta correta
click(308, 67)
time.sleep(1)

#Selecionar linha grossa
click(739, 100)
time.sleep(1)
click(759, 250)

# time.sleep(1)
# click(270,78)
# time.sleep(1)
# click(312,267)


for item in instructions:
    if not (item[2] == 255 and item[3] == 255 and item[4] == 255): #soltar cores brancas
        if not item[5] == color:
            seletor_de_cores(item[2],item[3],item[4])
            color = item[5]
        click(item[0],item[1])