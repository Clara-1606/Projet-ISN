
from distutils.core import setup
import py2exe
 
Mydata_files = [('images', ['D:\PythonVesval\Python\images\mastermind.gif'])]
 
setup(
    console=['Mastermind.py'],
    data_files = Mydata_files,
    options={
             "py2exe":{
                        "unbuffered": True,
                        "optimize": 2,
                        "excludes": ["email"]
             }
       }
)