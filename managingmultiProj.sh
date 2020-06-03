#Managing multiple project environments
#can mix up packages and dependencies mixed up, so managing is imp
#conda and pip can be used interchangably
#if pip can't find, use conda to find packages
#create an empty directory
mkdir my_project
cd my_project

#make a new vir env
conda create --name my_project_env flask sqlalchemy numpy pandas

pip list
#shows all the packages installed

#have all you need?
#create .yaml file to 

conda env export > environment.yaml
#some people will use yml and that's same

cat environment.yaml
#lists the name of env and all the dependencies with the version number
#so someone can now use this file to create a replica on their machine
#they will create a project directorym use the env file and run the following

conda env create -f environment.yaml

#how we manage our env variables
#used in doff projects to hold secret keys, python paths etc.
#sensitive data handling w/o everyone seeing the contents!

#Where is our env located?
conda env list
#this will list all the environ that exist on my machine

#change dir to v env
cd users/ankit//../

#create 2 diff directory trees to set env variables
#-p means it doesnt have to alreadyt exist
mkdir -p etc/conda/activate.d

mkdir -p etc/conda/deactivate.d
touch etc/conda/activate.d/env_vars.shows
touch etc/conda/deactivate.d/env_vars.shows

#lets edit these files and change variable values in them. activate file will set and the other one will deset
#More on: 
#Managing environments documentation

 https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
