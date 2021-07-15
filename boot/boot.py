from flask import Flask
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from .config.bootconfig import BootConfig
from .services.nlp import QGService

class ModelBootApp(Flask):

    configuration = BootConfig(AutoTokenizer, AutoModelForSeq2SeqLM)

    def __init__(self, import_name, repository, *args, **kwargs):
        super().__init__(import_name=import_name, *args, **kwargs) 
        self.repository = repository
        self.service = QGService(
            *ModelBootApp.configuration.configure(repository), #tokenizer, model
            return_tensors="pt"
        )
