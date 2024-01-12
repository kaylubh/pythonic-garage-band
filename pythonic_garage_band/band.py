class Musician:
  """
  
  """

  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f'My name is {self.name} and I play {self.get_instrument()}'
  
  def __repr__(self):
    return f'{self.__class__.__name__} instance. Name = {self.name}'

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
  
  def get_instrument(self):
    return 'guitar'

class Bassist(Musician):
  """
  
  """

  def __init__(self, name):
    super().__init__(name)
  
  def get_instrument(self):
    return 'bass'

class Drummer(Musician):
  """
  
  """

  def __init__(self, name):
    super().__init__(name)
  
  def get_instrument(self):
    return 'drums'
