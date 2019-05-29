# Overview
Drama & Company 과제

# Environments
* Python 2.7
* Flask 1.0.3
* SQLAlchemy 1.3.4

# DB 설계
![alt text](db.png)

# API 스펙
### 1) 회원 가입
* /v1/users/create
* POST
* Data
  * email(String)
  * passwd(String)
  * driver(String) :'t' or 'f'
* Response
```json
{
	'users': {'email': 'xxx@gmail.com', 'driver': 't'}
}
```
* Error
```json
# 이메일 중복
{
	'error': {
		'code': 422,
		'message': 'Duplicate email',
		'more_info': {'email': 'xxx@gmail.com'}
	}
}
```

    
### 2) 로그인
* /v1/users/login
* POST
* Data
	* email(String)
	* passwd(String)
* Response
```json
{
	'users': {'email': 'xxx@gmail.com'}
}
```
* Error
```json
# 이메일/비번 잘못 입력
{
	'error': {
		'code': 422,
		'message': 'Wrong email or password',
		'more_info': {'email': 'xxx@gmail.com'}
	}
}
```

### 3) 배차 요청
* /v1/dispatches/request
* POST
* Data
	* email(String) : customer
	* address(String)
* Response
```json
{
	'dispatch': {'email': 'xxx@gmail.com', 'address': 'nowon-gu'}
}
```
* Error
```json
# 올바르지 않는 유저
{
	'error': {
		'code': 422,
		'message': 'Invaild customer',
		'more_info': {}
	}
}
```
