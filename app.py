from flask import Flask
from flask import request, render_template
import urllib.request
import json
import os

app=Flask(__name__)

@app.route('/', methods=["POST","GET"])
def handle_form():
    if request.method == 'POST':
     
     query=request.form.get('user-input')
    
     data = {"query":f"{query}"}

     body = str.encode(json.dumps(data))

     url = 'https://sakbot-bot.southindia.inference.ml.azure.com/score'
 
     api_key = 'CqadEIYRy3gUwA7Ge3dtKHIXBQnK6XrX'
     if not api_key:
      raise Exception("A key should be provided to invoke the endpoint")


     headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'sakbot-bot-1' }

     req = urllib.request.Request(url, body, headers)

     try:
      response = urllib.request.urlopen(req)

      result = response.read()
      result_json = json.loads(result.decode('utf-8'))
      reply = result_json['reply']
      return render_template('chatbot.html', reply=reply)
      
    
     except urllib.error.HTTPError as error:
      print("The request failed with status code: " + str(error.code))
      print(error.info())
      print(error.read().decode("utf8", 'ignore'))

    else:
        return render_template("chatbot.html")


if __name__=='__main__':
    app.run(debug=True)