from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["pickachu", "Squirle","charmander"])
table.add_column("Type", ["Electric", "water", "fire"])
table.align="l"
print(table)