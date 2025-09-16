# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 09:58:31 2025

@author: User
"""

from suite2p.run_s2p import run_s2p

#paths to multiple experiment folders
folder1 = '/path/to/experiment1'
folder2 = '/path/to/experiment2'

#common input settings for all experiments
common_ops = {
    'frame_rate': 30,            
    'n channels': 2,   
    'nplanes': 1,          
    'diameter': 12,              
    'tau': 1.0,                  
    'save_path0': '',            
    'do_registration': True,
}

# Experiment-specific options (for example, only differing by diameter)
ops_exp1 = common_ops.copy()
ops_exp1['diameter'] = 10
ops_exp1['data_path'] = [folder1]
ops_exp1['save_path0'] = folder1 + '/suite2p_results'

ops_exp2 = common_ops.copy()
ops_exp2['diameter'] = 20
ops_exp2['data_path'] = [folder2]
ops_exp2['save_path0'] = folder2 + '/suite2p_results'

# Database dict for Suite2p - can be empty mostly
db_exp1 = {}
db_exp2 = {}

# Run Suite2p on first experiment
print(f"Running Suite2p on {folder1}")
ops_exp1 = run_s2p(ops_exp1, db_exp1)

# Run Suite2p on second experiment
print(f"Running Suite2p on {folder2}")
ops_exp2 = run_s2p(ops_exp2, db_exp2)
