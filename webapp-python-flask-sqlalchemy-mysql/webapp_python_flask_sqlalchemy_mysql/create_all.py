from project import db
from project.models import Recipe
 
 
# create the database and the database table
db.create_all()
 
# insert recipe data
hello_world = HelloWorld("hello, world")
db.session.add(recipe1)
 
# commit the changes
db.session.commit()
