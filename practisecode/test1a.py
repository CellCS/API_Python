

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