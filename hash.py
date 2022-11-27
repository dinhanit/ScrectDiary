# def hash(data):
#     NewData =''
#     key = 0
#     for word in data:
#         key = ord(word)+23
#         if key > 126:
#             key=key - 126 + 31
#         NewData = NewData+chr(key)
#     return NewData

# def UnHash(data):
#     NewData =''
#     key = 0
#     for word in data:
#         key = ord(word)-23
#         if key<32:
#             key=key+126 - 31
#         NewData = NewData+chr(key)
#     return NewData

# # content ='Udinhan|P232323'
# # print(hash(content))
# # print(UnHash(hash(content)))
# # # print(UnHash(hash(content)))
# # file = open('check.txt','w')
# # file.write(hash(content))
# # print(file.read())
# print(4,chr(10),3)








from colored import fg
blue= fg('blue')
print (color + 'Hello World !!!')
