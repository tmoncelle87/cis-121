from animal import Animal


class Dog(Animal):

  def __init__(self, name, color, eye_color, height, length, weight):
    super().__init__(name)
    self.color = color
    self.eye_color = eye_color
    self.height = height
    self.length = length
    self.weight = weight

  def sit(self):
    print("I'm sitting!")

  def laydown(self):
    print("I'm laying down!")

  def __str__(self):
    print("\n====Dog Info====")
    print(f"Name: {self.name}")
    print(f"Color: {self.color}")
    print(f"Eye Color: {self.eye_color}")
    print(f"Height: {self.height}")
    print(f"Length: {self.length}")
    print(f"Weight: {self.weight}")

    return ""


#
#
#
