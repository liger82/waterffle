import os
import pickle
import torch
from tqdm import tqdm

def set_6dec(track_id):
	if len(track_id) == 6:
		return track_id
	else:
		i = 6 - len(track_id)
		track_id = '0'*(i) + track_id
		return track_id


def load_poly_encoder_dataset():
    # poly_encoder_dataset saved by pickle
    # format : [label, now_track_id, next_track_id]
    # load raw mfcc data by poly_encoder_dataset
	with open('poly_encoder_dataset.pkl', 'rb') as f:
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
		
			now_mfcc = torch.load(os.path.join(fma_path, now_track_id[:3], (now_track_id+'.pt')))
			#print(os.path.join(fma_path, now_track_id[:3], (now_track_id+'.pt')))
			#print(now_mfcc.shape)
			now_mfcc_set.append(now_mfcc)
		
			next_mfcc = torch.load(os.path.join(fma_path, next_track_id[:3], (next_track_id+'.pt')))
			next_mfcc_set.append(next_mfcc)
		
		except Exception as e:
			print(e)

	print('labels : {}'.format(len(labels)))
	print('now : {}'.format(len(now_mfcc_set)))
	print('next : {}'.format(len(next_mfcc_set)))
	
	return labels, now_mfcc_set, next_mfcc_set
