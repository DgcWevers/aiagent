from functions.get_files_info import get_files_info

# Current directory
print('Result for current directory:')
result = get_files_info("calculator", '.')
if 'Error' in result: print(f'\t{result}')
else: print(result)

# Pkg directory
print("Result for 'pkg' directory:")
result = get_files_info("calculator", 'pkg')
if 'Error' in result: print(f'\t{result}')
else: print(result)

# /bin directory
print("Result for '/bin' directory:")
result = get_files_info("calculator", '/bin')
if 'Error' in result: print(f'\t{result}')
else: print(result)

# '../' directory
print("Result for '../' directory:")
result = get_files_info("calculator", '../')
if 'Error' in result: print(f'\t{result}')
else: print(result)