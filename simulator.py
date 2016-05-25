class TM:

  def load(self, program, tape):
    self.program = program
    self.tape = tape
    self.position = 0
    self.state = 's0'

  def execute(self):
    while self.state != 'HALT':
      for line in self.program:
        if line[0] == self.state and line[1] == self.tape[self.position]:
          self.state = self.execute_line(line)
    return self.tape

  def execute_line(self, line):
    symbol_to_write = line[2]
    movement = line[3]
    next_state = line[4]
    self.tape[self.position] = symbol_to_write
    if movement == 'R':
      self.position += 1
    elif movement == 'L':
      self.position -= 1
    elif movement == None:
      self.position += 0
    return next_state
