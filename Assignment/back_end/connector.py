import mysql.connector

class Staff():
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost',
                                           user='root',
                                           password='sujitakc',
                                           database='rockey')
        self.cursor = self.con.cursor()

    def insert(self, query, values):
        self.cursor.execute(query, values)
        self.con.commit()

    def update(self, query, values):
        self.cursor.execute(query, values)
        self.con.commit()

    def delete(self, query, values):
        self.cursor.execute(query, values)
        self.con.commit()

    def select(self,query):
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        self.con.commit()
        return records

    def search(self, query, values):
        self.cursor.execute(query, values)
        records = self.cursor.fetchall()
        self.con.commit()
        return records