# 장고(Django) 시작하기

## 1. Venv 설치 및 환경 켜기
- venv의 경우 Git에 올라가지 않기 때문에 각자의 환경에서 설치해줍니다.
- 설치 방법은 다음과 같습니다.
  - 설치 위치는 프로젝트 폴더의 최상단 위치와 같습니다. 예시는 아래와 같습니다.
  - backend
    |- venv
    |- WEB
    |- SERVER
```bash
$ python -m venv venv
```
- venv 활성화 방법은 다음과 같습니다.
- Bash 및 ZSH 터미널의 경우
```bash
# backend 폴더 내에서
$ Source venv/Scripts/activate
# (venv) 표시가 있는지 확인
```
- CMD 및 POWERSHELL의 경우
```cmd
./venv/Scripts/activate.bat
```

- venv 환경 종료
```bash
$ deactivate
```

## 2. 장고 설치하기
**반드시 venv 환경인지 확인합니다.**

#### A. `requirement.txt`가 없는 경우
```bash
$ pip install django
```

#### B. `requirement.txt`가 있는 경우
```bash
# requirements.txt 내의 모든 라이브러리를 설치
$ pip install -r requirements.txt
```

#### 참고. requirement.txt 생성법
```bash
$ pip freeze > requirements.txt
```

## 3. 장고 프로젝트 만들기 (새로운 프로젝트 생성)
```bash
$ django-admin startproject PROJECT-NAME
```

## 4. 장고 서버 실행
```bash
// 8301 포트 사용을 예시로 사용합니다.
// 포트번호 미 입력시 8080부터 비어있는 포트 번호로 자동 실행됩니다.
$ python manage.py runserver 8301
```

## 5. 장고 앱 추가
#### 5-1. 장고 앱 설치
```bash
$ python manage.py startapp APPNAME
```

- `프로젝트 이름/settings.py'
```python
INSTALLED_APPS = [
		# Project Apps
		'accounts',

		# thirdparty Apps

		# installed Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

#### 5-2. 장고 앱 설정
- 새로 만든 앱 폴더로 이동 후 `templates` 폴더 생성