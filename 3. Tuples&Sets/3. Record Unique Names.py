n = int(input())
# ako definirame prazen set izpozlvame set()
names = set()
for _ in range(n):
    name = input()
    names.add(name)

print('\n'.join(names))
