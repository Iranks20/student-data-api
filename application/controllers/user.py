from flask import Blueprint, request, jsonify, json
from application.models.user import User

bp_app = Blueprint('mod_user', __name__)
# getting all students
@bp_app.route('/all_students')
def get_students():
    data = User.all_students()
    return data

# Creating a user
@bp_app.route('/add_students', methods=['POST'])
def add_students():
    data = User.studentsAdd()
    return data