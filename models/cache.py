"""
Using to create a session for users and references
"""

from config import db
import datetime as dt
now = dt.datetime.today().isoformat(' ')

class cache(db.Model):
    """
    All data being storage on table "cache"

    id         | interger               | not null

    key        | character varying(255) | not null

    value      | text                   | not null
    
    expiration | integer                | not null
    """

    __tablename__ = "cache"

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(255), nullable=False, unique=True)
    value = db.Column(db.Text, nullable=False)
    expiration = db.Column(db.Integer, nullable=False)


class session(db.Model):
    """
    All data being storage on table "sessions"

    id            | integer | not null

    user_id       | integer                | 

    ip_address    | character varying(45)  | 

    user_agent    | text                   | 

    payload       | text                   | not null

    last_activity | character varying(255) | not null
    """

    __tablename__ = "sessions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    ip_address = db.Column(db.String(17))
    user_agent = db.Column(db.Text)
    payload = db.Column(db.Text, nullable=False)
    last_activity = db.Column(db.String(26), nullable=False)