from utils.logger import setup_logger
from utils.schema import SheetSchema, PagUrlParams
from utils.helper import SchemaHelper
from models.template_sheet import TemplateSheet as TemplateSheetModel
from .template_question_service import TemplateQuestionService

logger = setup_logger(__name__, "logs/services/template_sheet.log")

class TemplateSheetService:
    def __init__(self):
        self.logger = logger

    def create(self, data):
        data, error = SchemaHelper.validate(SheetSchema, data)

        if error:
            self.logger.error(error)
            return {"message": "One or more fields are invalid"}, 400

        questions = None
        if "questions" in data:
            questions = data["questions"]
            del data["questions"]                

        try:                      
            sheet = TemplateSheetModel(**data)
            sheet.save_to_db()

            if questions:
                questions = [dict(item, **{"id_template_sheet": sheet.id}) for item in questions]
                question = TemplateQuestionService()
                question.create(questions, validate=False)

            return {"message": "Item created"}, 201
        except Exception as e:
            self.logger.error(e)

        return {"message": "Something went wrong"}, 500
    
    def get_all(self, req_params=None):
        offset, limit = 0, 10

        if req_params:
            req_params, error = SchemaHelper.validate(PagUrlParams, req_params)

            if error:
                self.logger.error(error)
                return {"message": "The url parameters are wrong"}, 400
        
        offset = req_params["offset"] if req_params and req_params["offset"] > 0 else offset
        limit = req_params["limit"] if req_params and req_params["limit"] > 0 else limit

        try:
            items = [i.to_dict() for i in TemplateSheetModel.query.limit(limit).offset(offset)]
            response = {"items": [{"id": i["id"], "title": i["title"], "description": i["description"]} for i in items]}
            return response, 200
        except Exception as e:
            self.logger.error(e)

        return {"message": "Something went wrong"}, 500
    
    def get_by_id(self, id):
        try:
            sheet = TemplateSheetModel.find_by_id(id)
            if sheet:
                response = sheet.to_dict()
                response["questions"] = []

                for q in sheet.questions:
                    question = q.to_dict()
                    question["options"] = []

                    for o in q.options:
                        question["options"].append(o.to_dict())

                    response["questions"].append(question)
                
                return response, 200
        except Exception as e:
            self.logger.error(e)
        
        return {"message": "Item not found"}, 404

    def update(self, data):
        data, error = SchemaHelper.validate(SheetSchema, data)

        if error:
            self.logger.error(error)
            return {"message": "One or more fields are invalid"}, 400

        try:
            sheet = TemplateSheetModel.find_by_id(data["id"])

            if not sheet:
                message, code = self.create(data)
            else:
                sheet.title = data["title"]
                sheet.description = data["description"]
                sheet.save_to_db()

                if "questions" in data:
                    questions = [dict(item, **{"id_template_sheet": sheet.id}) for item in data["questions"]]
                    question = TemplateQuestionService()
                    question.update(questions)

            return {"message": "Item updated"}, 200
        except Exception as e:
            self.logger.error(e)

        return {"message": "Something went wrong"}, 500

    def delete(self, id):
        try:
            sheet = TemplateSheetModel.find_by_id(id)
            if sheet:
                sheet.delete_from_db()
        except Exception as e:
            self.logger.error(e)

        return {"message": "Item deleted"}, 200