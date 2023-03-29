from utils.logger import setup_logger
from utils.schema import QuestionSchema
from utils.helper import SchemaHelper
from models.template_question import TemplateQuestion as TemplateQuestionModel
from .template_question_option_service import TemplateQuestionOptionService

logger = setup_logger(__name__, "logs/services/template_question.log")

class TemplateQuestionService:
    def __init__(self):
        self.logger = logger

    def create(self, data: list, validate=True):
        if validate:
            data, error = SchemaHelper.validate(QuestionSchema, data, many=True)

            if error:
                self.logger.error(error)
                return False

        try:
            for qstn in data:
                options = None
                if "options" in qstn:
                    options = qstn["options"]
                    del qstn["options"]
                
                question = TemplateQuestionModel(**qstn)
                question.save_to_db()

                if options:
                    option_data = [{"id_template_question": question.id, "option": opt["option"]} for opt in options]
                    option = TemplateQuestionOptionService()
                    option.create(option_data)
                
            return True
        except Exception as e:
            self.logger.error(e)

        return False
    
    def update(self, data: list, validate=True):
        if validate:
            data, error = SchemaHelper.validate(QuestionSchema, data, many=True)

            if error:
                self.logger.error(error)
                return False
        
        try:
            new_questions = []
            old_questions = []

            for q in data:
                if "id" in q:
                    old_questions.append(q)
                else:
                    new_questions.append(q)

            questions = TemplateQuestionModel.query.filter_by(id_template_sheet=data[0]["id_template_sheet"]).all()

            for q in questions:
                delete = True
                for old_q in old_questions:
                    if old_q["id"] == q.id:
                        delete = False
                        q.question = old_q["question"]
                        q.id_field_type = old_q["id_field_type"]

                        if "options" in old_q:
                            option_data = [dict(i, **{"id_template_question": q.id}) for i in old_q["options"]]
                            option = TemplateQuestionOptionService()
                            option.update(option_data)
                        else:
                            for optn in q.options:
                                optn.delete_from_db()
                        break
                if delete:
                    q.session_delete()

            TemplateQuestionModel.commit()

            if new_questions:
                self.create(new_questions)
            
            return True
        except Exception as e:
            self.logger.error(e)
        
        return False