import jpype as jp
from monostrategy import Monostrategy

class Cobweb(Monostrategy):
    def __init__(self,arff_string,weights,acuity,mapi,max_depth,nb_steps,minimal_card):
        Monostrategy.__init__(self,arff_string,weights)
        self.acuity = float(acuity)
        self.mapi = float(mapi)
        self.max_depth = int(max_depth)
        self.nb_steps = int(nb_steps)
        self.minimal_card = int(minimal_card)
        
    def get_method(self):
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()
            
        ClassifierCobweb = jp.JClass('jcl.learning.methods.monostrategy.cobweb.ClassifierCobweb')
        return ClassifierCobweb(self.param, None)
        
        
    def get_parameters(self):
        Monostrategy.get_parameters(self)            
        ParametersCobweb = jp.JClass('jcl.learning.methods.monostrategy.cobweb.ParametersCobweb')
        return ParametersCobweb(self.acuity,self.mapi,self.max_depth, self.nb_steps, self.minimal_card, self.global_weights);