from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4


print(func_1())
print(func_2())
print(func_3())
print(func_4())

import pkg
print(pkg.URL)
# Genera error si no se tiene la importación explicita
# En el __init__.py importamos el pkg directamente

print(pkg.mod_1.func_1())

