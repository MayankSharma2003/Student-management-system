# from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
# app = Flask(__name__)
# cors = CORS(app)

# @app.route('/login', methods=['POST'])
# @cross_origin(origins=[u"*"])
# def login():
#     # Get username and password from request
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')

#     # Validate credentials (dummy example)
#     if username == 'admin' and password == 'password':
#         # Return a dummy token upon successful login
#         return jsonify({'msg': ''})
#     else:
#         return jsonify({'error': 'Invalid credentials'}), 401

# @app.route('/protected_data', methods=['GET'])
# def protected_data():
#     # Access token from request headers
#     token = request.headers.get('Authorization')

#     # Validate token (dummy example)
#     if token == 'dummy_token':
#         # Return protected data
#         return jsonify({'data': 'Protected data'})
#     else:
#         return jsonify({'error': 'Unauthorized'}), 401

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="studentmanagmentsystem"   
)

cursor = dataBase.cursor()


@app.route('/login', methods=['POST'])
@cross_origin(origins=[u"*"])
def login():
    # Get username and password from request
    data = request.get_json()
    username = data.get('username')
    password = data.get('studentId')

    query = f"SELECT * FROM STUDENT where stud = {password} and Name = '{username}'"
    cursor.execute(query)
    myresult = cursor.fetchall() 
    # Validate credentials (dummy example)
    if myresult:
        return jsonify({'msg': 'Login'})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401


@app.route('/protected_data', methods=['GET'])
def protected_data():
    # You can remove token validation here
    # Access protected data directly or implement other logic as needed
    return jsonify({'data': 'Protected data'})


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def access(self, course):
        query = "UPDATE STUDENT SET Course=%s WHERE stud=%s"
        value = (course, self.id)
        cursor.execute(query, value)
        dataBase.commit()
        return "Course updated successfully"

    def view_grades(self):
        query = f"SELECT * FROM STUDENT WHERE stud = {self.id}"
        cursor.execute(query)
        myresult = cursor.fetchall()
        return myresult

    def update_contact_info(self, contact_info):
        # Implement update contact information logic here
        pass


if __name__ == '__main__':
    app.run(debug=True)


#@app.route('/student', methods=['POST'])
# def create_student():
#     data = request.json
#     name = data.get('name')
#     id = data.get('id')
#     new_student = Student(name, id)
#     return jsonify({'message': 'Student created successfully'}), 201


# @app.route('/student/<int:id>/course', methods=['PUT'])
# def update_course(id):
#     student = Student(None, id)
#     course = request.json.get('course')
#     response = student.access(course)
#     return jsonify({'message': response}), 200


# @app.route('/student/<int:id>/grades', methods=['GET'])
# def get_grades(id):
#     student = Student(None, id)
#     grades = student.view_grades()
#     return jsonify({'grades': grades}), 200


# @app.route('/student/<int:id>/contact', methods=['PUT'])
# def update_contact_info(id):
#     contact_info = request.json.get('contact_info')
#     student = Student(None, id)
#     student.update_contact_info(contact_info)
#     return jsonify({'message': 'Contact information updated successfully'}), 200

