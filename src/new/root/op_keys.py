import operator

op_keys = {
    # Operadores de Comparação
    "==": operator.eq,
    "!=": operator.ne,
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge,
    "is": operator.is_,
    "is not": operator.is_not,
    
    # Operadores Aritméticos
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "@": operator.matmul,  # Multiplicação de matrizes
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod,
    "**": operator.pow,
    
    # Operadores Bitwise (Bit a Bit)
    "&": operator.and_,
    "|": operator.or_,
    "^": operator.xor,
    "~": operator.invert,
    "<<": operator.lshift,
    ">>": operator.rshift
}