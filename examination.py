import tkinter as tk

WIDTH = 800
HEIGHT = 400
BALL_SPEED_X = 3
BALL_SPEED_Y = 3
PADDLE_SPEED = 20
points = 0

root = tk.Tk()
root.title("Pingis")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

ball = canvas.create_oval(WIDTH//2-10, HEIGHT//2-10, WIDTH//2+10, HEIGHT//2+10, fill="white")

paddle = canvas.create_rectangle(WIDTH-30, HEIGHT//2-50, WIDTH-20, HEIGHT//2+50, fill="white")

point_text = canvas.create_text(10, 10, anchor="nw", text=f"Points: {points}", fill="white", font=("Arial", 16))

ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

def move_paddle(event):
    paddle_coords = canvas.coords(paddle)
    if event.keysym == "Up" and paddle_coords[1] > 0:
        canvas.move(paddle, 0, -PADDLE_SPEED)
    elif event.keysym == "Down" and paddle_coords[3] < HEIGHT:
        canvas.move(paddle, 0, PADDLE_SPEED)


def update_ball():
    global ball_dx, ball_dy, points

    canvas.move(ball, ball_dx, ball_dy)
    ball_coords = canvas.coords(ball)

    if ball_coords[1] <= 0 or ball_coords[3] >= HEIGHT:
        ball_dy = -ball_dy

    paddle_coords = canvas.coords(paddle)
    if (ball_coords[2] >= paddle_coords[0] and
    paddle_coords[1] < ball_coords[3] and
    paddle_coords[3] > ball_coords[1]):
        ball_dx = -ball_dx
        points += 1
        ball_dx *= 1.1  
        ball_dy *= 1.1
        
        canvas.itemconfig(point_text, text=f"Points: {points}")
        
        

    if ball_coords[2] >= WIDTH:
        canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="red", font=("Arial", 30))
        return

    canvas.after(20, update_ball)

root.bind("<Up>", move_paddle)
root.bind("<Down>", move_paddle)

update_ball()
root.mainloop()
