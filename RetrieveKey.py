obj1= {'a':{'b':{'c':'d'}}}
obj2 = {'x':{'y':{'z':'a'}}}
def retrievekey(obj,key): 
    try:
        c= key.count('/')
        if c == 0:
            print(key," subkey is: ",obj[key])
        elif c == 1:
            keylist = key.split('/')
            print(key , " subkey is: ", obj[keylist[0]][keylist[1]])
        elif c == 2:
            keylist = key.split('/')
            print(key , " subkey is: ", obj[keylist[0]][keylist[1]][keylist[2]])
        else:
            print("Invalid entry in calling retrievekey function, please check")
    except:
        print("An exception occurred! May be you have not entered the correct keys, please check")        
    
retrievekey(obj1,'a') 
retrievekey(obj1,'a/b')  
retrievekey(obj1,'a/b/c') 
retrievekey(obj2,'x/y/c')  
retrievekey(obj2,'x/y/z')

  