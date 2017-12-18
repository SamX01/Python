def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for num in range(len(magicians)):
        magicians[num] = "the great "+magicians[num]
    show_magicians(magicians)

magicians = ['famous Mr.A','tedious Mrs.B','talented Mr.C']
     
make_great(magicians[:])
show_magicians(magicians)
