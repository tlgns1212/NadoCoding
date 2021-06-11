# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1 : 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# ...

# 총 탑승 승객 : 2 분
from random import *
taxi_cust = []
for _ in range(50):
    taxi_cust.append(randint(5,51)) 
my_cust = 0
for i in taxi_cust:
    print(i)
    if i < 16:
        my_cust += 1

print(my_cust)