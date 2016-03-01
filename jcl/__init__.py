import jpype as jp
from os.path import join, normpath, dirname

BASE = normpath(dirname(__file__))
JARDIR = normpath(join(BASE, 'java_src'))
CLASSPATH = '-Djava.ext.dirs=' + JARDIR # + '-Djava.class.path=' + JARDIR
if not jp.isJVMStarted():
    jp.startJVM(jp.getDefaultJVMPath(), CLASSPATH, '-Djava.awt.headless=true')