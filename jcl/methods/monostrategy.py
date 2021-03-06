'''
Created on 29 feb. 2016

@author: alain
'''
import os
import jpype as jp
import tempfile
import time

class Monostrategy(object):
    def __init__(self,arff_string,weights):
        self.arff_string = arff_string
        self.weights = weights        
        self.global_weights = None
        self.dataset = None
        return None
    
    def run(self):
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()
            
        self.param = self.get_parameters()
        
        ARFFWriter = jp.JClass('jcl.io.arff.ARFFWriter')   
        method = self.get_method()
        result = method.learn(self.dataset) 
        clusRes = result.classify(self.dataset)

        temp_file_url = tempfile.mkdtemp()
        timenow = int(round(time.time() * 1000))
        output_file_url=os.path.join(temp_file_url,"result%s.arff"%str(timenow))

        writer = ARFFWriter(output_file_url,clusRes)
        writer.write()

        with open(output_file_url, 'r') as f:
            output_file = f.read()
        
        return output_file

    def get_method(self):
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()
        return None
                
    def get_parameters(self):
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()

        self.dataset = self.get_data()

        weights = jp.JClass('jcl.weights.Weights')(len(self.dataset.getAttributesNames()))
        
        if self.weights != None:
            for (att,wgt) in self.weights:
                weights.setWeight(int(att),float(wgt))
        self.global_weights = jp.JClass('jcl.weights.GlobalWeights')(weights)        
        return None

    def get_data(self):
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()
            
        if self.dataset == None:
            ARFFReader = jp.JClass('jcl.io.arff.ARFFReader')   
            url = tempfile.mkdtemp()
            timenow = int(round(time.time() * 1000))
            preclassifier_url=os.path.join(url,"preclassifier%s.arff"%str(timenow))
            
            with open(preclassifier_url, 'w') as f:
                f.write(self.arff_string)    
            reader = ARFFReader(preclassifier_url)
            reader.parse()
            self.dataset = reader.getData()
        return self.dataset
        