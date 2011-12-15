'''

>>> def dobro(n=1):
...     """Devolve duas vezes n"""
...     return n*2
>>> dobro(21)
42
>>> dobro('X')
'XX'
>>> dobro([10, 20, 30])
[10, 20, 30, 10, 20, 30]
>>> dobro #doctest: +ELLIPSIS
<function dobro at 0x...>
>>> type(dobro)
<type 'function'>
>>> x2 = dobro
>>> x2(1234)
2468
>>> map(dobro, [11, 22, 33])
[22, 44, 66]
>>> dobro.__doc__
'Devolve duas vezes n'
>>> dobro.__name__
'dobro'
>>> def fat(n=5):
...     if n < 2: return 1
...     return n*fat(n-1)
>>> fat(10)
3628800
>>> atr_func = ['__closure__','__code__', '__defaults__', '__dict__', '__name__']
>>> for atr in atr_func: #doctest:+ELLIPSIS
...     print '%14s : %r' % (atr, getattr(fat, atr))
   __closure__ : None
      __code__ : <code object fat at 0x...>
  __defaults__ : (5,)
      __dict__ : {}
      __name__ : 'fat'
>>> atr_co = [a for a in dir(fat.__code__) if a.startswith('co_')]
>>> for atr in atr_co: #doctest:+ELLIPSIS
...     print '%14s : %r' % (atr, getattr(fat.__code__, atr))
   co_argcount : 1
   co_cellvars : ()
       co_code : '|\\x00\\x00d\\x01\\x00k\\x00...S'
     co_consts : (None, 2, 1)
   co_filename : '<doctest funcao_1a_classe[...]>'
co_firstlineno : 1
      co_flags : 67
   co_freevars : ()
     co_lnotab : '\\x00\\x01\\x0c\\x00\\x04\\x01'
       co_name : 'fat'
      co_names : ('fat',)
    co_nlocals : 1
  co_stacksize : 4
   co_varnames : ('n',)
>>> from dis import dis
>>> dis(fat.__code__.co_code) #doctest: +NORMALIZE_WHITESPACE
          0 LOAD_FAST           0 (0)
          3 LOAD_CONST          1 (1)
          6 COMPARE_OP          0 (<)
          9 POP_JUMP_IF_FALSE    16
         12 LOAD_CONST          2 (2)
         15 RETURN_VALUE
    >>   16 LOAD_FAST           0 (0)
         19 LOAD_GLOBAL         0 (0)
         22 LOAD_FAST           0 (0)
         25 LOAD_CONST          2 (2)
         28 BINARY_SUBTRACT
         29 CALL_FUNCTION       1
         32 BINARY_MULTIPLY
         33 RETURN_VALUE




>>> tf = type(dobro)
>>> fonte = """def triplo(n): return n*3"""
>>> bytecode = compile(fonte,'__teste__', 'exec')
>>> triplo = tf(bytecode, globals())
'''