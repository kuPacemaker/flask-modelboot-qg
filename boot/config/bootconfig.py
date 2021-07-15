class BootConfig:

    def __init__(self, tokenizer_class, model_class):
        self.tokenizer_class = tokenizer_class
        self.model_class = model_class

    def configure(self, repo):
        tokenizer = self.tokenizer_class.from_pretrained(repo)
        self.preconfigure(repo, tokenizer)
        model = self.model_class.from_pretrained(repo)
        self.postconfigure(repo, tokenizer, model)
        return tokenizer, model

    def preconfigure(self, repo, tokenizer):
        pass

    def postconfigure(self, repo, tokenizer, model):
        pass
