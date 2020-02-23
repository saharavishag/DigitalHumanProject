
# activate:
# 	python3.7 -m venv venv3
# 	source venv3/bin/activate

# deactivate:
# 	deactivate

# env-setup:
# 	pip3 install -r requirements.txt
# 	export api_key=40d61a5ed053486f8b3ef093551f4d40

api-data:
	python3 ./NewsApi/GetNews.py

extract-tokens:
	python3 ./ExtractTokens/ExtractTokens.py

apply-yap:
	. applyYap.sh

reset:
	rm -R content
	rm -R tokens
	rm -R lattice
	rm -R finalresults
	
start:
	reset
	api-data
	extract-tokens
	apply-yap
	
