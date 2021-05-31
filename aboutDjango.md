# About Django

[https://docs.djangoproject.com/ko/3.2/intro/tutorial01/](https://docs.djangoproject.com/ko/3.2/intro/tutorial01/){:target="_blank"}

## The function of the fundamental files

* manage.py: Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티 입니다. manage.py 에 대한 자세한 정보는 django-admin and manage.py 에서 확인할 수 있습니다.
* waterffle/ 디렉토리 내부에는 프로젝트를 위한 실제 Python 패키지들이 저장됩니다. 이 디렉토리 내의 이름을 이용하여, (waterffle.urls 와 같은 식으로) 프로젝트의 어디서나 Python 패키지들을 임포트할 수 있습니다.
* waterffle/__init__.py: Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일입니다. Python 초심자라면, Python 공식 홈페이지의 패키지를 읽어보세요.
* waterffle/settings.py: 현재 Django 프로젝트의 환경 및 구성을 저장합니다. Django settings에서 환경 설정이 어떻게 동작하는지 확인할 수 있습니다.
* waterffle/urls.py: 현재 Django project 의 URL 선언을 저장합니다. Django 로 작성된 사이트의 《목차》 라고 할 수 있습니다. URL dispatcher 에서 URL 에 대한 자세한 내용을 읽어보세요.
* waterffle/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See ASGI를 사용하여 배포하는 방법 for more details.
* waterffle/wsgi.py: 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점입니다. WSGI를 사용하여 배포하는 방법를 읽어보세요.

## Project and Application

장고에서는 웹사이트에 대한 전체 프로그램을 project라고 하고, 모듈화된 단위 프로그램을 application 이라고 합니다. 

## MVT pattern

장고의 MVT 패턴은 웹프로그램 개발 시 언급되는 MVC(Model-View-Controller) 패턴을 동일하게 사용하고 있습니다. 다만 이름에만 차이가 있는데 다음과 같습니다.

* Model == Model : DB에 저장되는 데이터
* View == Template : 사용자에게 보여지는 UI
* Controller == View : 실질적으로 프로그램 로직이 동작하여 데이터를 가져오고 적절하게 처리한 결과를 템플릿에 전달하는 역할

<br><center><img src="https://blog.kakaocdn.net/dn/pdQ3m/btqwhTpC3gU/vXB2IGfXViX7cGFQgXjlR1/img.png"  width="70%"></center><br>


## Model

모델은 사용될 데이터에 대한 정의를 담고 있는 장고의 클래스입니다. 장고는 ORM 기법을 사용하여 애플리케이션에서 사용할 DB를 클래스로 매핑해서 코딩할 수 있습니다.  
--> 하나의 모델 클래스는 하나의 테이블에 매핑되고, 모델 클래스의 속성은 테이블의 컬럼에 매핑됩니다.

* ORM
    - ORM(Object-Relational Mapping)은 객체와 관계형 데이터베이스를 연결해주는 역할을 합니다. DB에 접근하기 위해 SQL을 사용할 필요가 없습니다. 객체를 대상으로 작업을 수행하면 ORM이 적절한 SQL 구문이나 데이터베이스 API를 호출해서 처리해주기 때문입니다. 물론 직접 SQL을 사용하여 데이터를 얻을 수도 있습니다.

데이터베이스 엔진을 변경하더라도 ORM을 통한 API는 변경할 필요가 없어 DB 엔진을 쉽게 변경할 수 있습니다.

테이블 정의는 models.py에 정의합니다.

```python
from django.db import models


class Music(models.Model):
    track_id = models.IntegerField(primary_key=True)
    filename = models.CharField()
    artist_name = models.CharField()
    ...

```

이렇게 정의해주면 Music model은 장고 내부에서 SQL 명령을 사용하여 데이터베이스 테이블을 생성합니다.
primary key는 모델 클래스에서 지정하지 않아도 장고에서 자동으로 부여합니다. 개발자가 직접 지정할 수도 있습니다.

<br>

## URL

클라이언트로부터 요청을 받으면 장고는 가장 먼저 요청에 들어있는 URL이 urls.py 에 정의된 URL 패턴과 매칭되는지 확인합니다.
다음 예제처럼 urls.py에 URL과 처리함수(view)를 매핑하는 파이썬 코드를 작성하면 됩니다. 이러한 URL/view 매핑을 URLconf라고 합니다.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('article/2003/', views.special_case_2003),
    path('article/<int:year>/', views.year_arhive),
    path('article/<int:year>/<int:month>/', views.month_arhive),
    path('article/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
```

웹 클라이언트가 웹서버에 페이지 요청 시, 장고에서 URL을 분석하는 순서를 간단히 요약하면 다음과 같습니다.

1. settings.py의 ROOT_URLCONF 항목을 읽어서 최상위 URLconf의 위치를 알아낸다.
2. URLconf를 로딩하여 urlpatterns 변수에 지정되어 있는 URL list를 검사한다
3. URL list를 위에서부터 순서대로 검사하며 URL pattern이 일치하면 검사를 종료한다.
4. 매치된 URL의 view를 호출한다. 여기서 뷰는 함수 또는 클래스의 메소드이다. 호출시 HttpRequest 객체와 매칭할 떼 추출된 단어들을 뷰에 인자로 넘겨준다.
5. URL list를 끝까지 검사했는데 매칭에 실패하면 에러를 처리하는 뷰를 호출한다.

<br>

URL pattern을 정의할 때 \<int:year\>처럼 꺾쇠를 사용하는 부분은 일부 문자열을 추출하기 위한 것으로, \<tyep:name> 형식으로 사용합니다. 이것을 장고에서는 path converter 라고 부르며, 여기에 사용되는 타입을 다음과 같습니다.

* str : /(slash)를 제외한 모든 문자열과 매치. default
* int : 0 또는 양의 정수와 매치
* slug : slug 형식의 문자열(ASCII, 숫자, 하이픈, 밑줄로만 구성됨)과 매치
* uuid : UUID 형식의 문자열과 매치. 파이썬의 UUID 타입으로 변환됨
* path : /(slash)를 포함한 모든 문자열과 매치. 이는 URL pattern의 일부가 아니라 전체를 추출하고자 할 때 많이 사용함.

url pattern에 정규표현식을 사용하면 URL을 좀 더 세밀하게 표현하거나, 복잡한 URL도 표현할 수 있습니다. 그때는 path 대신에 re_path 를 사용합니다.

자세한 내용은 [다음 링크](https://pilyeooong.tistory.com/entry/Django-path-repath-정규표현식){:target="_blank"}에서 확인바랍니다.

<br>

## View - 로직 정의

뷰는 웹 요청을 받아서 디비 접속 등 해당 애플리케이션의 로직에 맞는 처리를 하고 그 결과 데이터를 HTML로 변환하기 위하여 템플릿 처리를 한 후에, 최종 HTML로 된 응답 데이터를 웹 클라이언트로 반환하는 역할을 합니다.

뷰는 함수 또는 클래스의 메서드로 작성되고 웹 요청에 대한 응답을 반환합니다. 응답은 HTML 데이터일 수도 있고, 리다이렉션 명령일 수 있습니다. 보통 뷰는 views.py에 작성하지만 원한다면 다른 파일에 작성해도 무방합니다. 

간단한 예로 현재의 날짜와 시간을 HTML로 반환해주는 뷰를 작성해보겠습니다.

```python
from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now}.</body></html>"
    return HttpResponse(html)
```

이 경우는 함수 형태로 뷰를 작성한 예시입니다. 뷰 함수는 첫 번째 argument로 HttpRequest 객체(request)를 받습니다. 그리고 필요한 처리를 한 후에 HttpResponse 객체를 반환합니다. 

앞서의 예시에서는 HTML 코드를 뷰 함수 내에서 직접 사용했지만, 보통은 별도의 템플릿 파일에서 HTML 코드를 작성하여 이를 HttpResponse 객체에 담아 클라이언트에게 응답합니다.

<br>

## Template - 화면 UI 정의

장고가 클라이언트에게 반환하는 최종 응답은 HTML 텍스트입니다. *.html 파일을 템플릿이라고 부르며, 장고의 템플릿 시스템 문법에 맞게 작성하면 됩니다. 

장고에서 템플릿 파일을 찾을 때는 TEMPLATES 및 INSTALLED_APPS 에서 지정된 앱의 디렉토리를 검색합니다. 이 항목들은 프로젝트 설정 파일인 **settings.py** 파일에 정의되어 있습니다.

settings.py에 아래와 같이 정의되어 있다면,

```python
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

...

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

...

TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]

