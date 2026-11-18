# greeter.py
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}!")

g1 = Greeter("zeya222")
g1.greet()
