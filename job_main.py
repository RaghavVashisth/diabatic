from flask import Flask,render_template,request
import joblib


app = Flask(__name__)

model = joblib.load('diabatic_80.pkl')
@app.route('/')
def home():
    return render_template('home1.html')

@app.route('/data',methods=['post'])
def data():
    # 'preg' , 'plas' , 'pres', 'skin' , 'test', 'mass' , 'pedi', 'age', 'class'
    preg_=request.form.get('preg')
    plas_=request.form.get('plas')
    pres_=request.form.get('pres')
    skin_=request.form.get('skin')
    test_=request.form.get('test')
    mass_=request.form.get('mass')
    pedi_=request.form.get('pedi')
    age_=request.form.get('age')
    #class_=request.form.get('class')
    print(preg_,plas_,pres_,skin_,test_,mass_,pedi_,age_)
    
    result =  model.predict([[preg_,plas_,pres_,skin_,test_,mass_,pedi_,age_]])
    if result[0] ==1:
        data = 'person is diabatic'
    else:
        data = 'person is not diabetic'
    
    print(data)
    return render_template('predict.html',data = data)
 
app.run(debug=True)

