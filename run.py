from application import application

from application.controllers.user import bp_app as user_mod
from flask_cors import CORS


application.register_blueprint(user_mod)

cors = CORS(application)

application.run(port=9001, host="0.0.0.0", debug=True)