class NLPService:
    def __init__(self, tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model

    def offer(self, message):
       raise NotImplementedError("abstract method!")

class QGService(NLPService):
    def __init__(self, tokenizer, model, *args, **kwargs):
        super().__init__(tokenizer, model)
        self.return_tensors = kwargs.get('return_tensors', "pt")
        self.offermap = {
            str: self._offer_single,
            list: self._offer_batch
        }

    def offer(self, message):
        return self.offermap[type(message)](message)

    def _offer_single(self, message):
        input_ids = self.tokenizer.encode(message, return_tensors=self.return_tensors)
        outputs = self.model.generate(input_ids)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def _offer_batch(self, messages):
        inputs_encoded = self.tokenizer.batch_encode_plus(messages, 
                                                     padding='longest', 
                                                     return_tensors=self.return_tensors)
        input_ids = inputs_encoded['input_ids']
        attention_mask = inputs_encoded['attention_mask']
        input_ids, attention_mask = self._trim_batch(input_ids, self.tokenizer.pad_token_id, attention_mask)
        outputs = self.model.generate(input_ids, attention_mask=attention_mask)
        return self.tokenizer.batch_decode(outputs, skip_special_tokens=True)

    def _trim_batch(self, input_ids, pad_token_id, attention_mask=None):
        keep_column_mask = input_ids.ne(pad_token_id).any(dim=0)
        if attention_mask is None:
            return input_ids[:, keep_column_mask]
        else:
            return (input_ids[:, keep_column_mask], attention_mask[:, keep_column_mask])


