from flask import Flask
from transformers import AutoTokenizer, AutoModelForCausalLM
from config import preConfigure, postConfigure

class ModelBoot(Flask):

    def __init__(self, import_name, repository):
        super().__init__(import_name=import_name) 
        self.repository = repository
        self._load_tokenizer()
        preConfigure(self, self.tokenizer)
        self._load_model()
        postConfigure(self, self.tokenizer)

    def _load_tokenizer(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.repository)
       
    def _load_model(self):
        self.model = AutoModelForCausalLM.from_pretrained(self.repository)
