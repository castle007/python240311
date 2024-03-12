import turtle
import time
import random

# 화면 설정
wn = turtle.Screen()
wn.title("블록 깨기 게임")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# 패들 생성
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# 공 생성
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dy = 0  # y 방향 속도 초기화

# 최초 출발 각도를 랜덤으로 설정
# 주석: Set random initial angle for the ball
angle = random.uniform(-60, 60)  # -60도에서 60도 사이의 각도를 랜덤으로 선택
ball.setheading(angle)

# 중력 가속도 설정
gravity = 0.1

# 블록 생성
blocks = []

# 블록 그리기 함수
def create_blocks():
    colors = ["red", "orange", "yellow", "green", "blue"]
    for y in range(100, 250, 50):
        for x in range(-250, 275, 50):
            block = turtle.Turtle()
            block.speed(0)
            block.shape("square")
            block.color(colors[y//50 - 2])
            block.penup()
            block.goto(x, y)
            blocks.append(block)

create_blocks()

# 패들 이동 함수
def move_left():
    x = paddle.xcor()
    x -= 30
    if x < -280:
        x = -280
    paddle.setx(x)

def move_right():
    x = paddle.xcor()
    x += 30
    if x > 230:
        x = 230
    paddle.setx(x)

# 키보드 바인딩
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# 메인 게임 루프
while True:
    wn.update()

    # 공 이동
    ball.sety(ball.ycor() + ball.dy)

    # 중력 적용
    ball.dy -= gravity

    # 벽과 공의 충돌 처리
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # 공과 패들의 충돌 처리
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50):
        ball.sety(-240)
        ball.dy *= -1

    # 튕겨서 올라갈 때 속도 감소 및 증가
    if ball.dy > 0:  # 공이 올라가는 중일 때
        ball.dy = max(ball.dy - gravity * 0.5, 1)  # 최소 속도를 -0.5로 제한
    else:  # 공이 내려가는 중일 때
        ball.dy = min(ball.dy - gravity * 0.3, 20)  # 최대 속도를 10으로 제한

    # 공과 블록의 충돌 처리
    for block in blocks:
        if block.distance(ball) < 20:
            block.goto(1000, 1000)
            ball.dy *= -1
            ball.dy *= 2.5  # 튕겨서 올라갈 때 속도 증가

   # 맨 위로 올라갔을 때 다시 내려오도록 처리
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    time.sleep(0.01)

wn.mainloop()
