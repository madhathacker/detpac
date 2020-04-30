import pefile
pe = pefile.PE("calc.exe", fast_load=False)
print(pe.dump_info())
