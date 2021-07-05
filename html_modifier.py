import csv
input_csv='Resources/employee_data.csv'
input_html='Resources/original_html_file.html'
output_html='Resources/html_file_modified.html'

def read_csv_and_format(input_csv):
    table_data=""
    with open(input_csv, 'r') as file:
        employee_data = csv.reader(file)
        table_data += "\n\t\t\t"
        for row in employee_data:
            table_data += "\t\t" + "<tr>"
            table_data += "<td>"
            list_to_str = str(row[0])
            list_to_str = list_to_str.replace(";", "</td><td>")
            list_to_str += "</td>"
            table_data += list_to_str
            table_data += "</tr>"
            table_data+="\n\t\t\t"
        return table_data


def read_html_file(input_html):
    file=open(input_html,'r')
    old_file = file.read()
    file.close()
    return old_file


def html_file_formatter_outputter(output_html,old_file,table_data):
    new_file = old_file.format(table_data)
    file=open(output_html,'w')
    file.write(new_file)
    file.close()

table_data = read_csv_and_format(input_csv)
print(table_data)

old_file=read_html_file(input_html)
print(old_file)

html_file_formatter_outputter(output_html,old_file,table_data)
