from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://krzysztof@krzysztofmysql:Sxdcysio1@krzysztofmysql.mysql.database.azure.com:3306/tutorial"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)