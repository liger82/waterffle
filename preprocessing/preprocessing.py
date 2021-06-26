import os
import pickle
import torch
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

def load_poly_encoder_dataset():
    # poly_encoder_dataset saved by pickle
    # format : [label, now_track_id, next_track_id]
    # load raw mfcc data by poly_encoder_dataset
	with open('poly_encoder_dataset_b32.pkl', 'rb') as f:
	    pe_dataset = pickle.load(f)

	fma_path = '/home/super/database/fma/data/fma_small/'
	
	labels = []
	now_mfcc_set = []
	next_mfcc_set = []
	for i, pe in enumerate(tqdm(pe_dataset)):
		now_track_id = set_6dec(pe[1])
		next_track_id = set_6dec(pe[-1])
	
		try: 
			labels.append(pe[0])
		
			#now_mfcc = torch.load(os.path.join(fma_path, now_track_id[:3], (now_track_id+'.pt')))
			now_mfcc = np.load(os.path.join(fma_path, now_track_id[:3], (now_track_id+'.npy')))
			now_mfcc = now_mfcc.reshape(256,-1)	
			now_mfcc_set.append(now_mfcc)
		
			#next_mfcc = torch.load(os.path.join(fma_path, next_track_id[:3], (next_track_id+'.pt')))
			next_mfcc = np.load(os.path.join(fma_path, next_track_id[:3], (next_track_id+'.npy')))
			next_mfcc = next_mfcc.reshape(256,-1)	
			next_mfcc_set.append(next_mfcc)

			del now_mfcc
			del next_mfcc
		
		except Exception as e:
			print(e)
	
	labels = np.array(labels)
	now_mfcc_set = padding(now_mfcc_set)
	next_mfcc_set = padding(next_mfcc_set)
	
	print('labels : {}'.format(labels.shape))
	print('now_mfcc_set : {}'.format(now_mfcc_set.shape))
	print('next_mfcc_set : {}'.format(next_mfcc_set.shape))
	
	return labels, now_mfcc_set, next_mfcc_set

def load_dataset():
    # poly_encoder_dataset saved by pickle
    # format : [label, now_track_id, next_track_id]
    # load raw mfcc data by poly_encoder_dataset
	with open('poly_encoder_dataset.pkl', 'rb') as f:
	    pe_dataset = pickle.load(f)

	fma_path = '/home/super/database/fma/data/fma_small/'
	
	data = []
	for i, pe in enumerate(tqdm(pe_dataset)):
		if i > 100:
			break
		tmp = []            
		now_track_id = set_6dec(pe[1])
		next_track_id = set_6dec(pe[-1])
	
		try: 
		
			now_mfcc = torch.load(os.path.join(fma_path, now_track_id[:3], (now_track_id+'.pt')))
			#print(os.path.join(fma_path, now_track_id[:3], (now_track_id+'.pt')))
			#print(now_mfcc.shape)
			tmp.append(now_mfcc)
		
			next_mfcc = torch.load(os.path.join(fma_path, next_track_id[:3], (next_track_id+'.pt')))
			tmp.append(next_mfcc)
			tmp.append(pe[0])
			data.append(tmp)
		
		except Exception as e:
			print(e)

	print('data : {}'.format(len(data)))
# 	print('now : {}'.format(len(now_mfcc_set)))
# 	print('next : {}'.format(len(next_mfcc_set)))
	
	return data
