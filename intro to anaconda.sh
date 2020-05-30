#In this Python Tutorial, we will be learning how to install Anaconda by Continuum Analytics. Anaconda is a data science platform that comes with a lot of useful features right out of the box. Many people find that installing Python through Anaconda is much easier than doing so manually. Also, we will look at Conda. Conda is Continuum's package, dependency and environment manager. Let's get started.
#(base) ankit@Jarvis cs-python-AYNTK-programs % which python
#/Users/ankit/miniconda3/bin/python
#(base) ankit@Jarvis cs-python-AYNTK-programs % python
#Python 3.6.10 |Anaconda, Inc.| (default, Mar 23 2020, 17:45:12) 
#[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
#Type "help", "copyright", "credits" or "license" for more information.
#>>> import numpy
#>>> import matplotlib

#if all this goes through just fine that means you have Anaconda installed.
#need more packages? Use pip

#Anaconda's own pkg mgr is called Conda
conda --help

#list the packages
conda list

#install something?
conda install

#alternate way
pip install

#create virtual env
conda create --name my_app flask sqlalchemy
#must have 1 pckg when u start a new env
#activate this new env
#diff for mac and windows
conda activate my_app

#check if the prompt changes, itshould

which python
#should state it is using it under the newly created env

#exit out?
conda deactivate

#use older version in a newly created env
conda create --name my_app_olderver python=2.7 flask sqlalchemy

#activate this new installed environment
conda activate my_app_olderver

conda env list

conda remove --name my_app --all


