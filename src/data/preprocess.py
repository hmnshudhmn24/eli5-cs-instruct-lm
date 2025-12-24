from src.data.prompt_builder import build_prompt

def preprocess(e): e['prompt']=build_prompt(e['question']); e['labels']=e['answer']; return e
