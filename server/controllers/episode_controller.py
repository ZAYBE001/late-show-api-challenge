# server/controllers/episode_controller.py
from flask import Blueprint, request, jsonify
from server.extensions import db 
from server.models.episode import Episode

bp = Blueprint('episode', __name__)

@bp.route('/episodes', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify(episode.to_dict())

@bp.route('/episodes', methods=['POST'])
def create_episode():
    data = request.get_json()
    episode = Episode(date=data['date'], number=data['number'])
    db.session.add(episode)
    db.session.commit()
    return jsonify(episode.to_dict()), 201

@bp.route('/episodes/<int:id>', methods=['PUT'])
def update_episode(id):
    episode = Episode.query.get_or_404(id)
    data = request.get_json()
    episode.date = data.get('date', episode.date)
    episode.number = data.get('number', episode.number)
    db.session.commit()
    return jsonify(episode.to_dict())

@bp.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return '', 204