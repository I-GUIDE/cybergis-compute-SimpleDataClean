#!/bin/env python3

import yaml
import os


processor_dict ={'$1': {'SimpleDataClean':{'start_year': os.environ['param_start_year'],'end_year': os.environ['param_end_year']}}}

with open('/job/executable/data_clean.yml','w') as demfile:
    yaml.dump(processor_dict,demfile)


