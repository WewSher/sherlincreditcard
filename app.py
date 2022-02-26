#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template # request from the front end 
import joblib

@app.route("/", methods = ["GET", "POST"]) # decorator, the function before the real function
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        print(income,age,loan)
        model = joblib.load("CC Default")
        pred = model.predict([float(income), float(age), float(loan)])
        print(pred)
        pred = pred[0]
        s = "The predicted credit card default is " + str(pred)
   
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "Predict 2")) # Requesting from the front end


# In[ ]:





# In[ ]:


#only for the main module
if __name__ == '__main__':
    app.run(host="127.0.0.1", port = int("80"))


# In[ ]:




