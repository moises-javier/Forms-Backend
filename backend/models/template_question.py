from utils.db import db
from datetime import datetime

class TemplateQuestion(db.Model):
    __tablename__ = "template_question"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(250))
    correct_answer = db.Column(db.String(400))
    id_template_sheet = db.Column(db.Integer, db.ForeignKey("template_sheet.id"))

    id_field_type = db.Column(db.Integer, db.ForeignKey("field_type.id"))

    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    options = db.relationship("TemplateQuestionOption", cascade="all,delete", backref="template_question")
    question_in_sheet = db.relationship("Sheet", backref="question", lazy=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def add_all(self, data):
        db.session.add_all(data)
        db.session.commit()

    def session_delete(self):
        db.session.delete(self)

    def to_dict(self):
        return {            
            "id": self.id,
            "question": self.question,
            "correct_answer": self.correct_answer,
            "id_field_type": self.id_field_type,
        }

    @classmethod
    def commit(cls):
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
