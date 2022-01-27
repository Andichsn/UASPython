from cgitb import text
import requests
import mysql.connector
from texttable import Texttable

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
    cursor.execute("SELECT * FROM tbl_students_0545")
    myresult = cursor.fetchall()
    if myresult == '':
        mysql = '''INSERT INTO tbl_students_0545(no, nim, nama, jk, jurusan, alamat) VALUES (%s, %s, %s, %s, %s, %s)'''
        for i in data['data']:
            val = (i['id'], i['nim'], i['nama'], i['jk'], i['jurusan'], i['alamat'])
            cursor.execute(mysql,val)
            db.commit()
        
def showData():
    table = Texttable()
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM tbl_students_0545")
    myresult = mycursor.fetchall()
    # print('\n+----+---------+-------------+----+-----------------+-------------+')
    # print('| No |   NIM   |     NAMA    | JK |     Jurusan     |    Alamat   |')
    # print('+----+---------+-------------+----+-----------------+-------------+')
    # for j in myresult:
    #     print(j)
    mycursor.close()
    no = 0
    dbnim = []
    dbnama = []
    dbjk = []
    dbjurusan = []
    dbalamat = []

    for data in myresult:       
        dbnim.append(data[1])
        dbnama.append(data[2])
        dbjk.append(data[3])
        dbjurusan.append(data[4])
        dbalamat.append(data[5])
        no += 1
    
    for i in range(no):
        nim = dbnim
        nama = dbnama
        jk = dbjk
        jurusan = dbjurusan
        alamat = dbalamat      
    
        table.add_rows([['No.', 'NIM', 'Nama', 'JK', 'Jurusan', 'Alamat'],[i+1, nim[i], nama[i], jk[i], jurusan[i], alamat[i]]])
    print(table.draw())


def limitData():
    table = Texttable()
    line = int(input("\nBatas limit : "))
    mycursor = db.cursor()
    mysql = ("SELECT * FROM tbl_students_0545")
    mycursor.execute(mysql)
    myresult = mycursor.fetchmany(line)
    # print('\n+----+---------+-------------+----+-----------------+-------------+')
    # print('| No |   NIM   |     NAMA    | JK |     Jurusan     |    Alamat   |')
    # print('+----+---------+-------------+----+-----------------+-------------+')
    # for j in myresult:
    #     print(j)

    no = 0
    dbnim = []
    dbnama = []
    dbjk = []
    dbjurusan = []
    dbalamat = []

    for data in myresult:       
        dbnim.append(data[1])
        dbnama.append(data[2])
        dbjk.append(data[3])
        dbjurusan.append(data[4])
        dbalamat.append(data[5])
        no += 1
    
    for i in range(no):
        nim = dbnim
        nama = dbnama
        jk = dbjk
        jurusan = dbjurusan
        alamat = dbalamat      
    
        table.add_rows([['No.', 'NIM', 'Nama', 'JK', 'Jurusan', 'Alamat'],[i+1, nim[i], nama[i], jk[i], jurusan[i], alamat[i]]])
    print(table.draw())

def select_data_by_Nim():
    table = Texttable()
    ktm = str(input("\nMasukkan NIM: "))
    mycursor = db.cursor()
    # mysql = ("SELECT * FROM tbl_students_0545 WHERE nim=%s", (ktm,))
    mycursor.execute("SELECT * FROM tbl_students_0545 WHERE nim=%s", (ktm,))
    myresult = mycursor.fetchall()
    # print('\n+----+---------+-------------+----+-----------------+-------------+')
    # print('| no |   NIM   |     NAMA    | JK |     Jurusan     |    Alamat   |')
    # print('+----+---------+-------------+----+-----------------+-------------+')
    # print(myresult)
    
    no = 0
    dbnim = []
    dbnama = []
    dbjk = []
    dbjurusan = []
    dbalamat = []
    
    for data in myresult:       
        dbnim.append(data[1])
        dbnama.append(data[2])
        dbjk.append(data[3])
        dbjurusan.append(data[4])
        dbalamat.append(data[5])
        no += 1
    
    for i in range(no):
        nim = dbnim
        nama = dbnama
        jk = dbjk
        jurusan = dbjurusan
        alamat = dbalamat      
    
       
    if ktm in dbnim:
        table.add_rows([['No.', 'NIM', 'Nama', 'JK', 'Jurusan', 'Alamat'],[no, nim[i], nama[i], jk[i], jurusan[i], alamat[i]]])
        print(table.draw())
        show_menu()
        
    if ktm not in dbnim:
        table.add_rows([['No.', 'NIM', 'Nama', 'JK', 'Jurusan', 'Alamat'],['NA', 'NA', 'NA', 'NA', 'NA', 'NA']])
        print(table.draw())
        show_menu()

def show_menu():
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
        exit()
    else:
        pass

if __name__ == '__main__':
    #getAPI()
    while True:
        show_menu()
        
            
