from utils.logger import setup_logger
from models.template_question_option import TemplateQuestionOption as TemplateQuestionOptionModel

logger = setup_logger(__name__, "logs/services/template_question_option.log")

class TemplateQuestionOptionService:
    def __init__(self):
        self.logger = logger

    def create(self, data: list):
        try:
            _data = list(map(lambda x: TemplateQuestionOptionModel(**x), data))
            option = TemplateQuestionOptionModel()
            option.add_all(_data)
            return True
        except Exception as e:
            self.logger.error(e)
        
        return False

    def update(self, data: list):
        try:            
            new_options = []
            old_options = []

            for opt in data:
                if "id" in opt:
                    old_options.append(opt)
                else:
                    new_options.append(opt)

            options = TemplateQuestionOptionModel.query.filter_by(
                id_template_question=data[0]["id_template_question"]).order_by(TemplateQuestionOptionModel.id).all()

            for opt in options:
                delete = True
                for item in old_options:
                    if item["id"] == opt.id:
                        delete = False
                        opt.option = item["option"]
                        break
                if delete:
                    opt.session_delete()

            TemplateQuestionOptionModel.commit()

            if new_options:
                self.create(new_options)

            return True
        except Exception as e:
            self.logger.error(e)
        
        return False