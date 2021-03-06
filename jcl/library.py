from jcl.methods.kmeans import Kmeans
from jcl.methods.cobweb import Cobweb
from jcl.methods.som import Som
from jcl.methods.samarah import Samarah

def jcl_kmeans(input_dict):
    weights = input_dict['weights']
    arff_file = input_dict['arff_file']
    nb_seeds = input_dict['nb_seeds']
    nb_steps = input_dict['nb_steps']
    output_dict = {}
    output_dict['agent'] =  Kmeans(arff_file,weights,nb_seeds,nb_steps)
    
    return output_dict

def jcl_cobweb(input_dict):
    weights = input_dict['weights']
    arff_file = input_dict['arff_file']
    acuity = input_dict['acuity']
    mapi = input_dict['mapi']
    max_depth = input_dict['max_depth']
    nb_steps = input_dict['nb_steps']
    minimal_card = input_dict['minimal_card']


    output_dict = {}
    output_dict['agent'] =  Cobweb(arff_file,weights,acuity,mapi,max_depth,nb_steps,minimal_card)
    
    return output_dict

def jcl_som(input_dict):
    weights = input_dict['weights']       
    arff_file = input_dict['arff_file']
    nb_steps = input_dict['nb_steps']
    height = input_dict['height']
    width = input_dict['width']
    epsilon = input_dict['epsilon']
    output_dict = {}
    output_dict['agent'] =  Som(arff_file,weights,nb_steps,height,width,epsilon)
    
    return output_dict

def jcl_samarah(input_dict):
    agents = input_dict['agents']
    samarah = Samarah(agents)
        
    output_dict = {}
    output_dict['agent'] = samarah

    return output_dict

def jcl_create_attributes_weights(input_dict):
    output_dict = {}
    return output_dict

def jcl_create_attributes_weights_finished(postdata, input_dict, output_dict):
    output_dict['weights'] = []
    for idx in range(0,int(postdata['nb_attr'][0])):
        output_dict['weights'].append([idx, float(postdata['att_%d'%idx][0])])
    return output_dict
    
def jcl_classify(input_dict):
    agt = input_dict['agent']
    
    output_dict = {}
    output_dict['arff_file'] = agt.run()
    return output_dict