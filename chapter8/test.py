##unprinted_designs = ['iphone case','robot pendant','dedecahedron']
##completed_models = []
##
##def print_models(unprinted_designs,completed_models):
##    while unprinted_designs:
##        current_design = unprinted_designs.pop()
##
##        print("Printing model:"+current_design)
##        completed_models.append(current_design)
##
##def show_completed_models(completed_models):
##    print("\nThe following models have been printed:")
##    for completed_model in completed_models:
##        print(completed_model)
##
##print_models(unprinted_designs[:],completed_models)
##show_completed_models(completed_models)


producer='subaru'
model = 'outback'
additional_info = {'color':'blue','tow_packge':True,}
dic = {}
dic['producer'] = producer
dic['model'] = model

for key,value in additional_info.items():
    dic['key'] = value
