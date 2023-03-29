from utils.db import db
from datetime import datetime

class TemplateSheet(db.Model):
    __tablename__ = "template_sheet"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(400))
    id_sheet_type = db.Column(db.Integer, db.ForeignKey("sheet_type.id"))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    questions = db.relationship("TemplateQuestion", cascade="all,delete", backref="template_sheet")

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
            "title": self.title,
            "description": self.description
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()