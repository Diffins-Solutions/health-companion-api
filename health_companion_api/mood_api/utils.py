from django.core.exceptions import ValidationError
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from django.conf import settings

def validate_word_count(text):
    num_words = len(text.split())

    if (num_words > 500):
        raise ValidationError("Word count exceeds 500")

def get_emotion(text):
    model_path = os.path.join(settings.BASE_DIR, 'mood_api', 'models')
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    input_ids = tokenizer.encode(text + '</s>', return_tensors='pt')
    output = model.generate(input_ids=input_ids,
                            max_length=2)
    dec = [tokenizer.decode(ids) for ids in output]
    label = dec[0].replace('<pad> ','')
    return label
