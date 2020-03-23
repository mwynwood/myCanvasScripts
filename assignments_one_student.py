# This script creates an HTML file with a table that has every assignment in it from a particular student
# By Marcus Wynwood (MarcusTeachUs.com)

from canvasapi import Canvas
from api_key import API_URL, API_KEY
from datetime import datetime

canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(53357) # <-- Put the course ID here
student_id = 25933 # <-- Student you want

assignments = course.get_assignments(order_by='name') 

f = open("assignments_one_student.html", "w")
f.write("<table border='1' cellpadding='5' style='border-collapse: collapse;'>")
f.write("<h1>Assessment Tasks by Student " + str(student_id) + " in " + course.name + "</h1>")
f.write("<p><a href='" + API_URL + "/courses/" + str(course.id) + "'>" + API_URL + "/courses/" + str(course.id) + "</a></p>")
now = datetime.now()
f.write("<p><em>Generated on " + now.strftime("%d %B %Y, %H:%M:%S") + " by <a href='https://github.com/mwynwood/myCanvasScripts/blob/master/assignments_one_student.py'>assignments_one_student.py</a></em></p>")

count = 1
for assignment in assignments:

    assType = "Assignment"
    if(assignment.is_quiz_assignment == True):
        assType="Quiz"

    if(assignment.published == True and assignment.omit_from_final_grade == False):
        f.write("<tr>")
        f.write("<td>" + str(count) + "</td>")
        # https://canvas.education.tas.gov.au/courses/73609/gradebook/speed_grader?assignment_id=419848&student_id=23507
        f.write("<td><a href='" + API_URL + "/courses/" + str(course.id) + "/gradebook/speed_grader?assignment_id=" + str(assignment.id) + "&student_id=" + str(student_id) + "'>" + assignment.name + "</a></td>")
        f.write("<td>" + assType + "</td>")
        f.write("</tr>")
    count = count + 1

f.write("</table>")
f.close()