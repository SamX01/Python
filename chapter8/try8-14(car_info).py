def make_car(producer,model,**additional_info):
    dic={}
    dic['producer'] = producer
    dic['model'] = model
    for key,value in additional_info.items():
        dic['key'] = value
    return dic

car = make_car('subaru','outback',color = 'blue',tow_packge = True)

print(car)