```

템플렛을 찾기 위해 검색대상이 되는 디렉토리들은 다음과 같습니다. 기본적으로는 BASE_DIR 내의 templates 디렉토리를 검색하고
그 다음부터는 INSTALLED_APPS에 등록되어 있는 것을 기준으로 그 내부의 templates 디렉토리를 검색하는 순입니다.

```
/Users/username/projects/waterffle/templates
.../Lib/site-packages/django/contrib/admin/templates
.../Lib/site-packages/django/contrib/auth/templates
.../Lib/site-packages/django/contrib/contenttypes/templates
.../Lib/site-packages/django/contrib/sessions/templates
.../Lib/site-packages/django/contrib/messages/templates
.../Lib/site-packages/django/contrib/staticfiles/templates
```

<br>

## MVT 코딩 순서

모델, 뷰, 템플릿 중에서 무엇을 먼저 코딩해야 하는지에 대해 정해진 순서는 없지만 일반적으로 독립적인 개발이 가능한 모델을 먼저 코딩하고, 뷰와 템플릿은 서로 영향을 미치므로 나중에 합니다.

뷰와 템플릿 순서는 UI화면을 고려하면서 로직을 푸는 것이 쉽다면 템플릿을 우선합니다.
클래스형 뷰를 설계할 시에는 뷰의 코딩이 매우 간단해지므로 뷰를 먼저 하기도 합니다.

1. 프로젝트 뼈대 만들기
2. 모델 
3. URLconf
4. 뷰 
5. 템플릿

<br>

waterffle의 경우 화면은 하나만 있습니다.

* playlist.html

## 프로젝트 생성

```
$ django-admin startproject waterffle
```

이렇게 만들면 waterffle 이라는 디렉토리가 2개 생긴다. 가장 상위에 있는 것이 프로젝트 디렉토리이고 그 아래 디렉토리는 프로젝트 관련 파일을 모아둔 역할을 합니다.

## 애플리케이션 생성

```
$ python manage.py startapp playlist
```

## settings.py

1. ALLOWED_HOSTS 에 ip 추가
2. INSTALLED_APPS 에 애플리케이션 설정 클래스 추가
3. DB 설정
4. timezone 지정


