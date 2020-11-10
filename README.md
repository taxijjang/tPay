# tPay
tPay 코딩 테스트


### Django runserver 실행 방법 및 접속 URL
1. 가상환경 생성 후 패키지 설치
- > python -m venv venv
- > source venv/scripts/activate
- > pip install -r requirements.txt 

2. django 실행
- > python manage.py runserver

3. url 접속 (http://127.0.0.0:8000)
- > 상품 GET - /shop/products/, /shop/products/<pk>/
- > 상품 POST - /shop/products/
- > 상품 patch - /shop/products/<pk>/
 
### Docker run (또는 docker-compose up) 실행 방법 및 접속 URL
##### Docker Hub image
- > docker run -d -p 8000:8000 --name dockertpay gw9122/dockertpay:latest

##### Docker Hub docker-compose up
> -


### API 테스트 방법 또는 Postman Export 결과( Postman Export 파일 또는 Postman Url)