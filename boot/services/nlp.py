class NLPService:
    def __init__(self, tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model

    def offer(message):
       raise NotImplementedError("abstract method!")

class QGService(NLPService):
    def __init__(self, tokenizer, model, *args, **kwargs):
        super().__init__(tokenizer, model)
        self.return_tensors = kwargs.get('return_tensors', "pt")

    def offer(self, message):
        input_ids = self.tokenizer.encode(message, return_tensors=self.return_tensors)
        outputs = self.model.generate(input_ids)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


