users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for i in range(len(users['Students'])):
    length = len(users['Students'][i]['first_name'])+len(users['Students'][i]['last_name'])
    print((i+1),' - ',users['Students'][i]['first_name'],' '+users['Students'][i]['last_name'],' - ',length)
for i in range(len(users['Instructors'])):
    length = len(users['Instructors'][i]['first_name'])+len(users['Instructors'][i]['last_name'])
    print((i+1),' - ',users['Instructors'][i]['first_name'],' ',users['Instructors'][i]['last_name'],' - ',length)