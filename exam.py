import csv

exams = []

with open('exam2.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, dialect='excel')

    for row in reader:
        exams.append(row)
        # print(row)
    
with open('exam.html', 'w') as html_file:
    index = 1;
    
    while index < len(exams):
        if index + 2 >= len(exams) or not (exams[index + 2][0] == ''):
            index = index + 2
            # print(exams[index + 2][0])
            continue
        
        print(exams[index][0])
        
        html_file.write("\n\n")
        html_file.write(exams[index][0])
        html_file.write("\n\n")
        
        html_file.write("<td>\n");
        html_file.write("\t<div class=\"exam\">\n");
        
        html_file.write("\t<div class=\"type\">" + exams[index][1] + "</div></br>\n");
        html_file.write("\t<div class=\"subject\">" + exams[index+1][1] + "</div></br>\n");
        html_file.write("\t<div class=\"name\">" + exams[index+2][1] + "</div></br>\n");
        html_file.write("\t<div class=\"time\">" + exams[index+4][1] + "</div></br>\n");
        
        html_file.write("\t</div>\n");
        html_file.write("</td>\n");
        
        
        
        html_file.write("<td>\n");
        html_file.write("\t<div class=\"exam\">\n");
        
        html_file.write("\t<div class=\"type\">" + exams[index][2] + "</div></br>\n");
        html_file.write("\t<div class=\"subject\">" + exams[index+1][2] + "</div></br>\n");
        html_file.write("\t<div class=\"name\">" + exams[index+2][2] + "</div></br>\n");
        html_file.write("\t<div class=\"time\">" + exams[index+4][2] + "</div></br>\n");
        
        html_file.write("\t</div>\n");
        html_file.write("</td>\n");
        
        
        
        # html_file.write("<td>\n");
        # html_file.write("\t<div class=\"exam\">\n");
        
        # html_file.write("\t<div class=\"type\">" + exams[index][3] + "</div></br>\n");
        # html_file.write("\t<div class=\"subject\">" + exams[index+1][3] + "</div></br>\n");
        # html_file.write("\t<div class=\"name\">" + exams[index+2][3] + "</div></br>\n");
        # html_file.write("\t<div class=\"time\">" + exams[index+4][3] + "</div></br>\n");
        
        # html_file.write("\t</div>\n");
        # html_file.write("</td>\n");
        
        
        
        index = index + 5