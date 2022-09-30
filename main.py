#전역 변수
unit = []
select = -1

#추가 함수 (1번 선택 시 호출할 함수)
def add_data(data):
  unit.append(None)
  kLen = len(unit)
  unit[kLen-1] = data

#제거 함수 (2번 선택 시호출할 함수)
def delete_data(position):
  if position <= 0 or position > len(unit):
    print("삭제할 데이터가 존재하지 않습니다.")
    return
    
  del(unit[position-1]) #조건, 리스트의 특정 순서의 값을 삭제해야 하므로 del(unit[특정순서])를 사용
  print(unit)           #ex)  2번 순서의 값을 delete ---> del(unit[2-1])


#튜플 정렬하기 위한 sort_key정의
def sort_value(x):
    return x[1]


#메인 코드 부분 
while(select != 3):
  select = int(input("선택하세요(1: 추가, 2: 삭제, 3: 종료)--> "))

  if(select == 1):
    name = input("유닛 이름을 입력하세요 --> ") 
    hp = int(input("유닛의 체력을 입력하세요 --> "))
    data = (name, hp) #조건, 데이터를 tuple형태로 넣어준다.
    add_data(data)
    unit.sort(key=sort_value, reverse = True) #조건, 숫자가 내림차순 순서대로 정렬을하기 위해서 ,reverse = True라는 구문을 추가해준다
    print(unit)
    
  elif(select == 2):
    delete_index_number = int(input("몇번 자리의 unit를 삭제하시겠습니까?--> "))
    delete_data(delete_index_number)
    
  elif(select == 3):
    exit
    
  else:
    print("1~3 중 하나를 입력하세요.")
    continue