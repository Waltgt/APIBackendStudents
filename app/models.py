from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Careers(db.Model):
    __tablename__ = 'careers'
    code = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Career {self.code}: {self.description}>'
    

class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    career_code = db.Column(db.String(10), db.ForeignKey('careers.code'), nullable=False)

    career = db.relationship('Careers', backref=db.backref('students'))

    def __repr__(self):
        return f'<Student {self.id}: {self.first_name} {self.last_name}>'