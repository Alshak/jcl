import os
import jpype as jp
import tempfile

class Samarah(object):
    def __init__(self, agents):
        self.array_list = []
        self.agents = agents
        return None
                
    def add(self, data, params):       
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()
        SamarahAgent = jp.JClass('jcl.learning.methods.multistrategy.evosamarah.myversion.SamarahAgent')
        agent = SamarahAgent(data,params.getLearningMethodInstance())
        self.array_list.append(agent)
        

    def run(self):
        if not jp.isThreadAttachedToJVM():
            jp.attachThreadToJVM()
            
        for agent in self.agents:
            self.add(agent.get_data(), agent.get_parameters())
        
        ExClassification = jp.JClass('jcl.learning.methods.multistrategy.evosamarah.myversion.ExClassification')
        SetOfSamarahAgents = jp.JClass('jcl.learning.methods.multistrategy.evosamarah.myversion.SetOfSamarahAgents')
        ArrayList = jp.JClass('java.util.ArrayList')
        my_list = ArrayList()
        for agent in self.array_list:
            my_list.add(agent)
        samarah_set = SetOfSamarahAgents(my_list)
        exc = ExClassification(samarah_set)
        exc.classify()
        return ''
        