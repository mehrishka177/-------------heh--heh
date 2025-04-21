import matpolylib.pylot as plt

students_names=
["sanjay","Rahul","Karan","Wasim","Ramesh","Ajay","Sartaj","Pruya"]
students_marks=[35,50,20,45,25,40,25,40]

marks_perc = []

for x in student_marks:
         res = (x/50)*100
         marks_perc.append(res)

print(marks_perc)

def marks_line_chart():
  plt.plot(students_names,students_marks)
  plt.plot(students_names,students_marks)
  plt.xlabel("students marks graph")
  plt.ylabel("students marks")
  plt.show()

marks_line_chart()

def prcentege_bar_chart():
    plt.bar(students_names,marks_prcs)
    plt.title("students prcentege graph")
    plt.xlabel("students names")
    plt.ylabel("students percentage")
    plt.show()
    







  