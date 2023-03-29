from marshmallow import Schema, fields, validate, ValidationError, validates

class QuestionOptionSchema(Schema):
    id = fields.Int()
    option = fields.Str(required=True)
    id_template_question = fields.Int()

class QuestionSchema(Schema):
    id = fields.Int()
    question = fields.Str(required=True, validate=validate.Length(min=2, max=250))
    correct_answer = fields.List(fields.Int(required=True))
    id_template_sheet = fields.Int()
    id_field_type = fields.Int(required=True)
    options = fields.List(fields.Nested(QuestionOptionSchema))

class SheetSchema(Schema):
    id = fields.Int()
    title = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    description = fields.Str(required=True, validate=validate.Length(min=2, max=300))
    id_sheet_type = fields.Int(required=True)
    questions = fields.List(fields.Nested(QuestionSchema))

class PagUrlParams(Schema):
    offset = fields.Int(required=False)
    limit = fields.Int(required=False)