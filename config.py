from transformers import PretrainedConfig

def preConfigure(modelboot):
    configTokenizer(modelboot.tokenizer)

def postConfigure(modelboot):
    custom_dict = {
        'max_length': 512,
        'early_stopping': True,
        'temperature': 0.85,
        'do_sample': True,
        'top_p': 0.9,
        'top_k': 10,
        'num_beams': 3,
        'pad_token_id': modelboot.tokenizer.pad_token_id,
        'eos_token_id': modelboot.tokenizer.eos_token_id,
    }
    modelboot.model.config = PretrainedConfig.from_pretrained(modelboot.repository)
    modelboot.model.config.update(custom_dict)
    print("ModelConfig:", modelboot.model.config)

def configTokenizer(tokenizer):
    if tokenizer.pad_token is None:
        tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    if tokenizer.sep_token is None:
        tokenizer.add_special_tokens({'sep_token': '[SEP]'})
    if tokenizer.eos_token is None:
        tokenizer.add_special_tokens({'eos_token': '[EOS]'})
    tokenizer.add_tokens(['[HL]'], special_tokens=True)

