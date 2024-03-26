import os
from pathlib import Path
import sys
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

projectname = 'MLOPSCNNCLASSIFIER'


list_of_files=[
    ".github/worklfows/.gitkeep",
    f"src/{projectname}/__init__.py",
    f"src/{projectname}/components/_init__py",
    f"src/{projectname}/utils/__init__.py",
    f"src/{projectname}/config/__init__.py",          
    f"src/{projectname}/config/configuration.py",
    f"src/{projectname}/pipeline/__init__.py",
    f"src/{projectname}/entity/__init__.py",
    f"src/{projectname}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.py",
    "templates/index.html"
    
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Directory created at {filedir} for file{filename}")
    
    if(not os.path.exists(filepath))or(os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"File created at {filepath}")

    else:
        logging.info(f"File already exists at {filepath}")

    
