# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 10:12:30 2025

@author: User
"""

import numpy as np
from scipy.stats import zscore
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from matplotlib.patches import Polygon

#load data
F = np.load('F.npy', allow_pickle=True)
Fneu = np.load('Fneu.npy', allow_pickle=True)
spks = np.load('spks.npy', allow_pickle=True)
stat = np.load('stat.npy', allow_pickle=True)
ops =  np.load('ops.npy', allow_pickle=True)
ops = ops.item()
iscell = np.load('iscell.npy', allow_pickle=True)

#select cells and define intermediate values
neurons_raw = F[iscell[:, 0].astype(bool), :]
nN, nFrames = neurons_raw.shape
frameTime = np.arange(1, nFrames + 1) / ops['fs']

#correct for neuropil and zscore
neuropil = Fneu[iscell[:,0].astype(bool),:]
neurons = F - Fneu
neurons = zscore(neurons, axis=1)

#smooth
neurons_smooth = gaussian_filter1d(neurons, sigma=1.5, axis=1)
plt.figure(figsize=(12, 6))
plt.plot(frameTime, neurons[10,:], label='Noisy')
plt.plot(frameTime, neurons_smooth[10,:], label='Smoothed', linewidth=2)
plt.legend()
plt.show()

#debleach
#add


#Plot first n neurons' z-scored traces
n = 5 #how many neurons' traces do you want to visualize
plt.figure(figsize=(12, 6))
for i in range(min(n, neurons.shape[0])):
    plt.plot(frameTime, neurons[i], label=f'Neuron {i+1}')
plt.xlabel('Seconds')
plt.ylabel('Z-scored fluorescence')
plt.title('Z-scored fluorescence traces of neurons')
plt.legend()
plt.show()

#heatmap
fluo_interval = 100 #to visualize every nth neuron in the recording
plt.figure(figsize=(10, 8))
plt.imshow(neurons[0::fluo_interval,:], aspect='auto', cmap='viridis')
plt.colorbar(label='Z-scored fluorescence')
plt.xlabel('Frame')
plt.ylabel('Neuron')
plt.title('Heatmap of z-scored neural activity')
plt.show()

#raster plot
spike_interval = 100
plt.figure(figsize=(12, 6))
plt.imshow(spks[0::spike_interval,:], aspect='auto', cmap='Greys', interpolation='none')
plt.xlabel('Frame')
plt.ylabel('Neuron')
plt.title('Raster plot of inferred spikes')
plt.show()

#show ROIs
mean_image = ops['meanImg']
plt.imshow(mean_image, cmap='gray')

for i, roi in enumerate(stat):
    if iscell[i,0]:
        poly = Polygon([roi['med'[0]], [roi['med'][1]]], fill=None, edgecolor='r', linewidth=1)
        plt.gca().add_patch(poly)
plt.title('ROIs overlay on mean image')
plt.show()


