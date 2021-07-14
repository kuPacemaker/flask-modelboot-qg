from transformers import AutoTokenizer, AutoModelForCausalLM

repository = "p208p2002/gpt2-squad-qg-hl"

def main():
    tokenizer, model = load_model()
    while True:
        input_ids = tokenizer.encode(input(), return_tensors="pt")
        outputs = model.generate(input_ids, 
                max_length=512, 
                early_stopping=True, 
                temperatur=0.85, 
                do_sample=True, 
                top_p=0.9, 
                top_k=10, 
                num_beams=3, 
                pad_token_id=tokenizer.pad_token_id, 
                eos_token_id=tokenizer.eos_token_id)
        print("Generated:", tokenizer.decode(outputs[0], skip_special_tokens=True))
    
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(repository)
    model = AutoModelForCausalLM.from_pretrained(repository)
    model.resize_token_embeddings(len(tokenizer))
    add_tokens(tokenizer)
    notify_load_model()
    return tokenizer, model

def add_tokens(tokenizer):
    if tokenizer.pad_token is None:
        tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    if tokenizer.sep_token is None:
        tokenizer.add_special_tokens({'sep_token': '[SEP]'})
    if tokenizer.eos_token is None:
        tokenizer.add_special_tokens({'eos_token': '[EOS]'})
    tokenizer.add_tokens(['[HL]'], special_tokens=True)

def notify_load_model():
    pass


if __name__ == '__main__':
    main()
