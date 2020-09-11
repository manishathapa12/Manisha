import unittest
from back_end.connector import *
import front_end.main_interface
from model.model import *

class Test_learners(unittest.TestCase):
    def setUp(self):
        self.s=Members(101,"sudina","bhaktapur","female","9876543213","2001-12-09","su123@gmail.com")
        self.con=Staff()
        pass
    def test_get_ID(self):
        self.assertEqual(101,self.s.get_ID())
    def test_get_Name(self):
        self.assertEqual("sudina",self.s.get_Name())
    def test_set_ID(self):
        self.s.set_ID(6)
        self.assertEqual(6,self.s.get_ID())
    def test_set_Name(self):
        self.s.set_Name("sarita")
        self.assertEqual("sarita",self.s.get_Name())
    def test_get_Address(self):
        self.assertEqual("bhaktapur", self.s.get_Address())
    def test_get_DOB(self):
        self.assertEqual("2001-12-09", self.s.get_DOB())
    def test_set_Address(self):
        self.s.set_Address("Chitwan")
        self.assertEqual("Chitwan", self.s.get_Address())
    def test_set_DOB(self):
        self.s.set_DOB("2001-12-12")
        self.assertEqual("2001-12-12", self.s.get_DOB())
    def test_insert(self):
        query='insert into kalay values(%s,%s,%s,%s,%s,%s,%s);'
        values=(102,"Saugat Rijal","Bhaktapur","2000-12-04","Male","9808562357","saugat@hotmail.com")
        self.con.insert(query,values)
        query='select * from kalay where ID=%s;'
        values=(102,)
        actual=self.con.search(query,values)
        expect=[(102,"Saugat Rijal","Bhaktapur","2000-12-04","Male","9808562357","saugat@hotmail.com"),]
        self.assertEqual(actual,expect)
    def test_delete(self):
        query='delete from kalay where ID=%s;'
        values=(102,)
        self.con.insert(query,values)
        query='select * from kalay where ID=%s;'
        values=(102,)
        actual=self.con.search(query,values)
        expect=[]
        self.assertEqual(actual,expect)
    def test_update(self):
        query = 'update kalay set Name=%s,Address=%s,DOB=%s,Gender=%s,Contact=%s,Email=%s where ID=%s;'
        values = ("Yangchen Lama","Bouddha","1999-11-12","Female","9856347823","yamgchen@hotmail.com",1000)
        self.con.insert(query, values)
        query = 'select * from kalay' \
                ' where ID=%s;'
        values = (1000,)
        actual = self.con.search(query, values)
        expect = [(1000,"Yangchen Lama","Bouddha","1999-11-12","Female","9856347823","yamgchen@hotmail.com")]
        self.assertEqual(actual, expect)


    def test_linear_search(self):
        records=["Sudina","sudir"]
        Name="sudina"
        self.assertTrue(front_end.main_interface.linear_search(records,Name))

    def tearDown(self):
        self.s = None
        self.con = None
if __name__ == "__main__":
    unittest.main()
