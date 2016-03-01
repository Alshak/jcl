import jpype as jp
from monostrategy import Monostrategy

class Cobweb(Monostrategy):
    def __init__(self,arff_string,acuity,mapi,max_depth,nb_steps,minimal_card):
        Monostrategy.__init__(self, None)
        self.dataset = None
        self.arff_string = arff_string
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
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()
            
        ParametersCobweb = jp.JClass('jcl.learning.methods.monostrategy.cobweb.ParametersCobweb')
        GlobalWeights = jp.JClass('jcl.weights.GlobalWeights')
        self.dataset = self.get_data()
        return ParametersCobweb(self.acuity,self.mapi,self.max_depth, self.nb_steps, self.minimal_card, GlobalWeights(self.dataset));