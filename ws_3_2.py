from ws_3_1 import increase_user
number_of_people = 0

def create_user(name, age, address):
    user_info = {'name':name, 'age': age, 'address':address}
    print(f'{name}님 환영합니다!')
    print('현재 가입 된 유저 수 :',increase_user())
    return user_info
    
print(create_user(name = '홍길동', age =  30, address = '서울'))
