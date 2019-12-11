from os import getenv

import connexion

DEBUG = getenv("DEBUG", default=False)

options = {"swagger_ui": DEBUG}
app = connexion.FlaskApp(__name__, options=options)
app.add_api("api_spec.yml")
if DEBUG:
    app.run(debug=True)
