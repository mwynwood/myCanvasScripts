from canvasapi import Canvas

API_URL = "https://canvas.example.com"
API_KEY = "XXX"
canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(12345)

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
