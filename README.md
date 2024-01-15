# jamshid Referral sms api
api for sent referral codes to users<br>
with authentication of requested user per request<br>
all data has been stored on postgresql running on main server

### Built With
* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
* ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
* ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## Admin

admin panel
* https://offcode.api.jamshid.app/admin

import referral codes with json,csv,xls ...

json example:
```console
[
  {
    "generated_date": "2024-01-13 10:00:00",
    "code": "AMN533"
  },
  {
    "generated_date": "2024-01-14 19:45:00",
    "code": "XYZ555"
  },
  {
    "generated_date": "2024-01-15 21:20:00",
    "code": "ZXX111"
  }
]
```
csv example:
```console
generated_date,code
2024-01-13 10:00:00,UJGMW23D
2024-01-14 19:45:00,O123QQWV
2024-01-15 21:20:00,P123QQWV
```

## Usage

method = POST

### request path
```console
https://offcode.api.jamshid.app/api/sent-referral/
```
### be sure to pass jwt token as "token" in headers
jwt token example:
```console
Bearer <token>
```
### be sure to pass user number as "user" in headers
phone number example:
```console
09121111111
```
  
## Deploy

### 1. install python environment
```console
sudo apt install python3.10-venv
```
### 2. initialize environment
```console
python3 -m venv venv
```
### 3. activate environment
```console
source venv/bin/activate
```
### 4. install requirements
```console
pip3 install -r requirements.txt
```
### 5. make migrations
```console
python3 manage.py makemigrations
```
### 6. migrate
```console
python3 manage.py migrate
```
### 7. create admin user
```console
python2 manage.py createsuperuser
```
### 8. run
```console
python manage.py runserver
```

Developed By Hexoder
