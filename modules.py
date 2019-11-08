from canvasapi import Canvas
from api_key import API_URL, API_KEY

canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(53357) # Cert II
# course = canvas.get_course(63381) # Cert III

modules = course.get_modules();

f = open("canvas-modules.txt", "w")

for m in modules:
    print(m);
    f.write(str(m) + "\n")
    items = m.get_module_items()
    for i in items:
        print(" * " + str(i))
        f.write(" * " + str(i) + "\n")

f.close()