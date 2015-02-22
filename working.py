from bling import Ring, Chain, Clasp, Gem


test_1 = 'b', 'c'
test_2 = 'd', '|', 0
class_1 = Gem(*test_1)
class_2 = Ring('a', class_1)
class_3 = Chain('d', class_2)

print(class_3)

print(hash('a'))
print(hash('b'))
print(hash('c'))
print(hash('d'))

print(max([hash('a'), hash('b'), hash('c'), hash('d')]))

print(hash(frozenset(['dabc', 'dcba'])))