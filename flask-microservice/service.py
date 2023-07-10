from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

app = Flask(__name__)

engine = create_engine("postgres://flask_microservice_6pa7_user:WxfEZ6uhdOUI8EZljdzqO9BdGCkYmMvL@dpg-cim4kamnqqlfm48dpaog-a.oregon-postgres.render.com/flask_microservice_6pa7")

Base = declarative_base()

class User(Base) :
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

Base.metadata.create_all(engine)
print("Table 'users' created successfully.")

Session = sessionmaker(engine)


@app.route("/api/user", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data["name"]
    try:
        session = Session()
        new_user = User(name=name)
        session.add(new_user)
        session.commit()
        return {"id": new_user.id, "name": new_user.name, "message": f"User {name} created."}, 201
    except Exception as e:
        print(f"The error '{e}' occurred.")
        return {"error": "An error occurred while creating the user."}, 500

@app.route("/api/user", methods=["GET"])
def get_all_users():
    try:
        session = Session()
        users = session.query(User).all()
        if users:
            result = []
            for user in users:
                result.append({"id": user.id, "name": user.name})
            return jsonify(result)
        else:
            return jsonify({"error": f"Users not found."}), 404
    except Exception as e:
        print(f"The error '{e}' occurred.")
        return {"error": "An error occurred while getting all users."}, 500
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")