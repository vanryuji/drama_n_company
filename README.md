# Overview
Drama & Company 과제

# Environments
* Python 2.7
* Flask 1.0.3
* SQLAlchemy 1.3.4

# DB 설계
![alt text](db.png)

# API 스펙
### 회원 가입
* /v1/users/create
* POST
* data
  * email(String)
  * passwd(String)
  * driver(String) :'t' or 'f'
* Response
```json
{
	‘users’: {‘email’: ‘xxx@gmail.com’, ‘driver’: ‘t’}
}
```
* Error
```json
# 이메일 중복
{
	‘error’: {
		‘code’: 422,
		‘message’: ‘Duplicate email’,
		‘more_info’: {‘email’: ‘xxx@gmail.com’}
	}
}

```

    
### 
