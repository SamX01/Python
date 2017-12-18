##def build_person(first_name, last_name, age=''):
##    """"retrun a dictionary which contains info of one person"""
##    person = {'first_name':first_name.index(),'last_name':last_name.index()}
##    if age:
##        person['age'] = age
##    return person

##8-7
##def city_country(city_name,city_country):
##    string = '"'+city_name.title() +", "+ city_country.title()+'"'
##    return string
##
##back = city_country('chengdu','china')
##print(back)
##print(city_country('chongqing','china'))
##print(city_country('new york','america'))

def make_album(album_name,singer,song_numbers=''):
    album = {'name':album_name,'singer':singer}
    if song_numbers:
        album['song_numbers'] = song_numbers
        
    return album

album1 = make_album('山丘','李宗盛',22)
album2 = make_album('越过山丘','杨宗纬',song_numbers=3)
album3 = make_album('我真的还想再活五百年','韩庚')

print(album1)
print(album2)
print(album3)

dic = []
while True:
    isActive = input("Do you know more albums?(Y/N)")
    print("Your answer seems "+isActive)
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
            continue
        
    elif (isActive == 'N') or (isActive =='n'):
        print('What a shame')
        break
    else:
        print("Please type in Y(y) or N(n).")
        print("\n")
        continue
            
