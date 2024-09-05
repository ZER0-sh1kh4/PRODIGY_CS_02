try:
    
    path = r'C:\Users\SHOBHIT\Downloads\lol\ghost-render-magenta-abstraction-cgi-smoke-abstract-49932.png'
    action = input("Do you want to encrypt or decrypt the image? (E/D): ").strip().upper()
    key = int(input('Enter Key for the operation: '))
    
    
    print('The path of file : ', path)
    print('Key for the operation: ', key)
    
    with open(path, 'rb') as fin:
        image = fin.read()

    image = bytearray(image)

    
    for index, values in enumerate(image):
        image[index] = values ^ key
    with open(path, 'wb') as fout:
        fout.write(image)
    
    if action == 'E':
        print('Encryption Done...')
    elif action == 'D':
        print('Decryption Done...')
    else:
        print('Invalid choice. Please choose either "E" for encryption or "D" for decryption.')

except Exception as e:
    print('Error caught:', e.__class__.__name__, "-", str(e))
