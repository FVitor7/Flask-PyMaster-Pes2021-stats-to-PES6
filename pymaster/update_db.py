import os
#import sqlacodegen
#import sqlautocode
#import flask_sqlacodegen

#os.system('sqlacodegen sqlite:///development.db > models.py')

#os.system('sqlautocode -d -o sqlite:///development.db')
#os.system("flask create-db")
os.system("flask populate-db")
os.system("flask add-user -u admin -p 1234")



