from flask import Flask
from transformers import AutoTokenizer, AutoModelForCausalLM
from config import preConfigure, postConfigure

class ModelBoot(Flask):

    def __init__(self, import_name, repository, *args, **kwargs):
        super().__init__(import_name=import_name, *args, **kwargs) 
        self.repository = repository
        self._load_tokenizer()
        preConfigure(self)
        self._load_model()
        postConfigure(self)

    def _load_tokenizer(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.repository)
       
    def _load_model(self):
        self.model = AutoModelForCausalLM.from_pretrained(self.repository)

    def offer(self, message):
        input_ids = self.tokenizer.encode(message, return_tensors="pt")
        outputs = self.model.generate(input_ids)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
