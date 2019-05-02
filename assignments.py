from canvasapi import Canvas

API_URL = "https://canvas.example.com"
API_KEY = "XXX"
canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(12345)

assignments = course.get_assignments(order_by='name') # Or use bucket='ungraded' 

f = open("canvas-assignments.txt", "w")
for assignment in assignments:
    if(assignment.published == True):
        print(assignment.name)
        f.writelines(assignment.name + "\n")
f.close()
