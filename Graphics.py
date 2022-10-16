
import turtle as t
def main():
    t.color("red")
    t.bgcolor("pink")
    for i in range(10):
        t.circle(i+25)
    t.goto(0,20)
    for j in range(10):
        t.circle(j+25)
    t.goto(0,40)
    for j in range(10):
        t.circle(j+25)
    t.hideturtle()
    t.goto(120,120)
    t.write("Hello users! Spread love",90,align="center",font = ('Monotype',20,"bold"))

if __name__ == '__main__':
    main()
