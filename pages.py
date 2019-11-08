# Lists every PAGE in a course

from canvasapi import Canvas
from api_key import API_URL, API_KEY

canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(53357) # Cert II
# course = canvas.get_course(63381) # Cert III

pages = course.get_pages()

for page in pages:
    print(page)
