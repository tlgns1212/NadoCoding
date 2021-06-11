lst = ["가", "나", "다"]

for lst_idx, lst_val in enumerate(lst):
    print(lst_idx, lst_val)

balls = [1,2,3,4]
weapons = [11,22,3,44]

for ball_idx, ball_val in enumerate(balls):
    print("ball ", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons : ", weapon_val)
        if ball_val == weapon_val:
            print("공과 무기가 충돌")
            break

a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = a + b
print(c)