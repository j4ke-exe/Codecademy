class Pokemon:
  def __init__(self, name, level=10, type):
    self.name = name
    self.level = level
    self.health = level * 5
    self.max_health = level * 5
    self.type = type
    self.is_knocked_out = False
