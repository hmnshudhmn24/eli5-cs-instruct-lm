from transformers import pipeline

def load_pipeline(p): return pipeline('text-generation',model=p)
