#an in-depth look at Python's package management system, pip. We'll walk through how to install, 
#uninstall, list, and upgrade packages. We will also dive into how we can output 
#our dependencies and install a list of dependencies.
#On terminal try:

pip help
pip help install
pip search Pympler
pip install Pympler
pip list #lists package and ver num
#pip install Pympler to remove the package

#how do we know package is latest?
pip list -o #will list all the corresp versions

#update the old ones one by one to the latest available e.g. 2 updates below
pip install -U biopython
pip install -U google-auth

#freeze command - o/p all packages and ver num in a REQUIREMETNS format

pip freeze > requirements.txt
cat requirements.txt

#update based on a requirements file
pip install -r requirements.txt

#see outdates ones
pip list outdated

#update the ones that need updating - use if only few such packages

pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -uninstall
#pip freeze will output all the req, --local only prints local packages
#pipe the output to grep command that detches versions
#pipe to cut command that sets the delimiter to = sign and returns the first arg back of the result
#cut command cuts out after or before the equal signa nd only return package name strings
#xargs take that string package name and install it with a -U i.e. upgrade flag





