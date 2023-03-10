from app import app
from utils.db import db

from models import template_sheet
from models import template_question
from models import template_question_option
from models import sheet
from models import field_type
from models import sheet_type

db.init_app(app)

with app.app_context():
    db.create_all()
    
    sheetType = sheet_type.SheetType(**{"name": "Form", "description": "Form"})
    sheetType.save_to_db()

    field_types = [
        field_type.FieldType(**{"name": "Short answer text", "description": "Short answer text"}),
        field_type.FieldType(**{"name": "Paragraph", "description": "Paragraph"}),
        field_type.FieldType(**{"name": "Several options", "description": "Several options"}),
    ]

    fieldType = field_type.FieldType()
    fieldType.add_all(field_types)
