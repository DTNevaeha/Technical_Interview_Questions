import os

# Calculate file sizes in bytes, KB, MB

def file_info(file_path):
    return os.path.getsize(file_path)

result = file_info('iterator_generator.py')
print(f'The file size is {result} bytes')
print(f'The file size is {result/1024} KB')
print(f'The file size is {result/1024/1024} MB')
