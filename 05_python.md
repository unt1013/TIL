# Python

> 인생은 짧으니 파이썬을 써라!
>
> 그만큼 쉬운 언어



- 프로그래밍의 3원칙은 저장, 조건, 반복. 이만 지키면 알고리즘 문제들도 해결 할 수 있음
- 저장, 반복, 조건을 알아보자

# Python의 저장 반복 조건

## 1. 저장

### 1.1 문자와 숫자

- 담고자 하는 자료를 변수에 담기만 하면 된다. 문자와 글자의 구분은 ' '로 한다

### 1.2 Bool

- False, True로 표현한다.



## 2. 반복

### 2.1 for

- for 변수 in List : 형식으로 사용한다.

  ```python
  for number in list :
  ```



### 2.2 while

- while 조건 : 형식으로 사용한다.

  ```python
  while boolean :
  ```



## 3. 조건

### 3.1 if

- if 조건 : 형식으로 사용한다. 아래 내용은 들여쓰기로 하며, elif와 else 또한 같은 형식으로 사용

  ```python
  if boolean :
  	something
  elif boolean :
  	something
  else :
  	something
  ```



# Python의 자료구조

> List와 Dictionary를 사용한다.

## List

- list 명 = [변수, 변수 ,변수] 식으로 사용.

  ```python
  array = [1,2,3,"dd","ee"]
  ```

## Dictionary

- dictionary 명 = {'key' : 'value'} 식으로 사용.

  ```python
  Dict = {'key' : 'value', 'key2' : 'value2'}
  ```

  

## Python의 가상환경 설정

- 현재 사용하는 모듈의 리스트를 출력

  ```python
  pip list
  ```

- 자신의 모듈 버전 정보를 requirement.txt에 담아 해당 txt에 적힌 모듈을 다운받아 사용할 수 있도록 한다.

  ```python
  pip freeze > requirement.txt
  pip install -r requirement.txt
  ```

- 가상 환경을 생성하고 활성화시킨다

  ```python
  python -m venv venv
  source venv/Scripts/activate
  ```

  - 앞에 있는 venv 는 Python에서 제공하는 모듈집합의 이름, 뒤에 있는 이름은 모듈 명으로 다른 것으로 설정해도 되지만 혹시 모를 문제를 방지하기 위해 venv로 사용한다

- 종료시에는 deactivate 명령어를 사용한다

  ```python
  deactivate
  ```

- 종료 후 파일 삭제

  ```python
  rm -rf venv
  ```

  