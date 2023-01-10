from application import application
from datetime import datetime, timedelta
import uuid
import phonenumbers
from flask import jsonify, request
from helper.dbhelper import Database as db
import requests


application.config['SECRET_KEY'] = 'a6d4c1d6828549b6ada2d94ef4aeb9a1'
class User:
    def __init__(self):
        print('students model')

    @staticmethod
    def all_students():
        sql = "SELECT * FROM student_data.accounts "
        data = db().select(sql)
        return jsonify(data)

    @staticmethod
    def studentsAdd():
        try:
            # _students_id = uuid.uuid4()
            _json = request.json
            _firstname = _json['firstname']
            _lastname = _json['lastname']
            _dateofbirth = _json['dateofbirth']
            _gender = _json['gender']
            _registrationnumber = _json['registrationnumber']
            _nationality = _json['nationality']
            _telephone = _json['telephone']
            _email = _json['email']
            _permanentaddress = _json['permanentaddress']
            _fathersname = _json['fathersname']
            _fathersnumber = _json['fathersnumber']
            _mothersname = _json['mothersname']
            _mothersnumber = _json['mothersnumber']
            # _guardianname = _json['guardianname']
            # _guardiannumber = _json['guardiannumber']
            # _course = _json['course'],
            # olevel marks begin
            _biology = _json['biology']
            _chemistry = _json['chemistry']
            _mathematics = _json['mathematics']
            _physics = _json['physics']
            _agriculture = _json['agriculture']
            _fn = _json['fn']
            _history = _json['history']
            _cre = _json['cre']
            _ire = _json['ire']
            _fineart = _json['fineart']
            _geography = _json['geography']
            _literature = _json['literature']
            _economics = _json['economics']
            _rukiga = _json['rukiga']
            _luganda = _json['luganda']
            _entpreneurship = _json['entpreneurship']
            _english = _json['english']
            _computer = _json['computer']
            # _technicaldrawing = _json['technicaldrawing']
            _french = _json['french']
            _accounting = _json['accounting']
            _kiswahili = _json['kiswahili']
            _commerce = _json['commerce']
            _chinesse = _json['chinesse']

            # alevel marks
            _bio = _json['bio']
            _chem = _json['chem']
            _mtc = _json['mtc']
            _phy = _json['phy']
            _agric = _json['agric']
            _foodnutrition = _json['foodnutrition']
            _hist = _json['hist']
            _divinity = _json['divinity']
            # _islam = _json['islam']
            _art = _json['art']
            _geog = _json['geog']
            _lit = _json['lit']
            _econ = _json['econ']
            _ruk = _json['ruk']
            _lug = _json['lug']
            _ent = _json['ent']
            _ict = _json['ict']
            _submaths = _json['submaths']
            _gp = _json['gp']
            # other qualifications
            _certificate = _json['certificate']
            _diploma = _json['diploma']
            _bachelors = _json['bachelors']

            check_students = get_students_detail(_email, _telephone)
            if len(check_students) > 0:
                return make_response(403, "student Already Exists")
            
            addStudents_dict = {"firstname": _firstname, "lastname": _lastname, "dateofbirth": _dateofbirth, "gender": _gender, "registrationnumber": _registrationnumber, "nationality": _nationality, "telephone": _telephone, "email": _email, "permanentaddress": _permanentaddress, "fathersname": _fathersname, "fathersnumber": _fathersnumber, "mothersname": _mothersname, "mothersnumber": _mothersnumber,
            "biology": _biology, "chemistry": _chemistry, "mathematics": _mathematics, "physics": _physics, "agriculture": _agriculture, "fn": _fn, "history": _history, "cre": _cre, "ire": _ire, "fineart": _fineart, "geography": _geography, "literature": _literature, "economics": _economics, "rukiga": _rukiga, "luganda": _luganda, "entpreneurship": _entpreneurship, "english": _english, "computer": _computer, "french": _french, "accounting": _accounting, "kiswahili": _kiswahili, "commerce": _commerce, "chinesse": _chinesse,
            "bio": _bio, "chem": _chem, "mtc": _mtc, "phy": _phy, "agric": _agric, "foodnutrition": _foodnutrition, "hist": _hist, "divinity": _divinity, "art": _art, "geog": _geog, "lit": _lit, "econ": _econ, "ruk": _ruk, "lug": _lug, "ent": _ent, "ict": _ict, "submaths": _submaths, "gp": _gp, "certificate": _certificate, "diploma": _diploma, "bachelors": _bachelors}
            
            print(addStudents_dict)
            data = db().insert('student_data.accounts', **addStudents_dict)
            print(data)

            
            response = make_response(100, "thanks for submitting your information")
            print(response)

            return response
        except Exception as e:
            print(e)
            response = make_response(403, "failed retry")
            return response






# students details based on register model
def get_students_detail(Email, telephone):
    sql = "SELECT * FROM student_data.accounts WHERE email = '" + Email + "' OR telephone = '" + telephone + "' "
    data = db().select(sql)
    return data

#responses
def make_response(status, message):
    return jsonify({"message": message, "status": status})