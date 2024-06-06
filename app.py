
from flask import Flask, render_template, redirect, url_for,request
# from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message


import pickle
import pandas 
import smtplib



def get_suggest(crop_soil,crop_type):
    s=file.loc[(file['Crop Soil']==crop_soil) & (file['Crop Type']==crop_type)]
    
    d=s.to_dict()
    name=d.keys()
    lst2=[]
    for l in name:
        lst2.append(l)
    
    l=[]
    
    for i in d.values():
        l.extend(list(i.values()))
    l.extend(lst2)
    return l


app = Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="agrosmartproject2.0@gmail.com"
app.config['MAIL_PASSWORD']="ycbgowgbuzmterqk"
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail= Mail(app)



file=pickle.load(open('file.pkl','rb'))
soil="soil"
crop='crop'
@app.route("/",methods=['GET',"POST"])
def home():
    soil="soil"
    crop='crop'
    
    if request.method=='POST':
        soil=request.form['soil']
        crop=request.form['crop']
    print(soil,crop)
    
    lst=get_suggest(soil,crop)[:6]
    lstindex=get_suggest(soil,crop)[6:]
    print(lst)
    print(lstindex)

    
    

    
    
    return render_template('index.html',lst=lst,lstindex=lstindex)

    # Sending mail using smtp



@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        soil_type= request.form['soil']
        crop_type= request.form['crop']
        mo_number= request.form['contact']
        email1= request.form['email']
        soil=soil_type
        crop=crop_type
    print(soil,crop)
    
    lst=get_suggest(soil,crop)[:6]
    lstindex=get_suggest(soil,crop)[6:]
    print(lst)
    print(lstindex)
    s=""
    for i in range(6):
        s=s+lstindex[i]+" : "+lst[i]+", "
    print(s)


    msg= Message('Recommendation result',sender="agrosmartproject2.0@gmail.com",recipients=[email1])
    msg.body="You have selected"+"\n"+soil_type+"\n"+crop_type+"\n" + mo_number+"\n" + email1 +"\n" +"Recommended parameters are:"+"\n"+ s
    mail.send(msg)

    # lst=get_suggest(soil,crop)[:6]
    # lstindex=get_suggest(soil,crop)[6:]
    return render_template('index.html',lst=lst,lstindex=lstindex)


# crop combination

# lst=get_suggest(soil,crop)[:6]
# lstindex=get_suggest(soil,crop)[6:]
# if soil_type != crop_type:
#     for i in soil_type:
#         for j in crop_type:
#             print(soil_type,crop_type[:6])
# elif:
#     lst=get_suggest(soil,crop)[:6]
#     lstindex=get_suggest(soil,crop)[6:]

# try:
    
#     for i in soil_type:
#         for j in crop_type:
#             print(soil_type,crop_type[:6])

#     print("Result found :", lst,lstindex)
# except ZeroDivisionError:
        
#     return render_template('index.html',lst=lst,lstindex=lstindex)

    




if __name__=="__main__":
    app.run(debug=True)