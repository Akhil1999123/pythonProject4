import os
print(os.getcwd())
#print(os.mkdir('hcl_t'))
print(os.listdir(os.getcwd()))
print(os.listdir('hcl_t'))
for file in os.listdir('hcl_t'):
    if file.endswith('.py'):
        print(file)