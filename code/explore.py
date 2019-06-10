import pickle
from utils import *

with open('../data/history.pkl', 'rb') as f:
    f = pickle.load(f)
    imshow(f, 'LOSS')
