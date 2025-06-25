# server/controllers/appearance_controller.py
from flask import Blueprint, request, jsonify
from server.extensions import db
from server.models.appearance import Appearance
from flask_jwt_extended import jwt_required

bp = Blueprint('appearance', __name__)

@bp.route('/appearances', methods=['GET'])
def list_appearances():
    appearances = Appearance.query.all()
    return jsonify([appearance.to_dict() for appearance in appearances])

@bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    appearance = Appearance(rating=data['rating'], guest_id=data['guest_id'], episode_id=data['episode_id'])
    db.session.add(appearance)
    db.session.commit()
    return jsonify(appearance.to_dict()), 201

@bp.route('/appearances/<int:id>', methods=['PUT'])
@jwt_required()
def update_appearance(id):
    appearance = Appearance.query.get_or_404(id)
    data = request.get_json()
    appearance.rating = data.get('rating', appearance.rating)
    appearance.guest_id = data.get('guest_id', appearance.guest_id)
    appearance.episode_id = data.get('episode_id', appearance.episode_id)
    db.session.commit()
    return jsonify(appearance.to_dict())

@bp.route('/appearances/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_appearance(id):
    appearance = Appearance.query.get_or_404(id)
    db.session.delete(appearance)
    db.session.commit()
    return '', 204