from flask_marshmallow import Marshmallow
from .models import Students, Careers

ma = Marshmallow()

class CareerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Careers
        load_instance = True
        
career_schema = CareerSchema()
careers_schema = CareerSchema(many=True)

class StudentSchema(ma.SQLAlchemyAutoSchema):
    career = ma.Nested(CareerSchema)
    
    class Meta:
        model = Students
        load_instance = True
        include_fk = True
        
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)
        
        