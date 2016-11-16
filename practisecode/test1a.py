

"""
def fun1(x, y =2, z=8):
    return x+2*y+z**3

print (fun1(3,z=2))


def fun2(x, y=1,z=1, *tup):
    print ((x,y,z) +tup)

fun2(2)
fun2(1,2,3,4,5,6,78,9,99)



def fun13(x, y=1,z=1, **dictionary):
    print ((x,y,z, dict)
           
"""

"""
list1 = ['a',"b", "c",5]

for i in list1:
    if not isinstance(i,int):
        continue
    # not to continue
    print ("this is one inter :" +str(i))
 
"""       


"""
f = open ("myfile.txt", "w")
f.write("helloworld\n")
f.write("that is really word")
f.close()

# pointer at the last place after read()
# so then use line = readline() have no any words
f = open (r"myfile.txt", "r")
lines = f.read()
line1 = f.readline()
line2 = f.readline()
f.close()
print (line1)
print (line2)
print ("really?????")
print (lines)


f = open (r"myfile.txt", "r")

lines = f.read()
f.close()
print("*****************")
print (lines)


f1 = open (r"test1.txt", "r")
x=f1.read()
f1.close()
print (x)


x,y, z, w = 1,2,3,4

print(x,y,z,w)
"""



"""

import urllib

def read_text():
    quotes = open(r"E:\test2.txt")
    content = quotes.read()
    print (content)
    quotes.close()
    check_profanity(content)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output1 = connection.read()
    print (output1)
    connection.close()

read_text()

"""

"""

import urllib

def read_text():
    quotes = open(r"E:\test2.txt")
    content = quotes.read()
    print (content)
    quotes.close()
    check_profanity(content)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output1 = connection.read()
    print (output1)
    connection.close()

read_text()

"""

"""

import turtle

Colors = ["red","purple","blue","green", "orange", "yellow"]
turtle.Pen()
turtle.bgcolor("black")

for x in range(360):
    turtle.pencolor(Colors[x%6])
    turtle.width(x/10+1)
    turtle.forward(x)
    turtle.left(50)
    turtle.speed(100)

"""




"""
# Planing breaking timeimport turtle
import turtle
def draw_circle(some_turtle, r):
    some_turtle.circle(r)
def draw_art():
    window = turtle.Screen()
    window.bgcolor("pink")
    # create turtle brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(5)

    for i in range(0, 36):
        brad.left(50)
        brad.forward(50)
        brad.right(50)
        brad.forward(50)
        brad.right(145)
        brad.forward(50)
        brad.right(50)
        brad.forward(50)
        brad.right(10)
    draw_circle(brad,20)
    brad.forward(100)
    window.exitclick()

draw_art()



"""
"""
# Planing breaking time
import turtle
def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle, r):
    some_turtle.circle(r)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("pink")
    # create turtle brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(5)
    draw_square(brad)

    andy = turtle.Turtle()
    andy.shape("arrow")
    andy.color("blue")
    draw_circle(andy, 100)

    window.exitclick()

def draw_art1():
    window = turtle.Screen()
    window.bgcolor("pink")
    # create turtle brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(5)
    for i in range(1,36):
        draw_square(brad)
        # turn to right 10 degree
        brad.right(10)

draw_art1()

draw_art()





"""

"""
# Planing breaking time
import turtle
def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):
    some_turtle.circle(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("pink")
    # create turtle brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(5)
    draw_square(brad)

    andy = turtle.Turtle()
    andy.shape("arrow")
    andy.color("blue")
    draw_circle(andy)

    window.exitclick()

def draw_art1():
    window = turtle.Screen()
    window.bgcolor("pink")
    # create turtle brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(5)
    for i in range(1,36):
        draw_square(brad)
        # turn to right 10 degree
        brad.right(10)

draw_art1()







"""

"""
import turtle
def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):
    some_turtle.circle(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("pink")
    # create turtle brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(5)
    draw_square(brad)

    andy = turtle.Turtle()
    andy.shape("arrow")
    andy.color("blue")
    draw_circle(andy)

    window.exitclick()

draw_art()

"""

"""
import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor("pink")

    brad = turtle.Turtle()

    brad.shape("turtle")
    brad.color("black")
    brad.speed(5)

    count =0
    while count<4:
        brad.forward(100)
        brad.right(90)
        count+=1

def draw_circle():
    andy = turtle.Turtle()
    andy.shape("arrow")
    andy.color("blue")
    andy.circle(100)

# window.exitonclick()
draw_square()
draw_circle()
"""


'''
import webbrowser
import time


total_breaks = 5
break_count =0

print ('it is a rest time '+ time.ctime())

while (break_count < total_breaks):
    # tis function just 10seconds, so following is 10hrs
    # time.sleep(10*60*60)
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=NjTT5_RSkw4")
    break_count +=1
'''

"""
import os
def rename_files():
    # 1 get the file name from folder
    # 2 rename the file name
    file_list = os.listdir(r'F:\ScriptsDataBase\PythonScripts\Udacity\pythonProgram\testfile')
    print(file_list)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()

"""