from django.shortcuts import render

def jcl_filter_integers(request,input_dict,output_dict,widget):
    return render(request, 'interactions/jcl_filter_integers.html',{'widget':widget,'intList':input_dict['intList']})

def jcl_create_attributes_weights(request,input_dict,output_dict,widget):
    return render(request, 'interactions/jcl_create_attributes_weights.html',{'widget':widget})