import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if not seqs:
        return seqs
    
    # handle if max_len is None
    max_len = max(len(seq) for seq in seqs) if max_len is None else max_len

    # add pad_value as many times as max_len-len(seq), if it is negative no pad value is added
    final = [
        seq[:max_len]+[pad_value]*(max_len-len(seq)) 
        for seq in seqs
    ]
    return np.asarray(final)
        
    
