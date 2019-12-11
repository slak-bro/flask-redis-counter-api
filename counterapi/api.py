import connexion

app = connexion.FlaskApp(__name__)
app.add_api("api_spec.yml")
app.run(port=8080)