'''
(base) ankit@Jarvis cs-python-AYNTK-programs % ./intro\ to\ anaconda.sh
usage: conda [-h] [-V] command ...

conda is a tool for managing and deploying applications, environments and packages.

Options:

positional arguments:
  command
    clean        Remove unused packages and caches.
    config       Modify configuration values in .condarc. This is modeled
                 after the git config command. Writes to the user .condarc
                 file (/Users/ankit/.condarc) by default.
    create       Create a new conda environment from a list of specified
                 packages.
    help         Displays a list of available conda commands and their help
                 strings.
    info         Display information about current conda install.
    init         Initialize conda for shell interaction. [Experimental]
    install      Installs a list of packages into a specified conda
                 environment.
    list         List linked packages in a conda environment.
    package      Low-level conda package utility. (EXPERIMENTAL)
    remove       Remove a list of packages from a specified conda environment.
    uninstall    Alias for conda remove.
    run          Run an executable in a conda environment. [Experimental]
    search       Search for packages and display associated information. The
                 input is a MatchSpec, a query language for conda packages.
                 See examples below.
    update       Updates conda packages to the latest compatible version.
    upgrade      Alias for conda update.

optional arguments:
  -h, --help     Show this help message and exit.
  -V, --version  Show the conda version number and exit.

conda commands available from other packages:
  env
# packages in environment at /Users/ankit/miniconda3:
#
# Name                    Version                   Build  Channel
aioeasywebdav             2.4.0                 py36_1000    conda-forge
aiohttp                   3.6.2            py36h0b31af3_0    conda-forge
appdirs                   1.4.3                      py_1    conda-forge
async-timeout             3.0.1                   py_1000    conda-forge
attrs                     19.3.0                     py_0    conda-forge
bcrypt                    3.1.7            py36h37b9a7d_1    conda-forge
binlorry                  1.3.0a1                  pypi_0    pypi
biopython                 1.77                     pypi_0    pypi
blas                      1.0                         mkl  
boto3                     1.13.9             pyh9f0ad1d_0    conda-forge
botocore                  1.16.9             pyh9f0ad1d_0    conda-forge
brotlipy                  0.7.0           py36h37b9a7d_1000    conda-forge
ca-certificates           2020.1.1                      0  
cachetools                3.1.1                      py_0    conda-forge
certifi                   2020.4.5.1               py36_0  
cffi                      1.14.0           py36h356ff06_0    conda-forge
chardet                   3.0.4           py36h9f0ad1d_1006    conda-forge
conda                     4.8.3                    py36_0  
conda-package-handling    1.6.0            py36h37b9a7d_2    conda-forge
configargparse            1.2.3              pyh9f0ad1d_0    conda-forge
cryptography              2.9.2            py36hc9d8292_0    conda-forge
cycler                    0.10.0                   pypi_0    pypi
datrie                    0.8.2            py36h37b9a7d_0    conda-forge
decorator                 4.4.2                      py_0    conda-forge
distlib                   0.3.0                    pypi_0    pypi
docutils                  0.15.2                   py36_0    conda-forge
dropbox                   9.4.0                      py_0    conda-forge
filechunkio               1.8                        py_2    conda-forge
filelock                  3.0.12                   pypi_0    pypi
freetype                  2.10.2               h8da9a1a_0    conda-forge
ftputil                   3.4                        py_0    conda-forge
gitdb                     4.0.5                      py_0    conda-forge
gitpython                 3.1.2                      py_0    conda-forge
google-api-core           1.17.0           py36h9f0ad1d_0    conda-forge
google-auth               1.16.0                   pypi_0    pypi
google-cloud-core         1.3.0                      py_0    conda-forge
google-cloud-storage      1.28.1             pyh9f0ad1d_0    conda-forge
google-resumable-media    0.5.0                      py_1    conda-forge
googleapis-common-protos  1.51.0           py36h9f0ad1d_2    conda-forge
graphviz                  2.38.0            hc6cc99f_1011    conda-forge
idna                      2.9                        py_1    conda-forge
idna_ssl                  1.1.0                 py36_1000    conda-forge
importlib-metadata        1.6.0            py36h9f0ad1d_0    conda-forge
importlib-resources       1.5.0                    pypi_0    pypi
importlib_metadata        1.6.0                         0    conda-forge
intel-openmp              2020.1                      216  
jinja2                    2.11.2             pyh9f0ad1d_0    conda-forge
jmespath                  0.10.0             pyh9f0ad1d_0    conda-forge
jpeg                      9c                h1de35cc_1001    conda-forge
jsonschema                3.2.0            py36h9f0ad1d_1    conda-forge
kiwisolver                1.2.0                    pypi_0    pypi
libcxx                    4.0.1                hcfea43d_1  
libcxxabi                 4.0.1                hcfea43d_1  
libedit                   3.1.20181209         hb402a30_0  
libffi                    3.2.1                h475c297_4  
libgfortran               3.0.1                h93005f0_2  
libpng                    1.6.37               hbbe82c9_1    conda-forge
libtiff                   4.0.9             h79f4b77_1002    conda-forge
markupsafe                1.1.1            py36h37b9a7d_1    conda-forge
matplotlib                3.2.1                    pypi_0    pypi
minimap2                  2.17                 hfbae3c0_1    bioconda
mkl                       2019.4                      233  
mkl-service               2.3.0            py36h0b31af3_0    conda-forge
mkl_fft                   1.1.0            py36h3b54f70_1    conda-forge
mkl_random                1.1.0            py36ha771720_0  
multidict                 4.7.5            py36h37b9a7d_1    conda-forge
ncurses                   6.2                  h0a44026_0  
networkx                  2.4                        py_1    conda-forge
nodejs                    10.13.0              h0a44026_0  
numpy                     1.18.1           py36h7241aed_0  
numpy-base                1.18.1           py36h6575580_1  
openssl                   1.1.1g               h1de35cc_0  
pandas                    0.24.2           py36h86efe34_0    conda-forge
paramiko                  2.7.1                    py36_0    conda-forge
pip                       20.1               pyh9f0ad1d_0    conda-forge
porechop                  0.3.2rc0                 pypi_0    pypi
prettytable               0.7.2                      py_3    conda-forge
protobuf                  3.4.1                    py36_0    conda-forge
psutil                    5.7.0            py36h37b9a7d_1    conda-forge
pyasn1                    0.4.8                      py_0    conda-forge
pyasn1-modules            0.2.7                      py_0    conda-forge
pycosat                   0.6.3           py36h37b9a7d_1004    conda-forge
pycparser                 2.20                       py_0    conda-forge
pygraphviz                1.5             py36h37b9a7d_1002    conda-forge
pympler                   0.8                      pypi_0    pypi
pynacl                    1.3.0           py36h0b31af3_1001    conda-forge
pyopenssl                 19.1.0                     py_1    conda-forge
pyparsing                 2.4.7                    pypi_0    pypi
pyrsistent                0.16.0           py36h37b9a7d_0    conda-forge
pysftp                    0.2.9                      py_1    conda-forge
pysocks                   1.7.1            py36h9f0ad1d_1    conda-forge
python                    3.6.10               hfe9666f_1  
python-dateutil           2.8.1                      py_0    conda-forge
python-irodsclient        0.8.2                      py_0    conda-forge
python.app                1.3              py36h37b9a7d_1    conda-forge
python_abi                3.6                     1_cp36m    conda-forge
pytz                      2020.1             pyh9f0ad1d_0    conda-forge
pyyaml                    5.1.2            py36h0b31af3_0    conda-forge
rampart                   1.1.0                         0    artic-network
ratelimiter               1.2.0                 py36_1000    conda-forge
readline                  7.0                  h1de35cc_5  
requests                  2.23.0             pyh8c360ce_2    conda-forge
rsa                       4.0                        py_0    conda-forge
ruamel_yaml               0.15.87          py36h1de35cc_0  
s3transfer                0.3.3            py36h9f0ad1d_1    conda-forge
setuptools                47.1.1                   pypi_0    pypi
setuptools-scm            4.1.1                    pypi_0    pypi
six                       1.14.0                     py_1    conda-forge
smmap                     3.0.4              pyh9f0ad1d_0    conda-forge
snakemake                 5.3.0                    py36_1    bioconda
snakemake-minimal         5.3.0                    py36_1    bioconda
sqlite                    3.31.1               ha441bb4_0  
tk                        8.6.8                ha441bb4_0  
tqdm                      4.42.1                     py_0  
typing_extensions         3.7.4.2                    py_0    conda-forge
urllib3                   1.25.9                     py_0    conda-forge
virtualenv                20.0.21                  pypi_0    pypi
wheel                     0.34.2                     py_1    conda-forge
wrapt                     1.12.1           py36h37b9a7d_1    conda-forge
xmlrunner                 1.7.7                      py_0    conda-forge
xz                        5.2.4                h1de35cc_4  
yaml                      0.1.7                hc338f04_2  
yarl                      1.3.0           py36h0b31af3_1000    conda-forge
zipp                      3.1.0                      py_0    conda-forge
zlib                      1.2.11               h1de35cc_3  

CondaValueError: too few arguments, must supply command line package specs or --file

ERROR: You must give at least one requirement to install (see "pip help install")
WARNING: A conda environment already exists at '/Users/ankit/miniconda3/envs/my_app'
Remove existing environment (y/[n])? y

Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /Users/ankit/miniconda3/envs/my_app

  added / updated specs:
    - flask
    - sqlalchemy


The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/osx-64::ca-certificates-2020.1.1-0
  certifi            pkgs/main/osx-64::certifi-2020.4.5.1-py38_0
  click              pkgs/main/noarch::click-7.1.2-py_0
  flask              pkgs/main/noarch::flask-1.1.2-py_0
  itsdangerous       pkgs/main/noarch::itsdangerous-1.1.0-py_0
  jinja2             pkgs/main/noarch::jinja2-2.11.2-py_0
  libcxx             pkgs/main/osx-64::libcxx-10.0.0-1
  libedit            pkgs/main/osx-64::libedit-3.1.20181209-hb402a30_0
  libffi             pkgs/main/osx-64::libffi-3.3-h0a44026_1
  markupsafe         pkgs/main/osx-64::markupsafe-1.1.1-py38h1de35cc_0
  ncurses            pkgs/main/osx-64::ncurses-6.2-h0a44026_1
  openssl            pkgs/main/osx-64::openssl-1.1.1g-h1de35cc_0
  pip                pkgs/main/osx-64::pip-20.0.2-py38_3
  python             pkgs/main/osx-64::python-3.8.3-h26836e1_1
  readline           pkgs/main/osx-64::readline-8.0-h1de35cc_0
  setuptools         pkgs/main/osx-64::setuptools-46.4.0-py38_0
  sqlalchemy         pkgs/main/osx-64::sqlalchemy-1.3.17-py38haf1e3a3_0
  sqlite             pkgs/main/osx-64::sqlite-3.31.1-h5c1f38d_1
  tk                 pkgs/main/osx-64::tk-8.6.8-ha441bb4_0
  werkzeug           pkgs/main/noarch::werkzeug-1.0.1-py_0
  wheel              pkgs/main/osx-64::wheel-0.34.2-py38_0
  xz                 pkgs/main/osx-64::xz-5.2.5-h1de35cc_0
  zlib               pkgs/main/osx-64::zlib-1.2.11-h1de35cc_3


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate my_app
#
# To deactivate an active environment, use
#
#     $ conda deactivate


CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


/Users/ankit/miniconda3/bin/python

CommandNotFoundError: Your shell has not been properly configured to use 'conda deactivate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /Users/ankit/miniconda3/envs/my_app_olderver

  added / updated specs:
    - flask
    - python=2.7
    - sqlalchemy


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    certifi-2019.11.28         |           py27_0         153 KB
    itsdangerous-1.1.0         |           py27_0          27 KB
    markupsafe-1.1.1           |   py27h1de35cc_0          27 KB
    pip-19.3.1                 |           py27_0         1.7 MB
    python-2.7.18              |       h47d645e_1         9.3 MB
    setuptools-44.0.0          |           py27_0         513 KB
    sqlalchemy-1.3.12          |   py27h1de35cc_0         1.4 MB
    wheel-0.33.6               |           py27_0          42 KB
    ------------------------------------------------------------
                                           Total:        13.2 MB

The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/osx-64::ca-certificates-2020.1.1-0
  certifi            pkgs/main/osx-64::certifi-2019.11.28-py27_0
  click              pkgs/main/noarch::click-7.1.2-py_0
  flask              pkgs/main/noarch::flask-1.1.2-py_0
  itsdangerous       pkgs/main/osx-64::itsdangerous-1.1.0-py27_0
  jinja2             pkgs/main/noarch::jinja2-2.11.2-py_0
  libcxx             pkgs/main/osx-64::libcxx-10.0.0-1
  libedit            pkgs/main/osx-64::libedit-3.1.20181209-hb402a30_0
  libffi             pkgs/main/osx-64::libffi-3.3-h0a44026_1
  markupsafe         pkgs/main/osx-64::markupsafe-1.1.1-py27h1de35cc_0
  ncurses            pkgs/main/osx-64::ncurses-6.2-h0a44026_1
  pip                pkgs/main/osx-64::pip-19.3.1-py27_0
  python             pkgs/main/osx-64::python-2.7.18-h47d645e_1
  readline           pkgs/main/osx-64::readline-8.0-h1de35cc_0
  setuptools         pkgs/main/osx-64::setuptools-44.0.0-py27_0
  sqlalchemy         pkgs/main/osx-64::sqlalchemy-1.3.12-py27h1de35cc_0
  sqlite             pkgs/main/osx-64::sqlite-3.31.1-h5c1f38d_1
  tk                 pkgs/main/osx-64::tk-8.6.8-ha441bb4_0
  werkzeug           pkgs/main/noarch::werkzeug-1.0.1-py_0
  wheel              pkgs/main/osx-64::wheel-0.33.6-py27_0
  zlib               pkgs/main/osx-64::zlib-1.2.11-h1de35cc_3


Proceed ([y]/n)? y


Downloading and Extracting Packages
wheel-0.33.6         | 42 KB     | #################################################################### | 100% 
python-2.7.18        | 9.3 MB    | #################################################################### | 100% 
pip-19.3.1           | 1.7 MB    | #################################################################### | 100% 
markupsafe-1.1.1     | 27 KB     | #################################################################### | 100% 
certifi-2019.11.28   | 153 KB    | #################################################################### | 100% 
sqlalchemy-1.3.12    | 1.4 MB    | #################################################################### | 100% 
itsdangerous-1.1.0   | 27 KB     | #################################################################### | 100% 
setuptools-44.0.0    | 513 KB    | #################################################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate my_app_olderver
#
# To deactivate an active environment, use
#
#     $ conda deactivate


CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.


Python 3.6.10 |Anaconda, Inc.| (default, Mar 23 2020, 17:45:12) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
(base) ankit@Jarvis cs-python-AYNTK-programs % conda env list
# conda environments:
#
                         /Users/ankit/anaconda3
base                  *  /Users/ankit/miniconda3
my_app                   /Users/ankit/miniconda3/envs/my_app
my_app_olderver          /Users/ankit/miniconda3/envs/my_app_olderver
'''