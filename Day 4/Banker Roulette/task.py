import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
list_length=len(friends)-1
The_chosen = random.randint(0, list_length)
print(friends[The_chosen])