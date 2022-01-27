import requests
import mysql.connector

#https://api.abcfdab.cfd/students

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_akademik_0545"
)


def getAPI():
    endpoint = "students"
    base_url = "https://api.abcfdab.cfd/"
    response = requests.get(base_url+endpoint)
    data = response.json()
    cursor = db.cursor()
    mysql = '''INSERT INTO tbl_students_0545(no, nim, nama, jk, jurusan, alamat) VALUES (%s, %s, %s, %s, %s, %s)'''
    for i in data['data']:
        val = (i['id'], i['nim'], i['nama'], i['jk'], i['jurusan'], i['alamat'])
        cursor.execute(mysql,val)
        db.commit()
        
def showData():
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM tbl_students_0545")
    myresult = mycursor.fetchall()
    print('\n+----+---------+-------------+----+-----------------+-------------+')
    print('| No |   NIM   |     NAMA    | JK |     Jurusan     |    Alamat   |')
    print('+----+---------+-------------+----+-----------------+-------------+')
    for j in myresult:
        print(j)

def limitData():
    line = int(input("\nBatas limit : "))
    mycursor = db.cursor()
    mysql = ("SELECT * FROM tbl_students_0545")
    mycursor.execute(mysql)
    myresult = mycursor.fetchmany(line)
    print('\n+----+---------+-------------+----+-----------------+-------------+')
    print('| No |   NIM   |     NAMA    | JK |     Jurusan     |    Alamat   |')
    print('+----+---------+-------------+----+-----------------+-------------+')
    for j in myresult:
        print(j)

def select_data_by_Nim():
    v = "'"
    nim = input("\nMasukkan NIM: ")
    mycursor = db.cursor()
    mysql = ("SELECT * FROM tbl_students_0545 WHERE nim= ")
    mycursor.execute(mysql + v + nim + v)
    myresult = mycursor.fetchone()
    print('\n+----+---------+-------------+----+-----------------+-------------+')
    print('| no |   NIM   |     NAMA    | JK |     Jurusan     |    Alamat   |')
    print('+----+---------+-------------+----+-----------------+-------------+')
    print(myresult)

if __name__ == '__main__':
    getAPI()

    while True:
        print("\n1. Tampilkan semua data")
        print("2. Tampilkan data berdasarkan limit")
        print("3. Cari data berdasarkan NIM")
        print("0. Keluar")
        menu = int(input("Pilih menu: "))
        if menu == 1:
            showData()
        if menu == 2:
            limitData()
        if menu == 3:
            select_data_by_Nim()
        if menu == 0:
            break
        else:
            pass
            
