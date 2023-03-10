from utils.logger import setup_logger
from flask import request
from flask_restful import Resource
from services.template_sheet_service import TemplateSheetService

logger = setup_logger(__name__, "logs/resources/sheet.log")

class Sheet(Resource):
    def __init__(self):
        self.logger = logger
        self.sheet_service = TemplateSheetService()

    def get(self, id):
        try:
            return self.sheet_service.get_by_id(id)
        except Exception as e:
            self.logger.error(e)

        return {"message": "Something went wrong"}, 500

    def put(self, id):
        try:
            json_data = request.get_json(force=True)
            json_data["id"] = id
            return self.sheet_service.update(json_data)
        except Exception as e:
            self.logger.error(e)

        return {"message": "Something went wrong"}, 500

    def delete(self, id):
        try:
            return self.sheet_service.delete(id)
        except Exception as e:
            self.logger.error(e)
        
        return {"message": "Something went wrong"}, 500

class SheetList(Resource):
    def __init__(self):
        self.logger = logger
        self.sheet_service = TemplateSheetService()

    def get(self):
        try:
            return self.sheet_service.get_all(request.args)
        except Exception as e:
            self.logger.error(e)
        
        return {"message": "Something went wrong"}, 500

    def post(self):
        try:
            json_data = request.get_json(force=True)
            return self.sheet_service.create(json_data)
        except Exception as e:
            self.logger.error(e)

        return {"message": "Something went wrong"}, 500