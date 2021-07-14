from transformers import AutoTokenizer, AutoModelWithLMHead

repository = "danyaljj/gpt2_question_generation_given_paragraph_answer"

def main():
    tokenizer, model = load_model()
    while True:
        input_ids = tokenizer.encode(input(), return_tensors="pt")
        outputs = model.generate(input_ids)
        print("Generated:", tokenizer.decode(outputs[0], skip_special_tokens=True))
    
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(repository)
    model = AutoModelWithLMHead.from_pretrained(repository)
    notify_load_model()
    return tokenizer, model

def notify_load_model():
    pass


if __name__ == '__main__':
    main()
