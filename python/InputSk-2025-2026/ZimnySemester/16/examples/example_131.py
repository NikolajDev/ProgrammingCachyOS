class RAMError(Exception): pass

class Registers:
    def __init__(self, num_bytes, maximum):
        self._mem = []
        ...

    def get(self, address):
        return 0

    def set(self, address, value):
        ...

    def __repr__(self):
        return 'reg: ...'

class RAM:
    def __init__(self, program):
        ...

    def start(self, inp='', num_bytes=2, maximum=1000):
        self.reg = Registers(num_bytes, maximum)
        ...

    def __repr__(self):
        return repr(self.reg)

    def instruction(self, pc, instr, *param):
        ...
        return pc + 1