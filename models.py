"""SQLAlchemy models for blogly."""
from datetime import timezone, datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    power_level = db.Column(db.Integer, nullable=False, default=9000)

    posts = db.relationship('Post', backref="user", cascade="all, delete-orphan")
    @property
    def full_name(self):
        """Return full name of user with power level"""

        return f"{self.first_name} {self.last_name} : power level {self.power_level}"




class Post(db.Model):
    """Model for posts"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    @property
    def formated_date(self):
        """Returns a well formated date"""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
