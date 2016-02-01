import logging 

class BlindFail(Exception):
  pass



class BasicSql(object):

  def __init__(self):
    pass

  def int_eq(self, a, b):
    return "({0}={1})".format(a, b)
  
  def int_gt(self, a, b):
    return "({0}>{1})".format(a, b)

  def str_at(self,s,p):
    return "(mid(({}),{},1))".format(s,p)

  def char_ord(self,s):
    return "(CHR({0}))".format(s)

  def str_len(self,s):
    return "(LENGTH({0}))".foramt(s)

  def str_hex(self, s):
    return "(HEX({0}))".format(s)
 



class BlindMachine(object):
  engine = None

  def __init__(self, engine=None):
    if engine is None:
      self.engine = BasicSql()
    else:
      self.engine = engine


  def make_query(self):
    pass


  def guess_int(self, query='(SELECT 1)',min_val=0,max_val=0xFFFF):
    while True:
      dif = max_val - min_val
      if dif < 5:
        for i in range(dif):
          cur = min_val + i
          q = "( {0} = {1} )".format(query, cur)
          r = self.make_query(self.engine.int_eq(query, cur))
          if r:
            return cur
        raise BlindFail("Guess int fail - out of range")
      else:
        mid = (min_val + max_val) / 2
        r = self.make_query(self.engine.int_gt(query, mid))
        if r:
          min_val = mid
        else:
          max_val = mid

  def guess_str_len(self, query='(select 1)'):
    return self.guess_int(self.engine.str_len(query), 0, 500)

  def guess_char(self, query="(select 'x')",lo=20,hi=128):
    return gess_int(self.engine.char_ord(query),lo,hi)

  def guess_str(self, query='(select 1)', max_length=None):
    r = ''
    if max_length is None:
      max_length = self.guess_str_len(query)
    for i in range(max_length):
      c = self.guess_char(self.engine.str_at(query, i))
      r += chr(c)
    return r    
  



