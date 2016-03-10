from django.shortcuts import render
from jcl.methods.create_weights import find_attributes

def jcl_create_attributes_weights(request,input_dict,output_dict,widget):
    arff_file = input_dict['arff_file']
    attributes_list = find_attributes(arff_file)
    idx_attr_list = []
    for i,attribute in enumerate(attributes_list):
        idx_attr_list.append([i,attribute])
    return render(request, 'interactions/jcl_create_attributes_weights.html',{'widget':widget,'attributes_list':attributes_list})