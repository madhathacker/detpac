import pefile
pe = pefile.PE("7z.exe", fast_load=False)
print(pe.dump_info())

for section in pe.sections:
	print(section.Name)
