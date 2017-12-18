isActive ='n'

if (isActive == 'Y') or (isActive =='y'):
    album_name = input('The name of the album is: ')
    album_singer = input("The singer's name is: ")
    flag2 = input("Do you know how many songs are in this album?(Y/N)")
    if (flag2 == 'Y') or (flag2=='y'):
        album_song_number = input("The number of songs in this album is:")
        dic.append(make_album(album_name,album_singer,album_song_number))
        print(dic[-1])
    elif (flag2 == 'N') or (flag2=='n'):
        print("That's ok")
        dic.append(make_album(album_name,album_singer))
        print(dic[-1])
    else:
        print('Please type in Y(y) or N(n).')
 
elif (isActive == 'N') or (isActive =='n'):
    print('What a shame')
   
else:
    print("Please type in Y(y) or N(n).")
   
            
