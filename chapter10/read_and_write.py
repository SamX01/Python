#file_name = 'raw_input.txt'
file_name = '10million_pi.txt'

with open(file_name) as file_object:
##    contents = file_object.read()
##    print(contents)
    lines = file_object.readlines()

num_str =''
for line in lines:
    line = line.rstrip() #去除'\n'，即去除空行
    line = line.replace(' ','') #去除空格
    num_str += line

print(num_str[:100])

new_file_name = 'clean_10million_pi.txt'
with open(new_file_name,'w') as file_object:
    file_object.write(num_str[:1000])


with open(new_file_name,'a') as f2:
    f2.write('\n21\n\n12')
