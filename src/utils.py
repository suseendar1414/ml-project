import sys
import pandas as pd
import numpy as np
import os
import dill  # Assuming you imported the dill module for object serialization
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:  # Corrected the syntax for the except block
        raise CustomException(e, sys)
