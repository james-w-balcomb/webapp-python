from webapp_python_flask_sqlalchemy_mysql import db

 
class HelloWorld(db.Model):
 
    __tablename__ = "hello_world"
    
    record_id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True, autoincrement=True)
    hello_world = db.Column(db.String(12))
    hello = db.Column(db.String(5))
    comma = db.Column(db.String(1))
    world = db.Column(db.String(5))
    
    def __init__(self, hello_world):
        self.record_id = record_id
        self.hello_world = hello_world
        self.hello = hello
        self.comma = comma
        self.world = world
    
    def __repr__(self):
        return "<hello_world {}".format(self.hello_world)
