# server/models/appearance.py
from server.extensions import db
from server.models.guest import Guest
from server.models.episode import Episode

class Appearance(db.Model):
    __tablename__ = 'appearances'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id', ondelete='CASCADE'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id', ondelete='CASCADE'), nullable=False)

    guest = db.relationship('Guest', backref=db.backref('appearances', lazy=True))
    episode = db.relationship('Episode', backref=db.backref('appearances', lazy=True))

    def __init__(self, rating, guest, episode):
        self.rating = rating
        self.guest = guest
        self.episode = episode

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'guest_id': self.guest_id,
            'episode_id': self.episode_id
        }