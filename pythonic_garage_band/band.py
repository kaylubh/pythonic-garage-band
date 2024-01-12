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

  instances = []

  def __init__(self, name, members = None):
    self.name = name
    self.members = members or []
    self.instances.append(self)

  def __str__(self):
    return self.name
  
  def __repr__(self):
    return f'{self.__class__.__name__} instance. Name = {self.name}'

  def play_solos(self):
    return [member.play_solo() for member in self.members]
  
  @classmethod
  def to_list(cls):
    return cls.instances
    
class Guitarist(Musician):
  """
  
  """

  def __init__(self, name):
    super().__init__(name)
  
  def get_instrument(self):
    return 'guitar'
  
  def play_solo(self):
    return 'face melting guitar solo'

class Bassist(Musician):
  """
  
  """

  def __init__(self, name):
    super().__init__(name)
  
  def get_instrument(self):
    return 'bass'
  
  def play_solo(self):
    return 'bom bom buh bom'

class Drummer(Musician):
  """
  
  """

  def __init__(self, name):
    super().__init__(name)
  
  def get_instrument(self):
    return 'drums'
  
  def play_solo(self):
    return 'rattle boom crash'
