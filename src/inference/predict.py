from src.inference.pipeline import load_pipeline

def predict(q,p='checkpoints'): return load_pipeline(p)(q,max_new_tokens=200)
