import jpype as jp
from monostrategy import Monostrategy

class Som(Monostrategy):
    def __init__(self,arff_string,nb_steps,height,width,epsilon):
        Monostrategy.__init__(self, None)
        self.dataset = None

        self.arff_string = arff_string
        self.nb_steps = int(nb_steps)
        self.height = int(height)
        self.width = int(width)
        self.epsilon = float(epsilon)
        
    def get_method(self):
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()
            
        ClassifierSOM = jp.JClass('jcl.learning.methods.monostrategy.som.ClassifierSOM')
        return ClassifierSOM(self.param, None)
    
    def get_parameters(self):
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()
            
        ParametersSOM = jp.JClass('jcl.learning.methods.monostrategy.som.ParametersSOM')
        GlobalWeights = jp.JClass('jcl.weights.GlobalWeights')
        self.dataset = self.get_data()
        return ParametersSOM(self.width, self.height, self.nb_steps,self.epsilon, GlobalWeights(self.dataset));