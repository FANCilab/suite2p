# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import suite2p
from suite2p.run_s2p import run_s2p


# ops_options = {
#     "child1": {"key": "value", "key2": 1},
#     "child2": {"key": "value2", "key2": 2},
#     "child3": {"key": "value3", "key2": 3}
# }


ops =  np.load("Z:\Data\suite2p_tutorial\Ops\ops_1P_miniscope.npy", allow_pickle=True)
ops = ops.item()
db = {
    'data_path': "Z:\Data\suite2p_tutorial\Data\1P_Miniscope\20240303\4",
    'save_path0': "D:/Data/2P/1P",
}

output_ops = suite2p.run_s2p(ops=ops, db=db)