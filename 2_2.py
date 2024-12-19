#Take input from one file and place it to another file. Use ASCII value for comparison. Rotate the content in the copied file Design one hash function to check the integrity of the two files
import hashlib
def rotate_char(c,shift):
    return chr((ord(c)+shift)%256) #rotated within extended ASCII range
def read_file(filename):
    with open(filename,'r') as file:
        return file.read()
def write_file(filename,content):
    with open(filename,'w') as file:
        file.write(content)
def rotate_content(content,shift):
    rotated=''.join(rotate_char(c,shift)for c in content)
    return rotated
def hash_file_content(content):
    sha256_hash=hashlib.sha256()
    sha256_hash.update(content.encode('utf-8')) # Hash the content after encoding to bytes
    return sha256_hash.hexdigest()
def copy_and_rotate(input_file,output_file,shift):
    original_content=read_file(input_file)
    rotated_content=rotate_content(original_content,shift)
    write_file(output_file,rotated_content)

    original_hash=hash_file_content(original_content)
    rotated_hash=hash_file_content(rotated_content)
    return original_hash,rotated_hash
#example
input_filename = 'input.txt'
output_filename = 'output.txt'
shift_value = 3  # Rotate characters by 3 ASCII values
# Perform the copy, rotate, and hash integrity check
original_hash, rotated_hash = copy_and_rotate(input_filename, output_filename, shift_value)
print(f"Original File Hash (SHA-256): {original_hash}")
print(f"Rotated File Hash (SHA-256): {rotated_hash}")

if(original_hash==rotated_hash):
    print("the files are identical")
else:
    print("the files aren't identical ")

