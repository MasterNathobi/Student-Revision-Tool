from datetime import datetime
now = datetime.now()
joindate = now.strftime("%Y-%m-%d %H:%M:%S")
firstname = 'nathan'
surname = 'ritchie'
password = '123456'
username = 'nritchie03'

ID = firstname[0:3].title()+ surname[0:3].title()+now.strftime('%d%m%S')
print(ID)
