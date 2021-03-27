# Serve T5 model as a flask application

import torch
import json
import time
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
from flask import Flask, request

secret_token = 'this secret should not be hardcoded like this'
model_large = None
tokenizer_large = None
model_small = None
tokenizer_small = None
device = None
app = Flask(__name__)

def load_model():
	global model_small
	global tokenizer_small
	global device
	# Download and save the models:
	# Large
	model_small = T5ForConditionalGeneration.from_pretrained('t5-small')
	tokenizer_small = T5Tokenizer.from_pretrained('t5-small')
	print ("loading models...")
	device = torch.device('cpu')
	print ("models loaded...")

def getTextFromRequest(request):
	data = request.get_json()
	preprocess_text = data['text'].strip().replace("\n","")
	print ("original text preprocessed: \n", preprocess_text)
	return "summarize: "+ preprocess_text

def getSummary(tokenizer, model, prepared_text):
	tokenized_text = tokenizer.encode(prepared_text, return_tensors="pt").to(device)
	summary_ids = model.generate(tokenized_text,
		num_beams=4,
		no_repeat_ngram_size=2,
		min_length=30,
		max_length=100,
		early_stopping=True)
	output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
	print ("\n\nSummarized text: \n", output)
	return output

def hasToken(request):
	data = request.get_json()
	if data['token'] == secret_token: 
		return True
	else:
		return False

@app.route('/')
def home_endpoint():
    return 'Nothing to see here... move along.'


@app.route('/small', methods=['POST'])
def get_small_summary():
	if hasToken(request) == False: return 'permission denied'
	start_time = time.time()
	if request.method == 'POST':
			t5_prepared_Text = getTextFromRequest(request)
			output = getSummary(tokenizer_small, model_small, t5_prepared_Text)
	print("--- %s seconds ---" % (time.time() - start_time))
	return str(output)

if __name__ == '__main__':
	load_model()  # load model at the beginning once only
	app.run(host='0.0.0.0', port=80)
