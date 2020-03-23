# This script creates an HTML file with a table that has every assignment in it.
# By Marcus Wynwood (MarcusTeachUs.com)

from canvasapi import Canvas
from api_key import API_URL, API_KEY
from datetime import datetime

canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(73609) # <-- Put the course ID here

assignments = course.get_assignments(order_by='name') 

f = open("assignments.html", "w")
f.write("<table border='1' cellpadding='5' style='border-collapse: collapse;'>")
f.write("<h1>Assessments in " + course.name + "</h1>")
f.write("<p><a href='" + API_URL + "/courses/" + str(course.id) + "'>" + API_URL + "/courses/" + str(course.id) + "</a></p>")
now = datetime.now()
f.write("<p><em>Generated on " + now.strftime("%d %B %Y, %H:%M:%S") + " by <a href='https://github.com/mwynwood/myCanvasScripts/blob/master/assignments.py'>assignments.py</a></em></p>")

count = 1
for assignment in assignments:

    assType = "Assignment"
    if(assignment.is_quiz_assignment == True):
        assType="Quiz"

    if(assignment.published == True and assignment.omit_from_final_grade == False):
        f.write("<tr>")
        f.write("<td>" + str(count) + "</td>")
        # f.write("<td><input type='checkbox'></td>")
        f.write("<td><a href='" + assignment.html_url + "'>" + assignment.name + "</a></td>")
        f.write("<td>" + assType + "</td>")
        # f.write("<td>" + str(assignment.assignment_group_id) + "</td>")
        f.write("</tr>")
    count = count + 1

f.write("</table>")
f.close()