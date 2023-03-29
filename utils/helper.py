from marshmallow import ValidationError

class SchemaHelper:
    @classmethod
    def validate(cls, _schema, data, many=False,):
        resp, error = None, None
        try:
            resp = _schema(many=many).load(data)
        except ValidationError as err:
            error = err
        return resp, error        
