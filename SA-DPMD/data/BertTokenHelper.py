from transformers import BertTokenizer, AutoTokenizer, AutoConfig

class BertTokenHelper(object):
    def __init__(self, bert_dir):
        self.tokenizer = BertTokenizer.from_pretrained(bert_dir) # to use local file
        # self.tokenizer = AutoTokenizer.from_pretrained("/DATA1/ritesh/baselines_discourse_parsing/SA-DPMD/ssp_model100000/tokenizer_config.json", 
        #             config=AutoConfig.from_pretrained("/DATA1/ritesh/baselines_discourse_parsing/SA-DPMD/ssp_model100000"))
        special_tokens_dict = {'additional_special_tokens': ['URL', 'FILEPATH', '<root>']}
        self.tokenizer.add_special_tokens(special_tokens_dict)
        print("Load bert vocabulary finished.")


    def pad_token_id(self): 
        return self.tokenizer.pad_token_id


    def batch_bert_id(self, inst_text):
        for idx, text in enumerate(inst_text):
            inst_text[idx] = text.replace('##', '@@')
        outputs = self.tokenizer.batch_encode_plus(inst_text, add_special_tokens=True)
        input_ids = outputs.data['input_ids']
        token_type_ids = outputs.data['token_type_ids']
        attention_mask = outputs.data['attention_mask']

        return input_ids, token_type_ids, attention_mask







