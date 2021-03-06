try:
    from flask import Flask, jsonify, request
    from flask_sqlalchemy import SQLAlchemy
    app = Flask(__name__, template_folder="views")

    driver = "mysql://"
    username_password = "root:tranbo9x"
    hostname = "172.16.69.251:3306"
    database_name = "/status_page"

    databse_uri = driver + username_password + "@" + hostname + database_name

    app.config['SQLALCHEMY_DATABASE_URI'] = databse_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    catalogs = {
        "incidents": "http://localhost:5000/api/incidents"
    }
except BaseException as e:
    raise e
