import tkinter as tk

WIDTH = 500
HEIGHT = 400
BALL_SPEED_X = 3
BALL_SPEED_Y = 3
PADDLE_SPEED = 20
points = 0


class Ball:
    ball = canvas.create_oval(WIDTH//2-10, HEIGHT//2-10, WIDTH//2+10, HEIGHT//2+10, fill="white")