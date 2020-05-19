## Prereqs
	curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

## Locally
	pip3 install -r requirements.txt
	python3 app.py


## Container
	docker build -t summarizer .
	docker run -p 80:80 summarizer .

## Example usage

curl -X POST   \
 ec2-3-94-112-129.compute-1.amazonaws.com/small  \
-H 'Content-Type: application/json' \
-d '{"text":"The good news is that, after digging into this, there is a lot of low hanging fruit (and regardless of the current circumstances, it’s good company hygiene for us to look back at expenses and consider if there are things we can eliminate). Let me start by saying, this is a work in progress. Changing infrastructure expenses, for example, isn’t an overnight project. We’ve identified about $6M in expenses that we think we can cut and many of you have already been looped into investigating these opportunities.", "token":"this secret should not be hardcoded like this"}'

## How tos:

https://towardsdatascience.com/simple-way-to-deploy-machine-learning-models-to-cloud-fd58b771fdcf

https://medium.com/runwayml/creating-a-custom-gpt-2-slack-bot-with-runwaymls-hosted-models-c639fe135379

