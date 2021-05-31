# waterffle
new shuffle style : waterffle! It is the shuffle that naturally moves on to the next song like water.

## Introduction of Frame directories and the files

* manage.py : 장고의 명령어를 처리하는 파일

* waterffle : project 이름으로 만들어진 디렉토리이며 프로젝트 관련 파일들이 들어있음
* waterffle/settings.py : 프로젝트 설정 파일
* waterffle/urls.py : 프로젝트 레벨의 URL pattern을 정의하는 최상위 URLconf 파일이며 애플리케이션마다 따로 urls.py을 가지고 있음.
* waterffle/wsgi.py : Apache와 같은 웹서버와 WSGI 규격으로 연동하기 위한 파일

* playlist : 애플리케이션 디렉토리. 
* playlist/admin.py : admin site에 모델 클래스를 등록해주는 파일
* playlist/apps.py : 애플리케이션 설정 클래스를 정의하는 파일
* playlist/templates : html 파일 디렉토리
* playlist/static : CSS, Image, Javascript 파일 보관

* migrations : 데이터베이스 변경사항을 관리하기 위한 디렉토리.
* migrations/models.py : 데이터베이스 모델 클래스를 정의하는 파일
* migrations/tests.py : 단위 테스트용
* migrations/views.py : 뷰 함수 혹은 클래스를 정의하는 파일

* logs : 로그 파일 디렉토리. settings.py에서 LOGGING 항목으로 위치 지정


## DB 설정

* DB : PostgreSQL
    - version : 13.3

### How to install postgresql

* mac 이라면  
```
$brew install postgresql==13.3
```
* ubuntu 라면
    - 참조 사이트 : [https://phoenixnap.com/kb/how-to-install-postgresql-on-ubuntu](https://phoenixnap.com/kb/how-to-install-postgresql-on-ubuntu)

* 버전 확인  
```
$psql -V
```

### How to use postgresql

* postgresql 서버 가동  
```
$postgres -D /usr/local/var/postgres
```

* Database 생성
```
$createdb waterffle
```

* User 생성
```
$createuser ok
```

* 생성한 DB 접속
```
$psql waterffle
```

* 모든 database 정보 확인
```
waterffle=# \l
```

* waterffle db의 소유권 ok에게 넘겨주기
```
waterffle=# alter database waterffle owner to ok;
```

* user 권한 주기
```
waterffle=# grant all on database waterffle to ok with grant option;
```

### Django와 연동

1. postgresql의 정보를 settings.py에 명시
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'waterffle',
        'USER': 'ok',
        'PASSWORD': 'okay',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

2. models.py 작성

3. migration(db 켜놓은 상태에서)
```
$python manage.py migrate
```

4. 확인
```
waterffle=# \dt

                  List of relations
 Schema |            Name            | Type  | Owner
--------+----------------------------+-------+-------
 public | auth_group                 | table | ok
 public | auth_group_permissions     | table | ok
 public | auth_permission            | table | ok
 public | auth_user                  | table | ok
 public | auth_user_groups           | table | ok
 public | auth_user_user_permissions | table | ok
 public | django_admin_log           | table | ok
 public | django_content_type        | table | ok
 public | django_migrations          | table | ok
 public | django_session             | table | ok
(10 rows)

```

