message = raw_input("Enter your message")
messageArray = []
messageArray = list(message)
print messageArray
EncryptedArray = []
for x in range(len(messageArray)):
    EncryptedArray.append(chr(ord(messageArray[x])+3))
print EncryptedArray
print "".join(EncryptedArray)
