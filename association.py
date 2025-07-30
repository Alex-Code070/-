import os

def merge_files_by_line_count(input_files, output_file):
    files_data = []

    for filename in input_files:
        with open(filename, encoding='utf-8') as f:
            lines = f.readlines()
            files_data.append((filename, len(lines), lines))

    files_data.sort(key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as result:
        for name, count, content in files_data:
            result.write(f"{name}\n")
            result.write(f"{count}\n")
            result.writelines(content)
            result.write('\n')

# Пример
if __name__ == '__main__':
    input_files = ['1.txt', '2.txt', '3.txt']
    output_file = 'result.txt'
    merge_files_by_line_count(input_files, output_file)
