import requests

TEACHER_URL = "http://localhost:5000/api/teacher"  # Create URLS for API resources
STUDENT_URL = "http://localhost:5000/api/student/"

response = requests.get(TEACHER_URL)   # Make the HTTP request to the app
if response.status_code == requests.codes.OK:  # Check that the HTTP status code is 200 (OK)
    print(response.text)  # Get the returned JSON as a binary string (bytes object) and decode to Python string
print('=' * 60)

for i in range(10):
    url = f"{STUDENT_URL}{i}"  # Construct URL with unique IDs
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        print(response.text)
    print('-' * 60)
