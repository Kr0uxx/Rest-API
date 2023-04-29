from requests import get, post, delete, put

print(get('http://127.0.0.1:8080/api/jobs').json())

print(get('http://127.0.0.1:8080/api/jobs/1').json())

print(get('http://127.0.0.1:8080/api/jobs/111111111').json())

print(get('http://127.0.0.1:8080/api/jobs/id').json())


