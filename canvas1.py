from canvasapi import Canvas
from api_key import API_URL, API_KEY

canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(53357) # C2
# course = canvas.get_course(63381) # C3

# assignments = course.get_assignments(bucket='ungraded')
assignments = course.get_assignments(order_by='name')

f = open("canvas-assignments.html", "w")
f.write("<table border='1' cellpadding='5' style='border-collapse: collapse;'>")
for assignment in assignments:

    assType = "Assignment"
    if(assignment.is_quiz_assignment == True):
        assType="Quiz"

    if(assignment.published == True and assignment.omit_from_final_grade == False):
        f.write("<tr>")
        f.write("<td><input type='checkbox'></td>")
        f.write("<td><a href='" + assignment.html_url + "'>" + assignment.name + "</a></td>")
        # f.write("<td>" + assType + "</td>")
        # f.write("<td>" + str(assignment.assignment_group_id) + "</td>")
        f.write("</tr>")

f.write("</table>")
f.close()