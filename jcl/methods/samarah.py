import os
import jpype as jp
import tempfile
import time

class Samarah(object):
    def __init__(self, agents):
        self.array_list = []
        self.agents_python = agents
        return None      

    def run(self):
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()
            
        HybridClassification = jp.JClass('jcl.learning.methods.multistrategy.samarah.HybridClassification')
        self.hybrid_classification = HybridClassification()
        
        for agent_python in self.agents_python:
            self.hybrid_classification.addAgent(agent_python.get_parameters(), agent_python.get_data())

        self.hybrid_classification.classify()
        clusRes = self.hybrid_classification.getClusteringResult()
        
        temp_file_url = tempfile.mkdtemp()
        timenow = int(round(time.time() * 1000))
        output_file_url=os.path.join(temp_file_url,"result%s.arff"%str(timenow))
        
        ARFFWriter = jp.JClass('jcl.io.arff.ARFFWriter')   
        writer = ARFFWriter(output_file_url,clusRes)
        writer.write()

        with open(output_file_url, 'r') as f:
            output_file = f.read()
        
        return output_file
    
    def get_parameters(self):
        raise NotImplementedError()
    
    def get_data(self):
        return self.agents_python[0].get_data()
    
    def get_method(self):
        raise NotImplementedError()