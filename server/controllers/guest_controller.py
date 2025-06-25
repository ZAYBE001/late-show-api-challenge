# server/controllers/guest_controller.py
from flask import Blueprint, request, jsonify
from server.extensions import db
from server.models.guest import Guest

bp = Blueprint('guest', __name__)

@bp.route('/guests', methods=['GET'])
def list_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@bp.route('/guests/<int:id>', methods=['GET'])
def get_guest(id):
    guest = Guest.query.get_or_404(id)
    return jsonify(guest.to_dict())

@bp.route('/guests', methods=['POST'])
def create_guest():
    data = request.get_json()
    guest = Guest(name=data['name'], occupation=data['occupation'])
    db.session.add(guest)
    db.session.commit()
    return jsonify(guest.to_dict()), 201

@bp.route('/guests/<int:id>', methods=['PUT'])
def update_guest(id):
    guest = Guest.query.get_or_404(id)
    data = request.get_json()
    guest.name = data.get('name', guest.name)
    guest.occupation = data.get('occupation', guest.occupation)
    db.session.commit()
    return jsonify(guest.to_dict())

@bp.route('/guests/<int:id>', methods=['DELETE'])
def delete_guest(id):
    guest = Guest.query.get_or_404(id)
    db.session.delete(guest)
    db.session.commit()
    return '', 204