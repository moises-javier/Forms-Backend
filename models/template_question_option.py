from utils.db import db
from datetime import datetime

class TemplateQuestionOption(db.Model):
    __tablename__ = "template_question_option"

    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.String(500))
    id_template_question = db.Column(db.Integer, db.ForeignKey("template_question.id"))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def add_all(self, data):
        db.session.add_all(data)
        db.session.commit()

    def to_dict(self):
        return {            
            "id": self.id,
            "option": self.option
        }

    def session_delete(self):
        db.session.delete(self)

    @classmethod
    def commit(cls):
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()