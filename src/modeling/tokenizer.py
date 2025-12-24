from transformers import AutoTokenizer

def load_tokenizer(m): t=AutoTokenizer.from_pretrained(m); t.pad_token=t.eos_token; return t
