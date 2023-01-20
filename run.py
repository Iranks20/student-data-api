from application import application

from application.controllers.user import bp_app as user_mod
# from flask_cors import CORS
from flask_cors import CORS, cross_origin



application.register_blueprint(user_mod)

cors = CORS(application)
# cors = CORS(application, resources={r"/foo": {"origins": "*"}})


application.run(port=9001, host="0.0.0.0", debug=True)