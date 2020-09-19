import unittest
import hands_on_1
import hands_on_2
from hands_on_2 import Player,Sample

class SampleTest(unittest.TestCase):

    def test_lstrev(self):
        self.assertEqual(hands_on_1.lst_rev([1,2,3,4,5]),[5,4,3,2,1])
        self.assertEqual(hands_on_1.lst_rev([1, -2, -3, 4, 5]), [5, 4, -3, -2, 1])
        self.assertNotEqual(hands_on_1.lst_rev([1]), [1,2,3])
        self.assertRaises(TypeError,hands_on_1.lst_rev,1)

    def test_starting_zero_InList(self):
        self.assertEqual(hands_on_1.StartZero([1,0,2,0,3]),[0,0,1,2,3])
        self.assertEqual(hands_on_1.StartZero([1,2,3,4,5]), [1,2,3,4,5])
        self.assertNotEqual(hands_on_1.StartZero([0,0,0]), [])
        self.assertRaises(TypeError,hands_on_1.StartZero([1,2,3,4,5]))

    def test_lstmerge_inAsce(self):
        self.assertEqual(hands_on_1.merge([1,2,3],[4,5,6]),[1,2,3,4,5,6])
        self.assertNotEqual(hands_on_1.merge([1,2,3],[]),[1,2,3,4])
        self.assertRaises(TypeError,hands_on_1.merge([1,2],[1,2,3]))

    def test_char_rev(self):
        self.assertEqual(hands_on_1.abc("aBGtu"),"AbgTU")
        self.assertEqual(hands_on_1.abc("aB$tu"), "Ab$TU")
        self.assertRaises(TypeError,hands_on_1.abc('1'))
        self.assertNotEqual(hands_on_1.abc("!@#$%^"), "Error")

    def test_oddeven(self):
        self.assertEqual(hands_on_1.oddeven_1([1,2,6,3,7,5]),[1,3,7,5,2,6])
        self.assertEqual(hands_on_1.oddeven_1([-1,2,4,3,6,5]), [-1,3,5,2,4,6])
        self.assertNotEqual(hands_on_1.oddeven_2([1, 2, 6, 3, 7, 5]), [1, 3, 5, 7, 2, 6])

    def test_cont_maxsum(self):
        self.assertEqual(hands_on_1.sum([1,2,0,2,3,4,-1,2,4,5,7,8]),[2,4,5,7,8])
        self.assertNotEqual(hands_on_1.sum([10,20,0,-1,100,-7,50,30]), [50,30])

    def test_end_zero(self):
        self.assertEqual(hands_on_1.order([1,0,5,0,2]),[1,5,2,0,0])
        self.assertEqual(hands_on_1.order([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertNotEqual(hands_on_1.order([0, 0, 0]), [])
        self.assertRaises(TypeError,hands_on_1.order(['a','b','c']))

    def test_mrepeat_ktimes(self):
        self.assertFalse(hands_on_1.repeat_2([1,2,3,4,5,4,3],1,3))
        self.assertFalse(hands_on_1.repeat_2([1,2,3,7,2,4,4,4],2,2))
        self.assertTrue(hands_on_1.repeat_2([1,2,3,3,2,1,4,4,4],3,2))

    def test_conc_oddnum(self):
        self.assertTrue(hands_on_2.odd([1,2,5,7,9,0,20]))
        self.assertFalse(hands_on_2.odd([1,2,3,4,5,6]))

    def test_multiple(self):
        self.assertAlmostEqual(hands_on_2.miltiple(5),5,10,15,20)
        self.assertAlmostEqual(hands_on_2.miltiple(-5),-5,-10,-15,-20)

    def test_seperator(self):
        self.assertNotEqual(hands_on_2.seperator(34),'.034')
        self.assertEqual(hands_on_2.seperator(12345678), '12.345.678')

    def setUp(self):
        self.Player_1 = Player('Virat', 'Kholi', '31', 'India')
        self.Player_2 = Player('Brett', 'Lee', '40', 'Australia')
        self.Player_3 = Player('Wasim', 'Akram', '45', 'Pakistan')
        self.Player_4 = Sample()

    def tearDown(self):
        pass

    def test_Player_details(self):
        self.assertEqual(self.Player_1.Player_details("BCCI"),
                         'Virat Kholi belongs to BCCI and play Cricket for all ICC tournaments')
        self.assertNotEqual(self.Player_2.Player_details("ACC"),
                         'Brett Lee belongs to BCCI and play Cricket for all ICC tournaments')
        self.assertEqual(self.Player_3.Player_details("PCB"),
                         'Wasim Akram belongs to PCB and play Cricket for all ICC tournaments')

    def test_fullname(self):
        self.assertEqual(self.Player_1.full_name,'Virat Kholi')
        self.assertNotEqual(self.Player_2.full_name, 'BrettLee')
        self.assertEqual(self.Player_3.full_name, 'Wasim Akram')

    def test_instance(self):
        self.assertIsInstance(self.Player_1, Player)
        self.assertIsInstance(self.Player_2, Player)
        self.assertIsInstance(self.Player_3, Player)
        self.assertNotIsInstance(self.Player_4, Player)

if __name__ == '__main__':
    unittest.main()

