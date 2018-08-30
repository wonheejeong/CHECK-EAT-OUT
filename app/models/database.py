from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time=db.Column(db.DateTime)
    tag = db.Column(db.String(50))
    filepath = db.Column(db.String(255))



# for i in range (number_of_rows):
# 	print (row[i])
