import jpype as jp
from monostrategy import Monostrategy

class Kmeans(Monostrategy):
    def __init__(self,arff_string,nb_seeds,nb_steps):
        Monostrategy.__init__(self, None)
        self.dataset = None
        self.arff_string = arff_string
        self.nb_seeds = int(nb_seeds)
        self.nb_steps = int(nb_steps)
        
    def get_method(self):
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()
            
        ClassifierKmeans = jp.JClass('jcl.learning.methods.monostrategy.kmeans.ClassifierKmeans')
        return ClassifierKmeans(self.param, None)
    
    def get_parameters(self):
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()
            
        ParametersKmeans = jp.JClass('jcl.learning.methods.monostrategy.kmeans.ParametersKmeans')
        GlobalWeights = jp.JClass('jcl.weights.GlobalWeights')
        self.dataset = self.get_data()        
        return ParametersKmeans(self.nb_seeds, self.nb_steps, GlobalWeights(self.dataset));
