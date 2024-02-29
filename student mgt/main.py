import requests
from bs4 import BeautifulSoup 
import  pandas as pd
import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database = "studentmanagmentsystem"
)

cursor = dataBase.cursor()
cursor.execute('create database if not exists studentmanagmentsystem')

url = "https://www.teachoo.com/16739/3814/Question-2/category/Case-Based-MCQ-Questions/"

r = requests.get(url)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
header = soup.find("tr")
headers = header.find_all("td")
titles= []

for i in headers:
    titles.append(i.get_text().strip().replace(".",""))

header = soup.find_all("tr")

maindata = []
for j in header[1:]:
    td =  j.find_all("td")
    data = {}
    for i  in range(len(td)):
        data[titles[i]] = td[i].get_text().strip()
    maindata.append(data)


# sql = "INSERT INTO STUDENT (Stud, Name, Course, Result)\
# VALUES (%s, %s, %s, %s)"

# sqlMaindata=[]
# for i in maindata:
#     sqldata  = tuple((i["Stud"],i["Name"], i["Course"], i["Result"]))
#     sqlMaindata.append(sqldata)

# print(sqlMaindata)
# cursor.executemany(sql, sqlMaindata)
# dataBase.commit()

df = pd.DataFrame(columns=maindata)
# print(maindata);