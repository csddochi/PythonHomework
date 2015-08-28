__author__ = 'John'
import turtle as t
import random
wSize = 200

wn = t.Screen()
t0 = t.Turtle()
t1 = t.Turtle()
t2 = t.Turtle()

seurat = t.Turtle()
dot_distance = 20
width = 20
height = 20

seurat.penup()
seurat.setpos(-150, -150)
seurat.speed(10)
for y in range(height + 1):
    for i in range(width + 1):
        seurat.dot()
        seurat.forward(dot_distance)
    seurat.backward(dot_distance * (width + 1))
    seurat.left(90)
    seurat.forward(dot_distance)
    seurat.right(90)
seurat.setpos(0, 0)

t0.penup()
t0.setpos(-150, -150)
t0.pendown()
t0.pensize(5)
for i in range(0, 4):
    t0.forward(wSize * 2)
    t0.left(90)


t1.penup(); t1.setpos(-150, -150); t1.pendown()
t2.penup(); t2.setpos(-150, -150); t2.pendown()
t1.color("red"); t1.pensize(3)
t2.color("blue"); t2.pensize(1.5)
for i in range(0, wSize - 1):
    if (t1.xcor() >= (wSize * 2 - 150)) or (t1.ycor() >= (wSize * 2 - 150)):
        t1.penup(); t1.setpos(-150, -150)
    else:
        t1.setx(-150 + 3 * i)
        t1.sety(-150 + 30 + random.randint(-30+(i*3), 30+(i*3)))

    if (t2.xcor() >= (wSize * 2 - 150)) or (t2.ycor() >= (wSize * 2 - 150)):
        t2.penup(); t2.setpos(-150, -150)
    else:
        t2.setx(-150 + 3 * i)
        t2.sety(-150 + 60 + random.randint(-60+(i*3), 60+(i*3)))

wn.mainloop()

# import threading
# import time
# import random
# import turtle as t
# hw = t.Turtle()
#
# class TestThread(threading.Thread):
#     def run(self):
#         for n in range(0, 60):
#             print('[{0}] Thread {1:03d}'.format(
#                 self.getName(),
#                 random.randrange(1, 999))
#             )
#             time.sleep(1)
#
#
# th = []
# for i in range(3):
#     th.append(TestThread())
#
# for i in th:
#     i.start()
#
# for i in th:
#     i.join()
#
# hw.forward(100)
#
#
#
# if __name__ == "__main__":
#     pass