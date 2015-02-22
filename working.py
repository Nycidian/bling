from bling import Ring, Chain, Clasp, Gem


test_1 = 'a', 'b', 'c'
test_2 = 'd', '|', 0
class_1 = Gem(*test_1)
class_2 = Ring('|', class_1)
class_3 = Ring('|', class_2)
class_4 = Chain('|', '-')


print(class_4.out_of('||||-|||'))




