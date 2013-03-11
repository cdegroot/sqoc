from myhdl import Cosimulation
from myhdl import Simulation, Signal, intbv, join, delay
import unittest

def mainModule(clock, reset, pc):
    return Cosimulation("vvp -m myhdl out/a.out", clock=clock, reset=reset, pc=pc)

class MainTestBench(unittest.TestCase):


    def testReset(self):
        def clockGen(clk):
            while 1:
                clk.next = 1 ^ clk
                yield delay(1)

        def check(reset, clock, pc):
            pc.next = 25
            yield delay(10)
            reset.next = 1
            yield delay(10)
            self.assertEquals(pc, 0)

        reset = Signal(intbv(0))
        clock = Signal(intbv(0))
        pc = Signal(intbv(0)[8:])
        main = mainModule(clock, reset, pc)
        sim = Simulation(main, clockGen(clock), check(reset,clock,pc))
        sim.run(duration=100, quiet=0)
        print "Test done"
       
if __name__ == '__main__':
    unittest.main()
