from transformers import AutoModelForCausalLM

def load_model(m): return AutoModelForCausalLM.from_pretrained(m)
