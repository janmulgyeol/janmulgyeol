from vpython import *  # 7.6.2
from math import *
 
# 그래픽창을 설정하는 코드
scene.center = vector(0,-1,0)
scene.width = 400
scene.height = 700
 
# 단진자와 이를 받쳐주는 바닥과 봉, 단진자의 실을 생성
ball = sphere(pos=vector(0,0,0), radius=0.15, color=color.white, opacity=0.8)
base = box(pos=vector(0,-2.5,-1), color=color.white, size=vector(2,0.1,2))
wall = box(pos=vector(0,-1,-1), color=color.white, size=vector(0.1,3,0.1))
bar = cylinder(pos=vector(0,0,-1), radius=0.05, axis=vector(0,0,1), color=color.white)
line = curve(pos=bar.pos, color=color.gray(0.5))
line.append(ball.pos)
  
pi = 3.14159  # pi 값
r = 2.        # 실의 길이 m
theta0 = 60   # 초기각도 (deg)
theta = (180 - theta0)*pi / 180  # 초기각도 (rad)
g = 9.81                        # 중력가속도

# 속도를 가시화하기 위한 화살표객체를 생성
velArrow = arrow(pos=ball.pos, axis=vector(0,0,0) , color=color.white)
velFlag = 1
 
omega = 0   # 각속도
alpha = 0   # 각가속도
a = 0       # 가속도
v = 0       # 속도
v_max = sqrt(2*g*r*(-cos(theta)))   # 초기각도에서의 속도의 최대값을 운동에너지 = 위치에너지
 
# 애니메이션 코드
t = 0
dt = 0.01
deg_theta = 0
 
# 텍스트를 위한 라벨 객체를 생성
label1 = label()
label2 = label()
label3 = label()
 
while True:
    rate(100)
    t += dt
 
    # 운동방정식으로 각가속도를 계산하고 이를 적분해 각속도,각도 구함
    alpha = (g*sin(theta))/r
    omega += alpha*dt
    theta += omega*dt
 
    # 각도를 deg단위로 변환
    deg_theta = 180 - theta*180./pi
 
    # x축 방향의 속도를 계산 
    # 실제속도 = 속도의 최대값 - 현재각도에서 속도값(위치에너지에 따른)
    v = v_max - sqrt(2*g*r*(1-cos(pi - theta)))
 
    # 줄의 위치와 공의 위치를 업데이트
    line.modify(0, bar.pos + vector(0,0,1))
    line.modify(1, ball.pos)
    ball.pos = vector(r*sin(theta), r*cos(theta), 0)
 
    # 텍스트 데이터
    label1.pos = base.pos + vector(0,-0.5,0)
    label1.text = 'theta : %.2f deg' % (deg_theta)
    label2.pos = base.pos + vector(0,-0.1,0)
    label2.text = 'time : %.2f s' % (t)
    label3.pos = base.pos + vector(0,-0.9,0)
    label3.text = 'vel_x : %.2f m/s' % (v)

