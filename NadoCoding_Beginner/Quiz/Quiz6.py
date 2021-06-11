# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#   * 함수명 : std_weight
#   * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    weight = 0
    if gender == "men":
        weight = height * height * 22
    elif gender == "women":
        weight = height * height * 21
    return weight

gender = "men"
height = 1.75
weight = std_weight(height, gender)
print(f"키 {int(height*100)}cm 남자의 표준 체중은 {weight:.2f} 입니다.")    