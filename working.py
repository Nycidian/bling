from forge.ring import Ring
from forge.chain import Chain
from forge.gem import Gem

test_1 = 0, 'd', '|'
test_2 = 'd', '|', 0
class_1 = Gem(*test_1) << 1

class_2 = Ring(*test_2)

print(class_1._versions_)
print(class_1.shift)