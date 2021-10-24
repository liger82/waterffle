import os
import pickle

import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np
from tqdm import tqdm

def set_6dec(track_id):
	if len(track_id) == 6:
		return track_id
	else:
		i = 6 - len(track_id)
		track_id = '0'*(i) + track_id
		return track_id

def padding(mfcc_list):
	# find the max time_length
	maxLength = 0
	seq_len_list = []
	for mfcc in mfcc_list:
		seq_len_list.append(mfcc.shape[1])
		maxLength = max(maxLength, mfcc.shape[1])
	print('max length : {}'.format(maxLength))

	# padding
	print('padding')
	for i, mfcc in enumerate(mfcc_list):
		# padSecs is the length of padding
		padSecs = maxLength - mfcc.shape[1]
		# numpy.pad pad the inputList[origI] with zeros at the tail
		mfcc_list[i] = np.pad(mfcc.T, ((0,padSecs), (0,0)), 'constant', constant_values=0)

	pad_mfcc_list = np.asarray(mfcc_list)
	print('mfcc shape : {}'.format(pad_mfcc_list.shape))

	return pad_mfcc_list

def paddingAndCrop(data, last_pad_length, pad_value=0):
	print("====== Zero Padding and Crop ======")	
	for i in tqdm(range(len(data))):
		if last_pad_length - data[i][0].shape[-1] > 0:
			pad = ((0,0), (0, last_pad_length - data[i][0].shape[-1]))
			#data[i][0] = F.pad(data[i][0], pad, "constant", pad_value)
			data[i][0] = np.pad(data[i][0], pad, 'constant', constant_values=pad_value)
		else:
			data[i][0] = data[i][0][:,:last_pad_length]
        
		if last_pad_length - data[i][1].shape[-1] > 0:
			pad = ((0,0), (0, last_pad_length - data[i][1].shape[-1]))
			#pad = (0, last_pad_length - data[i][1].shape[-1])
			#data[i][1] = F.pad(data[i][1], pad, "constant", pad_value)
			data[i][1] = np.pad(data[i][1], pad, 'constant', constant_values=pad_value)
		else:
			data[i][1] = data[i][1][:,:last_pad_length]
		
	return data

def load_poly_encoder_dataset(last_pad_length, num_feature=128, pad_value=0):
    # poly_encoder_dataset saved by pickle
    # format : [label, now_track_id, next_track_id]
    # load raw mfcc data by poly_encoder_dataset
	with open('poly_encoder_dataset_b32.pkl', 'rb') as f:
	    pe_dataset = pickle.load(f)

	fma_path = '/home/super/database/fma/data/fma_small/'

	print("====== Get MFCC with padding and crop======")	
	now_mfcc_set = []
	next_mfcc_set = []
	label_set = []
	cs_path = []
	ns_path = []

	for i, pe in enumerate(tqdm(pe_dataset)):
		now_track_id = set_6dec(pe[1])
		next_track_id = set_6dec(pe[-1])
	
		try: 
			#now_mfcc = torch.load(os.path.join(fma_path, now_track_id[:3], (now_track_id+'.pt')))
			cs_path.append(os.path.join(fma_path, now_track_id[:3], now_track_id))
			now_mfcc = np.load(os.path.join(fma_path, now_track_id[:3], (now_track_id+'.npy')))
			now_mfcc = now_mfcc.reshape(num_feature,-1)

			if last_pad_length - now_mfcc.shape[-1] > 0:
				pad = ((0,0), (0, last_pad_length - now_mfcc.shape[-1]))
				now_mfcc = np.pad(now_mfcc, pad, 'constant', constant_values=pad_value)
			else:
				now_mfcc = now_mfcc[:,:last_pad_length]
			
			now_mfcc_set.append(now_mfcc)
		
			#next_mfcc = torch.load(os.path.join(fma_path, next_track_id[:3], (next_track_id+'.pt')))
			ns_path.append(os.path.join(fma_path, next_track_id[:3], next_track_id))
			next_mfcc = np.load(os.path.join(fma_path, next_track_id[:3], (next_track_id+'.npy')))
			next_mfcc = next_mfcc.reshape(num_feature,-1)	
			
			if last_pad_length - next_mfcc.shape[-1] > 0:
				pad = ((0,0), (0, last_pad_length - next_mfcc.shape[-1]))
				next_mfcc = np.pad(next_mfcc, pad, 'constant', constant_values=pad_value)
			else:
				next_mfcc = next_mfcc[:,:last_pad_length]
			
			next_mfcc_set.append(next_mfcc)
			
			label_set.append(pe[0])

			del now_mfcc
			del next_mfcc
		
		except Exception as e:
			print(e)

	#data = np.asarray(data)	
	#print('data : {}'.format(data.shape))
	
	return now_mfcc_set, next_mfcc_set, label_set, cs_path, ns_path

def load_ausil_feature_dataset():
    # poly_encoder_dataset saved by pickle
    # format : [label, now_track_id, next_track_id]
    # load raw mfcc data by poly_encoder_dataset
	with open('poly_encoder_dataset_b32.pkl', 'rb') as f:
	    pe_dataset = pickle.load(f)

	fma_path = '/home/super/database/fma/data/fma_small/'

	print("====== Get extracted feature by pre-trained CNN ======")	
	now_mfcc_set = []
	next_mfcc_set = []
	label_set = []

	for i, pe in enumerate(tqdm(pe_dataset)):
		now_track_id = set_6dec(pe[1])
		next_track_id = set_6dec(pe[-1])
	
		try: 
			#now_mfcc = torch.load(os.path.join(fma_path, now_track_id[:3], (now_track_id+'.pt')))
			now_mfcc = np.load(os.path.join(fma_path, now_track_id[:3], (now_track_id+'_wlaf.npz')))
			now_mfcc_set.append(now_mfcc['features'])
		
			#next_mfcc = torch.load(os.path.join(fma_path, next_track_id[:3], (next_track_id+'.pt')))
			next_mfcc = np.load(os.path.join(fma_path, next_track_id[:3], (next_track_id+'_wlaf.npz')))
			next_mfcc_set.append(next_mfcc['features'])
			
			label_set.append(pe[0])

			del now_mfcc
			del next_mfcc
		
		except Exception as e:
			print(e)

	#data = np.asarray(data)	
	#print('data : {}'.format(data.shape))
	
	return now_mfcc_set, next_mfcc_set, label_set