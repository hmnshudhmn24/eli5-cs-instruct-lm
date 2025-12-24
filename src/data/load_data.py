from datasets import load_dataset

def load_eli5_dataset(t,v,s): return load_dataset('json',data_files={'train':t,'validation':v,'test':s})
