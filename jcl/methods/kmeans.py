import jpype as jp
from monostrategy import Monostrategy

class Kmeans(Monostrategy):
    def __init__(self,arff_string,weights,nb_seeds,nb_steps):
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()
        
        Monostrategy.__init__(self,arff_string,weights)
        self.nb_seeds = int(nb_seeds)
        self.nb_steps = int(nb_steps)
        
    def get_method(self):
        Monostrategy.get_method(self)
        ClassifierKmeans = jp.JClass('jcl.learning.methods.monostrategy.kmeans.ClassifierKmeans')
        return ClassifierKmeans(self.param, None)
    
    def get_parameters(self):
        Monostrategy.get_parameters(self)
        ParametersKmeans = jp.JClass('jcl.learning.methods.monostrategy.kmeans.ParametersKmeans')
        return ParametersKmeans(self.nb_seeds, self.nb_steps, self.global_weights);
