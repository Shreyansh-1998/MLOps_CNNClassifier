import os
from box.exceptions import BoxValueError
import yaml
from MLOPSCNNCLASSIFIER import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read the yaml file and return the ConfigBox
    
    Args:
        path_to_yaml(str): path like input
    
    Raises:
        ValueError: If the yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directoties: list,verbose=True):
    """
    Create directories

    Args:
        path_to_directoties(list): list of path of directories
        ignore_log(bool,optional): ignore if multiple dirs is to be created. Defaults to False
    """
    for path in path_to_directoties:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory created at {path}")
@ensure_annotations
def save_json(path:Path,data:dict):
    """
    Save the json data  
    Args:
        path(Path): path to the json file
        data(dict): data to be saved in the json file  
    """
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
    
    logger.info(f"json file saved at {path}")


@ensure_annotations
def load_json(path:Path)->ConfigBox:
    """
    Loads the json files and returns the ConfigBox

    Args:
        path(Path): path to the json file

    Returns:
        ConfigBox: data as class attribute instead of a dictionary
    """
    with open(path) as f:
        content=json.load(f)
        logger.info(f"json file loaded successfully from {path}")
        return ConfigBox(content)


@ensure_annotations
def save_bin(data:Any,path:Path):
    """
    Save the binary file

    Args:
        data(Any): data to be saved as binart file
        path(Path): path to the file
    """
    joblib.dump(value=data,path=Path)
    logger.info(f"Binary file saved at {path}")


@ensure_annotations
def load_bin(path:Path)->Any:
    """
    Load the binary file

    Args:
        path(Path): path to the binaryfile

    Returns:
        Any: data from the binary file
    """
    data=joblib.load(path)
    logger.info(f"Binary file loaded successfully from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of the file in KB

    Args:
        path(Path): path to the file

    Returns:
        str: size of the file in Kb
    """
    size_in_kb= round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring,fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())