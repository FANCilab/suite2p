# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import suite2p
from suite2p.run_s2p import run_s2p

ops =  np.load("file_path", allow_pickle=True)
ops = ops.item()
db = {
    'data_path': "path",
    'save_path0': "path",
}


output_ops = suite2p.run_s2p(ops=ops, db=db)
