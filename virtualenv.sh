#separate python environments for diff projects
#multiple projects and they all rely on Django or Flask but they might be using diff ver of flask or django
#now if u update one of these it will break the other packages or flow elsewhere based on versions
#so virtualenv allows us to make diff pythoin environments

#pip install virtualenv

#make first environment
virtualenv project1_env

#to activate this new environment
source project1_env/bin/activate

#check the change in your terminal prompt
#or
which python
which pip
pip list
pip install numpy
pip install pytz
pip install psutil

pip list


#export these and use in another project

pip freeze --local > requirements.txt
ls
cat requirements.txt

#get out of the python env and go back to global
deactivate
#prompt goes away
#lists global conda path
ls
#get rid of virtualenv you created fully after deactivating
rm -rf project1_env/

#use the txt file to create another

virtualenv -p /usr/bin/python py2.6env

source py2.6env/bin/activate

which python
python --version
#should say you are using 2.6.something instead of the 3v
pip install -r requirements.txt
pip list

#you could now work on your project
deactivate

which python
#it ishould now be back to v 3

#venv shoul dnot have all the project files 
#this is only to separate the dependencies you are going to use project to project

'''
                        TERMINAL DUMP
(base) ankit@Jarvis cs-python-AYNTK-programs % ./virtualenv.sh
created virtual environment CPython3.6.10.final.0-64 in 245ms
  creator CPython3Posix(dest=/Users/ankit/Documents/GitHub/cs-python-AYNTK-programs/project1_env, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/Users/ankit/Library/Application Support/virtualenv/seed-app-data/v1.0.1)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
/Users/ankit/Documents/GitHub/cs-python-AYNTK-programs/project1_env/bin/python
/Users/ankit/Documents/GitHub/cs-python-AYNTK-programs/project1_env/bin/pip
Package    Version
---------- -------
pip        20.1.1
setuptools 46.4.0
wheel      0.34.2
Collecting numpy
  Using cached numpy-1.18.4-cp36-cp36m-macosx_10_9_x86_64.whl (15.2 MB)
Installing collected packages: numpy
Successfully installed numpy-1.18.4
Collecting pytz
  Using cached pytz-2020.1-py2.py3-none-any.whl (510 kB)
Installing collected packages: pytz
Successfully installed pytz-2020.1
Processing /Users/ankit/Library/Caches/pip/wheels/a1/d9/f2/b5620c01e9b3e858c6877b1045fda5b115cf7df6490f883382/psutil-5.7.0-cp36-cp36m-macosx_10_9_x86_64.whl
Installing collected packages: psutil
Successfully installed psutil-5.7.0
Package    Version
---------- -------
numpy      1.18.4
pip        20.1.1
psutil     5.7.0
pytz       2020.1
setuptools 46.4.0
wheel      0.34.2
Intro to python.py              importmodules_stdlibrary.py     project1_env
README.md                       lists_tuples_sets.py            py2.6env
__pycache__                     loops&iterations.py             requirements.txt
conditionals&booleans.py        my_module.py                    variables and data types.py
dictionaries.py                 numeric_datatypes.py            virtualenv.sh
functions.py                    pip.sh
numpy==1.18.4
psutil==5.7.0
pytz==2020.1
Intro to python.py              importmodules_stdlibrary.py     project1_env
README.md                       lists_tuples_sets.py            py2.6env
__pycache__                     loops&iterations.py             requirements.txt
conditionals&booleans.py        my_module.py                    variables and data types.py
dictionaries.py                 numeric_datatypes.py            virtualenv.sh
functions.py                    pip.sh
created virtual environment CPython2.7.16.final.0-64 in 271ms
  creator CPython2macOsFramework(dest=/Users/ankit/Documents/GitHub/cs-python-AYNTK-programs/py2.6env, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/Users/ankit/Library/Application Support/virtualenv/seed-app-data/v1.0.1)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator
/Users/ankit/Documents/GitHub/cs-python-AYNTK-programs/py2.6env/bin/python
Python 2.7.16
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
ERROR: Could not find a version that satisfies the requirement numpy==1.18.4 (from -r requirements.txt (line 1)) (from versions: 1.3.0, 1.4.1, 1.5.0, 1.5.1, 1.6.0, 1.6.1, 1.6.2, 1.7.0, 1.7.1, 1.7.2, 1.8.0, 1.8.1, 1.8.2, 1.9.0, 1.9.1, 1.9.2, 1.9.3, 1.10.0.post2, 1.10.1, 1.10.2, 1.10.4, 1.11.0b3, 1.11.0rc1, 1.11.0rc2, 1.11.0, 1.11.1rc1, 1.11.1, 1.11.2rc1, 1.11.2, 1.11.3, 1.12.0b1, 1.12.0rc1, 1.12.0rc2, 1.12.0, 1.12.1rc1, 1.12.1, 1.13.0rc1, 1.13.0rc2, 1.13.0, 1.13.1, 1.13.3, 1.14.0rc1, 1.14.0, 1.14.1, 1.14.2, 1.14.3, 1.14.4, 1.14.5, 1.14.6, 1.15.0rc1, 1.15.0rc2, 1.15.0, 1.15.1, 1.15.2, 1.15.3, 1.15.4, 1.16.0rc1, 1.16.0rc2, 1.16.0, 1.16.1, 1.16.2, 1.16.3, 1.16.4, 1.16.5, 1.16.6)
ERROR: No matching distribution found for numpy==1.18.4 (from -r requirements.txt (line 1))
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Package    Version
---------- -------
pip        20.1.1
setuptools 44.1.0
wheel      0.34.2
/Users/ankit/miniconda3/bin/python
./virtualenv.sh: line 62: 
: command not found
'''
