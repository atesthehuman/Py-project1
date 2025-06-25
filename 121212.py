import time
import turtle



t = turtle.Turtle()
s = turtle.Screen()
t.shape("turtle")
arka = input("arkaplan rengi ne olsun?")
if arka == "mavi":
    arka = "blue"
if arka == "kırmızı":
    arka = "red"
if arka == "pembe":
    arka = "pink"
if arka == "siyah":
    arka = "black"
if arka == "beyaz":
    arka = "white"
if arka == "turuncu":
    arka = "orange"
if arka == "yeşil":
    arka = "green"
if arka == "mor":
    arka = "purple"


s.bgcolor(arka)
time.sleep(2)
t.speed(10)
t.shape("turtle")
t.left(180)
t.forward(250)
t.right(90)
t.forward(250)
t.pencolor("black")
if arka == "black":
    t.pencolor("red")
t.write("ATEŞ BABA'NIN PROJESİ!!!!!")

t.color(arka)
t.left(180)
t.forward(250)
t.left(90)
t.forward(250)

t.color("white",arka)

while True:
    time.sleep(1)
    x = input("w a s d")
    time.sleep(1)
    if x == "w":
        ert = input("kalınlık ne olsun?")
        sayi = input("kaç birim ilerliceksin?")
        time.sleep(1)
        renk = input("renk ne olsun?")
        time.sleep(1)
        if renk == "kırmızı":
            renk = "red"
        if renk == "mavi":
            renk = "blue"
        if renk ==  "pembe":
            renk = "pink"
        if renk == "siyah":
            renk = "black"
        if renk == "beyaz":
            renk = "white"
        if renk == "turuncu":
            renk = "orange"
        if renk == "yeşil":
            renk = "green"
        if renk == "mor":
            renk = "purple"
        if renk == "arkaplan rengi olsun":
            renk = arka
        t.color( renk,"black")


        sayi = int(sayi)
        t.pensize(ert)
        t.forward(sayi)


    if x == "a":
        time.sleep(1)
        w = input("açınızı girin!")
        w = int(w)
        t.right(w)
    if x == "s":
        time.sleep(1)

        t.left(180)
    if x == "d":
        time.sleep(1)
        r = input("açınızı girin!")
        r = int(r)
        t.left(r)
    if x == "e":
        t.up()
    if x == "g":
        t.down()


turtle.done()