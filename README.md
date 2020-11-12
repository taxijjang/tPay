# tPay
tPay 코딩 테스트


### Django runserver 실행 방법 및 접속 URL

1. 가상환경 생성 후 패키지 설치
- > python -m venv venv
- > source venv/scripts/activate
- > pip install -r requirements.txt 

2. django 실행
- > python manage.py runserver

3. 접속 URL (http://127.0.0.0:8000)
- > 상품 GET - /shop/products/, /shop/products/{pk}/
- > 상품 POST - /shop/products/
- > 상품 patch - /shop/products/{pk}/

---
### Docker run (또는 docker-compose up) 실행 방법 및 접속 URL
##### docker-compose file을 작성하여 was를 구성 하였습니다.

1. WAS 구성요소
- > Nginx
- > Gunicorn
- > Django

2. docker-compose 실행 방법
- > docker-compose.yml 파일이 있는 디렉토리로 이동
- > docker-compose up --build

3. 접속 URL (http://127.0.0.0)
- > 상품 GET - /shop/products/, /shop/products/{pk}/
- > 상품 POST - /shop/products/
- > 상품 patch - /shop/products/{pk}/

---
### API 테스트 방법 또는 Postman Export 결과( Postman Export 파일 또는 Postman Url)
##### Postman Export

> - https://documenter.getpostman.com/view/11699885/TVem9oRm 


### git action을 이용하여 CI 구축완료
---
### pytest를 이용하여 API unit-test 완료
