from flask import Flask
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from .config.modelconfig import ModelConfig

class ModelBootApp(Flask):

    configuration = ModelConfig(AutoTokenizer, AutoModelForSeq2SeqLM)

    def __init__(self, import_name, repository, *args, **kwargs):
        super().__init__(import_name=import_name, *args, **kwargs) 
        self.repository = repository
        self.tokenizer, self.model = ModelBootApp.configuration.configure(repository)

    def offer(self, message):
        input_ids = self.tokenizer.encode(message, return_tensors="pt")
        outputs = self.model.generate(input_ids)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
