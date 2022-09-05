from . import db
from sqlalchemy.sql import func

class newRecipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    header = db.Column(db.String(30))
    data = db.Column(db.String(10000))