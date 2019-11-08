from canvasapi import Canvas

API_URL = "https://canvas.education.tas.gov.au"
API_KEY = "9371~llK07Wa9SnYxqcluchx0oymdt9F9g1UOATShQ7TFGmUHWWvNGagNuUJsw0yqwORV"
canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(53357) # Cert II
# course = canvas.get_course(63381) # Cert III

pages = course.get_pages()

for page in pages:
    print(page)
