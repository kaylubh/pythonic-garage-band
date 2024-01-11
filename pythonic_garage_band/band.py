class Musician:
  """
  
  """

  def __init__(self, name):
    self.name = name

class Band:
  """
  
  """

  members = []

  def __init__(self, name, members = None):
    self.name = name
    self.members = members or []
    
class Guitarist(Musician):
  """
  
  """

  def __init__(self, name):
    super().__init__(name)

  def __str__(self):
    return f'My name is {self.name} and I play guitar'
  
  def __repr__(self):
    return f'Guitarist instance. Name = {self.name}'
  
  def get_instrument(self):
    return 'guitar'

class Bassist(Musician):
  """
  
  """

  def __init__(self, name):
    super().__init__(name)

  def __str__(self):
    return f'My name is {self.name} and I play bass'
  
  def __repr__(self):
    return f'Bassist instance. Name = {self.name}'
  
  def get_instrument(self):
    return 'bass'

class Drummer(Musician):
  """
  
  """

  def __init__(self, name):
    super().__init__(name)

  def __str__(self):
    return f'My name is {self.name} and I play drums'
  
  def __repr__(self):
    return f'Drummer instance. Name = {self.name}'
  
  def get_instrument(self):
    return 'drums'
