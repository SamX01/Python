# Programming Python
# 6-5 Rivers
# Xiang Peng
# 2017-12-1

river_dic = {}
river_dic['nile'] = 'egypt'
river_dic['long river'] = 'china'
river_dic['yellow river'] = 'china'
river_dic['mississippi'] = 'america'

##river_dic={
##    'nile':'egypt',
##    'long river':'china',
##    'yellow river':'china',
##    'mississippi river':'america',
##    }
for rivers,countries in river_dic.items():
    print("The "+rivers.title()+" runs through "+countries.title()+".")

for rivers in river_dic.keys():
    print("River Name:%s"%(rivers.title()))

print("\n")

for countries in river_dic.values():
    print("Country Name:"+countries.upper())
