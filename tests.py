import unittest
from simulator import TM

class TMSimulatorTest(unittest.TestCase):

  def test_write_a_0_on_tape(self):
    tm = TM()
    s0 = ('s0', None, 0, 'R', 's1')
    s1 = ('s1', None, 0, None, 'HALT')
    program = [s0,s1]
    tm.load(program, [None]*100)
    self.assertEqual(0, tm.execute()[0])
    self.assertEqual('HALT', tm.state)

  def test_add_1(self):
    tm = TM()
    l0 = ('s0', None, 1, None, 'HALT')
    l1 = ('s0', 0   , 0, 'R' , 's0')
    l2 = ('s0', 1   , 1, 'R' , 's0')
    program = [l0,l1,l2]
    tm.load(program, [1,0,None])
    self.assertEqual([1,0,1], tm.execute())
    tm.load(program, [None])
    self.assertEqual([1], tm.execute())

  def test_double_ones(self):
    tm = TM()
    l0  = ('s0', 1, 0, 'R', 's1')# cancello e scorrimento a dx (1)
    l1 =  ('s1', 1, 1, 'R', 's1')# scorrimento a dx (1)
    l2  = ('s1', 0, 0, 'R', 's2')#salta gap
    l3  = ('s2', 0, 1, 'R', 's3')#scrivi doppio numero
    l4  = ('s2', 1, 1, 'R', 's2')#scorrimento a dx (2)
    l5  = ('s3', 0, 1, 'R', 's4')#scrivi doppio numero
    l6  = ('s4', 0, 0, 'L', 's5')#mi giro
    l7  = ('s5', 1, 1, 'L', 's5')#scorrimento a sx(1)
    l8  = ('s5', 0, 0, 'L', 's6')#salta gap
    l9  = ('s6', 0, 0,None, 'HALT')#fine
    l10  = ('s6', 1, 1, 'L', 's7')
    l11 = ('s7', 1, 1, 'L', 's7')#scorrimento a sx(2)
    l12 = ('s7', 0, 0, 'R', 's0')
    program = [l0,l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    tm.load(program, [1,1,1,0,0,0,0,0,0,0,0])
    self.assertEqual([0,0,0,0,1,1,1,1,1,1,0], tm.execute())
    tm.load(program, [1,1,1,1,0,0,0,0,0,0,0,0,0,0])
    self.assertEqual([0,0,0,0,0,1,1,1,1,1,1,1,1,0], tm.execute())
