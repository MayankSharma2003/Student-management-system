from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS, cross_origin
import jwt

app = Flask(__name__)
cors = CORS(app)

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="studentmanagmentsystem"   
)

cursor = dataBase.cursor()

header = {  
  "alg": "HS256",  
  "typ": "JWT"  
}  
  
secret = "Mayank"  
  

@app.route('/login', methods=['POST'])
@cross_origin(origins=[u"*"])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('studentId')

    print(username,password)
    role="student"
    if password == '1' and username == "admin":
        role="admin"
        myresult=True
        print("HAAHHA")
    else:
        query = f"SELECT * FROM STUDENT where stud = {password} and Name = '{username}'"
        cursor.execute(query)
        myresult = cursor.fetchall() 
        print("HIHIHIHI")
    
    if myresult:
        token = jwt.encode({'studentId':password}, secret, algorithm='HS256', headers=header)  
        return jsonify({'msg': 'Login','role':role,'token':token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
    
@app.route('/signup', methods=['POST'])
@cross_origin(origins=[u"*"])
def signup():
    data = request.get_json()
    username = data.get('username')
    studentId = data.get('studentId')
    email = data.get('email')
    contactnumber = data.get('contactNumber')
    address = data.get('address')
    dob = data.get('dob')
    coursename = data.get('coursename')
    grades = data.get('grades')

    query = f"SELECT * FROM STUDENT where stud = {studentId}"
    cursor.execute(query)
    myresult = cursor.fetchall() 
    # print(len(myresult))
    if len(myresult)==0:
        sql = "INSERT INTO STUDENT (Stud, Name, Course, Result,DOB, address, contactnumber,email)\
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        sqlMaindata=tuple((studentId,username,coursename,grades,dob,address,contactnumber,email))
        cursor.execute(sql, sqlMaindata)
        dataBase.commit()
        return jsonify({'msg': 'Signup'})
    else:
        return jsonify({'error': 'User already exist'}), 401


@app.route('/updateData', methods=['POST'])
@cross_origin(origins=[u"*"])
def updateData():
    data = request.get_json()
    username = data.get('name')
    studentId = data.get('studentId')
    email = data.get('email')
    contactnumber = data.get('contactNumber')
    coursename = data.get('coursename')
    grades = data.get('grades')
    sql = f"update STUDENT set Stud=%s, Name=%s, Course=%s, Result=%s, contactnumber=%s,email=%s where stud=%s"

    val=(studentId,username,coursename,grades,contactnumber,email,studentId)
    cursor.execute(sql,val)
    dataBase.commit()
    return jsonify({'msg': 'Updated'}), 200

@app.route('/deleteData', methods=['POST'])
@cross_origin(origins=[u"*"])
def deleteData():
    data = request.get_json()
    studentId = data.get('studentId')

    query = f"delete from student where stud={studentId}"
    cursor.execute(query)
    dataBase.commit()

    # if myresult:
    return jsonify(),200

@app.route('/allData', methods=['GET'])
@cross_origin(origins=[u"*"])
def allData():
    query = f"SELECT * FROM STUDENT where stud!=1"
    cursor.execute(query)
    myresult = cursor.fetchall() 

    if myresult:
        return jsonify({'students':myresult})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
    
@app.route('/myData', methods=['GET'])
@cross_origin(origins=[u"*"])
def myData():
    token = request.headers.get("Authorization")
    auth_token = jwt.decode(token,secret, algorithms=['HS256'])
    query = f"SELECT * FROM STUDENT where stud={auth_token['studentId']} "
    cursor.execute(query)
    myresult = cursor.fetchall() 

    if myresult:
        return jsonify({'students':myresult})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)

