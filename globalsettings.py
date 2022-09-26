import os
import configparser

# Class to store settings
class prjSettings:
    
    def __init__(self):
        pass

## FILES
prj_files = prjSettings()

prj_files.dir_root  = os.path.abspath(os.path.dirname(__file__)) # Project root is defined by globalsettings.py location
prj_files.dir_data  = os.path.join(prj_files.dir_root, "data")
prj_files.dir_raw   = os.path.join(prj_files.dir_data, "raw")
prj_files.dir_clean = os.path.join(prj_files.dir_data, "clean")

# RAW DATA
prj_files.raw_bank_additional_full  = os.path.join(prj_files.dir_raw, "bank-additional-full.csv")


# OUTPUTS
prj_files.dir_outputs = os.path.join(prj_files.dir_root, "outputs")
prj_files.dir_outputs_files = os.path.join(prj_files.dir_outputs, "files")