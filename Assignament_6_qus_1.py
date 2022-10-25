import json

file = open ("C:\\Users\\USER\\Documents\\DS290822B\\_Assignament_6\\employee.json","r")

data = json.load(file)

for i  in data ['employee_details']:
    print(i)

file.close()