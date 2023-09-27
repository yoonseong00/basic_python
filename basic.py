dust = 10

# print(dust)

dust = '홀리몰리'

dust = True

# print(dust)

dust_list = [20, 0, 10, 0, 100]

# m = sum(dust_list)/len(dust_list)

# print(dust_list[0])

dust_dict = {
    '서울': 100,
    '대전': 10,
    '부산': 50,
}

# print(dust_dict['부산'])

age = 2

#조건

# if age > 20:
#     print('성인입니다.')
# elif age > 8:
#     print('청소년입니다')
# else:
#     print('어린이입니다.')

import random

dust = random.randrange(1, 200)

if dust >= 150:
    print('매우 나쁨, 미세먼지 농도:',dust)
elif dust >= 80:
    print('나쁨, 미세먼지 농도:',dust)
elif dust >= 30:
    print('보통, 미세먼지 농도:',dust)
else:
    print('좋음, 미세먼지 농도:',dust)


#3. 반복
menus = ['햄버거', '치킨', '피자', '짬뽕']

n = 0

while n<4:   #인덱스적인 접근을 할 때 위주로 사용
    print(menus[n])
    n = n + 1

#for item in list(list 안에 있는 데이터를 조각내서 하나의 item으로 분류)

for menu in menus: #대부분 하는 작업들은 for문 사용
    print(menu)  #menus에 있는 메뉴들은 하나씩 모두 출력