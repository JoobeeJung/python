#24BookDB.py

import sqlite3

def createTable():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE book_table (
            idx     integer primary key,
            title   text,
            year    integer,
            company text,
            pages   integer,
            exist_flag integer,
            price   integer            
        )  '''
    )

    conn.commit()
    conn.close()

"""
    SELECT f1,f2,,,, FROM 테이블명 WHERE 조건
                            age>10 and age<=12  ORDER BY
"""


def selectBooks():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    #cur.execute("SELECT * FROM book_table WHERE price>15000")
    #cur.execute("SELECT * FROM book_table")
    cur.execute("SELECT * FROM book_table order by title DESC")

    print("[1] 전체 데이터 출력")
    books = cur.fetchall()

    for book in books:
        print(book)

    print("[2] 일부 데이터 조회")
    cur.execute("SELECT * FROM book_table")
    books = cur.fetchmany(3)
    for book in books:
        print(book)
    conn.close()

def updateBooks():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()

    key = int(input("insert key : "))
    title = input("Insert title : ")
    price = int(input("insert price : "))

    sql = "UPDATE book_table SET title=? , price=? WHERE idx=? "
    cur.execute(sql, (title, price, key ) )
    conn.commit()

    conn.close()

def deleteBooks():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()

    key = input("insert key to Delete : ")

    sql = "DELETE FROM book_table  WHERE idx=? "
    cur.execute(sql, key )
    conn.commit()

    conn.close()

def insertBooks():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()

    sql = "insert into book_table (title, year, company, pages, exist_flag, price) " \
          "values (?, ?, ?, ?, ?, ? )"
    #cur.execute(sql, ('자바', '2020', '하나은행', '300', '1', '12000') )

    #cur.execute("insert into book_table (title, year, company, pages, exist_flag, price) "
    #            "values ('파이썬', '2022', '국민은행', '1234', '1', '12000'  )")

    books = [
        ('책제목1', '2020', '국민은행', '3456', '0', '8000'),
        ('책제목2', '2010', '국민은행', '356', '1', '7000'),
        ('책제목3', '2021', '국민출판', '656', '0', '18000'),
        ('책제목4', '2020', '하나출판', '340', '1', '12000'),
        ('책제목5', '2018', '신한출판', '956', '1', '23000')
    ]

    cur.executemany(sql, books)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    #createTable()
    #print("Insert...")
    #insertBooks()
    #print("Update")
    #updateBooks()

    deleteBooks()
    print("Select")
    selectBooks()

