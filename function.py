import random

#랜덤한 숫자 호출
# random = random.randrange(1,100) 

# max_num = random

numbers = [1, 2, 3, 4, 5]

# max_num = max(numbers)

# print(max_num)

r = random.randint(1, 100) #1<=N<=100를 만족하는 임의 정수 N을 반환

# print(r)

##############

menus = ['치킨', '피자', '햄버거']

random_nubmer = random.randint(0, 2)

# print(menus[random_nubmer])

menu = random.choice(menus) #random_choice는 랜덤한 숫자 하나를 선정

# print(menu)


#####

numbers = range(1, 46)
lotto_number = random.sample(numbers, 6) 
#random_sample은 (랜덤변수, k=뽑을 횟수) 선정 
# (중복X)(순서 무작위 ex:뒤에있는 숫자가 앞 숫자보다 작을 수 있음)

# print(sorted(lotto_number)) #sorted 함수 : 오름차순으로 정렬

# url = 앞에는 http와 주소로 되어있고 ?다음으로는 데이터가 들어온다는 것  key와query로 구분 ㄷㅌ:k=q & k=q ...로 되어있음


#HTTP = W3(www)상에서 정보를 주고 받을 수 있는 프로토콜
#^의 핵심 : 사용자가 주소를 서버에 HTTP를 요청하면 그것에 맞는 HTTP를 제공한다.

########################

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086' #대문자는 절대 변하는 않는 데이터(상수)

#pip install requests
import requests

res = requests.get(URL)

# print(res) 
#<Response [200]> == 200은 HTTP의 상태코드 2xx은 (성공) , URL의 정보가 아닌 그 상위 정보
#우리가 흔히 아는 404는 4xx(클라이언트 오류): 요청의 문법이 잘못되거나 or 요청 처리 불가

#data = rex.text <- text 값에 직접 접근
data = res.json() #json은 문자열 자료(str)를 dictionary 자료로 바꿔줌 ex: 10 -> '10' 

drwtNo1 = data['drwtNo1']
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4']
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']

# print(drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6)

lucky_number = (drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6)

#list, dic(자료 구조)에서는 [], 데이터 세부사항에 접근할 때
#(), 소괄호는 함수호출 할때만 즉, ()가 붙는 것은 함수 아닌 것은 값

print(lotto_number)
print(lucky_number)

print(set(lotto_number) & set(lucky_number)) #set()은 두개의 배열 안의 값을 비교해서 같은 값 출력