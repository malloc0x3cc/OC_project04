class Player():
	def __init__(self, name, age) -> None:
		self.name = name
		self.age = age

test_player = Player(name="Mac", age=24)
print(test_player)
print(test_player.name)
print(test_player.age)