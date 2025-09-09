'''
                                                                METODOS MAGICOS DUNDER

| Operador / Función              | Método especial                                                      | Ejemplo de uso                        |
| ------------------------------- | -------------------------------------------------------------------- | ------------------------------------- |
| **Aritméticos**                 |                                                                      |                                       |
| `+` (suma)                      | `__add__(self, other)`                                               | `a + b`                               |
| `-` (resta)                     | `__sub__(self, other)`                                               | `a - b`                               |
| `*` (multiplicación)            | `__mul__(self, other)`                                               | `a * b`                               |
| `/` (división)                  | `__truediv__(self, other)`                                           | `a / b`                               |
| `//` (división entera)          | `__floordiv__(self, other)`                                          | `a // b`                              |
| `%` (módulo)                    | `__mod__(self, other)`                                               | `a % b`                               |
| `**` (potencia)                 | `__pow__(self, other)`                                               | `a ** b`                              |
| `+=`                            | `__iadd__(self, other)`                                              | `a += b`                              |
| `-=`                            | `__isub__(self, other)`                                              | `a -= b`                              |
| `*=`                            | `__imul__(self, other)`                                              | `a *= b`                              |
| `/=`                            | `__itruediv__(self, other)`                                          | `a /= b`                              |
| **Comparación**                 |                                                                      |                                       |
| `==`                            | `__eq__(self, other)`                                                | `a == b`                              |
| `!=`                            | `__ne__(self, other)`                                                | `a != b`                              |
| `<`                             | `__lt__(self, other)`                                                | `a < b`                               |
| `<=`                            | `__le__(self, other)`                                                | `a <= b`                              |
| `>`                             | `__gt__(self, other)`                                                | `a > b`                               |
| `>=`                            | `__ge__(self, other)`                                                | `a >= b`                              |
| **Conversión / Representación** |                                                                      |                                       |
| `str(obj)` / `print(obj)`       | `__str__(self)`                                                      | Texto amigable                        |
| `repr(obj)`                     | `__repr__(self)`                                                     | Representación oficial                |
| `len(obj)`                      | `__len__(self)`                                                      | Longitud                              |
| `abs(obj)`                      | `__abs__(self)`                                                      | Valor absoluto                        |
| `int(obj)`                      | `__int__(self)`                                                      | Conversión a int                      |
| `float(obj)`                    | `__float__(self)`                                                    | Conversión a float                    |
| **Acceso a elementos**          |                                                                      |                                       |
| `obj[i]`                        | `__getitem__(self, i)`                                               | Acceso a índice                       |
| `obj[i] = x`                    | `__setitem__(self, i, x)`                                            | Asignación                            |
| `del obj[i]`                    | `__delitem__(self, i)`                                               | Eliminación                           |
| `in`                            | `__contains__(self, item)`                                           | `x in obj`                            |
| **Otros útiles**                |                                                                      |                                       |
| `callable(obj)`                 | `__call__(self, *args)`                                              | Permite llamar al objeto como función |
| `with`                          | `__enter__(self)` y `__exit__(self, exc_type, exc_value, traceback)` | Manejo de contexto                    |

'''

'''                                 Tabla de Operadores Compuestos en Python

| Operador compuesto | Equivalente a | Descripción                            |     |                       |
| ------------------ | ------------- | -------------------------------------- | --- | --------------------- |
| `a += b`           | `a = a + b`   | Suma y asigna                          |     |                       |
| `a -= b`           | `a = a - b`   | Resta y asigna                         |     |                       |
| `a *= b`           | `a = a * b`   | Multiplica y asigna                    |     |                       |
| `a /= b`           | `a = a / b`   | Divide y asigna (resultado float)      |     |                       |
| `a //= b`          | `a = a // b`  | División entera y asigna               |     |                       |
| `a %= b`           | `a = a % b`   | Módulo (residuo) y asigna              |     |                       |
| `a **= b`          | `a = a ** b`  | Potencia y asigna                      |     |                       |
| `a &= b`           | `a = a & b`   | AND bit a bit y asigna                 |     |                       |
| \`a                | = b\`         | \`a = a                                | b\` | OR bit a bit y asigna |
| `a ^= b`           | `a = a ^ b`   | XOR bit a bit y asigna                 |     |                       |
| `a >>= b`          | `a = a >> b`  | Desplazamiento a la derecha y asigna   |     |                       |
| `a <<= b`          | `a = a << b`  | Desplazamiento a la izquierda y asigna |     |                       |

'''