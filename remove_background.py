from rembg import remove
from PIL import Image
import os

path = os.getcwd()
input_path = path+'\\people3\\'
output_path = path+'\\people3_out\\'

print(input_path)
print(output_path)

file_list = os.listdir(input_path)

for filename in file_list:
    print(filename)
    input = Image.open(input_path+filename)
    output = remove(input)
    output.save(output_path+filename)
