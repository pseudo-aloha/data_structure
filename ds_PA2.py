

def hash_funciton(salted_password):
    answer = ((243 * int(salted_password[:8])) + int(salted_password[8:])) % 85767489
    return str(answer)

file_name = input('please enter the file name: ')

f = open(file_name,'r')
passwords = f.read()
f.close()
_passwords_list = passwords.split('\n')
passwords_list = []


for password in _passwords_list:
    if len(password) == 6:
        passwords_list.append(password)
        
f = open('Dictionary.txt','w')

for password in passwords_list:
    ascii_password = ''
    for i in range(6):
        ascii_password += str(ord(password[i]))
    for i in range(1000):
        f.write(password + ' ' + str('{:0>3d}'.format(i)) + ' ' + hash_funciton((str('{:0>3d}'.format(i))+str(ascii_password)))+'\n')

f.close()

hash_value = input("please input a hash value: ")

f = open('Dictionary.txt','r')
dictionary_list = f.read().split('\n')
dictionary_list.pop()
f.close()

number_of_search = 0
found = False

for line in dictionary_list:
    number_of_search += 1
    items = line.split(' ')
    if int(hash_value) == int(items[2]):
       print('the password is recovered!\n'+items[0] + ' ' + items[1] + ' ' + str(number_of_search))
       found = True
       break
if found == False:
    print('Search failed!!!')
    print('Number of entries haven been searched: ' + str(number_of_search))

f = open('results_pa2.txt','w')
f1 = open('list_pa2.txt','r')
hash_values = f1.read()
f1.close()
hash_values_list = hash_values.split('\n')
hash_values_list.pop()



# for hash_value in hash_values_list:
#     number_of_search = 0
#     found =False
#     for line in dictionary_list:
#         number_of_search += 1
#         items = line.split(' ')
#         if int(hash_value) == int(items[2]):
#             f.write(str(hash_value) + ' ' + items[0] + ' ' + items[1] + ' ' + str(number_of_search)+'\n')
#             found = True
#             break
#     if found == False:
#         f.write(str(hash_value)+' ****** *** ' + str(number_of_search)+'\n')

f.close();




    