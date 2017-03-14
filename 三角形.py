from turtle import *

def main():
    setup(1300,600,50,50)
    pensize(5)
    pencolor("blue")
    for x in range(0,3):
        fd(150)
        seth(120*(x+1))
main()
