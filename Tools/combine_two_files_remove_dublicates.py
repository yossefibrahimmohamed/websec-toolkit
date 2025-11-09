def combine_files(file_one, file_two, output_file):
    try:

        with open(file_one, 'r') as f1:
            lines1 = f1.readlines()
        with open(file_two, 'r') as f2:
            lines2 = f2.readlines()

        combined_lines = lines1 + lines2
        unique_lines = sorted(set(line.strip() for line in combined_lines if line.strip()))

        with open(output_file, 'w') as out:
            for line in unique_lines:
                out.write(line + '\n')

        print(f"[+] Combined unique lines written to '{output_file}'")

    except Exception as e:
        print(f"[!] Error: {e}")


file1 = 'file_one.txt'
file2 = 'file_two.txt'
output_file = 'output_file.txt'

combine_files(file1, file2, output_file)
