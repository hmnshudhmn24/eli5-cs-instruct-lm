from transformers import Trainer,TrainingArguments

def get_trainer(m,t,d,c): a=TrainingArguments(output_dir=c['output_dir'],per_device_train_batch_size=c['batch_size'],num_train_epochs=c['epochs'],learning_rate=c['learning_rate'],logging_steps=c['logging_steps'],evaluation_strategy=c['evaluation_strategy']); return Trainer(model=m,args=a,train_dataset=d['train'],eval_dataset=d['validation'],tokenizer=t)
