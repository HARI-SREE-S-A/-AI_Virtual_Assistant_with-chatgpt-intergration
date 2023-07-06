import openai
openai.api_key = "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"
models = openai.Model.list()
for model in models['data']:


    
    print(model['id'])
