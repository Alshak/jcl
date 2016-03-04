import jpype as jp
import tempfile
import time
import os

def find_attributes(arff_string):
    if not jp.isThreadAttachedToJVM():
        jp.attachThreadToJVM()
    
    ARFFReader = jp.JClass('jcl.io.arff.ARFFReader')   
    url = tempfile.mkdtemp()
    timenow = int(round(time.time() * 1000))
    preclassifier_url=os.path.join(url,"preclassifier%s.arff"%str(timenow))
    
    with open(preclassifier_url, 'w') as f:
        f.write(arff_string)    
    reader = ARFFReader(preclassifier_url)
    reader.parse()
    
    dataset = reader.getData()
    return dataset.getAttributesNames()