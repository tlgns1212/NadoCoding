# Quiz) 사이트별로 비밀번호 만들어주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 -> naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성

# 예) 생성된 비밀번호 : nav51!

site_full_name = input()
first_slash = site_full_name.find('/')
first_dot = site_full_name.find('.')
site_name = site_full_name[first_slash + 2 : first_dot]

password = site_name[:3] + str(len(site_name)) + str(site_name.count('e')) + '!'

print(f"{site_full_name}의 비밀번호는 {password}입니다.")