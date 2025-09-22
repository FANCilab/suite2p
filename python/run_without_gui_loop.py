# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import suite2p
from suite2p.run_s2p import run_s2p

#here you will load the ops for your current data type (for example, 1P or 2P)
ops =  np.load("file_path", allow_pickle=True)
ops = ops.item()

db_dict = {}

#now you will modify some fields of those ops as appropriate for this specific experiment. You always need to change some file directories, and sometimes
#other fields like cell diameter if there was a different zoom.

#first entry in db dictionary
db_dict['First experiment'] = {
    'data_path': "path",
    'save_path0': "path",
}


db_dict['Second experiment'] = {
    'data_path': "path",
    'save_path0': "path",
}

num_experiments = np.size(db_dict)

#for every entry in the db dictionary, call on the common ops and the specific db
list_experiments = list(db_dict.keys())
for i in range(num_experiments):
    output_ops = suite2p.run_s2p(ops = ops, db = db_dict[list_experiments[i]])


