from flask import Flask, render_template, request, session,redirect, url_for
import secrets
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.secret_key = 'your_secret_key_here'
text_area_data = []
id = 0
current_data = []

@app.route('/')
def page1():
    session.clear()  # clear session data when visiting home page
    return render_template('page1.html')

@app.route('/page1_submit', methods=['POST'])
def submit_dropdown():
    selected_id = request.form.get('River') # access the 'River' select element's value
    session['id'] = int(selected_id)
    return redirect(url_for('page2', id=session['id']))

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        text_area_1_list = request.form.getlist('text_area_1')
        text_area_2_list = request.form.getlist('text_area_2')
        text_area_3_list = request.form.getlist('text_area_3')
        text_area_4_list = request.form.getlist('text_area_4')
        text_area_5_list = request.form.getlist('text_area_5')
        text_area_6_list = request.form.getlist('text_area_6')
        text_area_7_list = request.form.getlist('text_area_7')
        text_area_8_list = request.form.getlist('text_area_8')

        for i in range(14):
            text_area_data.append([text_area_1_list[i], text_area_2_list[i], text_area_3_list[i],text_area_4_list[i],text_area_5_list[i],text_area_6_list[i],text_area_7_list[i],text_area_8_list[i]])
        current_data = text_area_8_list[13]
        if session['id'] == 1 :
            print("isdkfnsdjnjnvern",session['id'])
            chalakudi_model = load_model('final_chalakudi_gruu.h5')
            dt=pd.read_csv('chalakudi_final.csv')

            scaler=MinMaxScaler()
            scaler=scaler.fit(dt)
            a=np.array(text_area_data)
            data = pd.DataFrame(a, columns=['a','b','c','d','e','f','g','i'])
            disc=data['i']
            data=data.iloc[0:14,0:8]
            data=scaler.transform(data)
            fore=[]
            # n_future=3
            n_past=14
            fore.append(data[0:n_past,0:data.shape[1]])
            fore=np.array(fore)
            def for5(fore):
                ff=chalakudi_model.predict(fore)
                forcasted = np.repeat(ff.reshape(-1,1),8, axis=1)
                precip_for = scaler.inverse_transform(forcasted)[:, 7]
                print(precip_for)
                return precip_for
            
            kk=for5(fore)
            print(kk)
            
           
        elif session['id'] == 2 :
            print("isdkfnsdjnjnvern",session['id'])
            achankovil_model = load_model('achankovil.h5')
            dt=pd.read_csv('achankovil_combined.csv')

            scaler=MinMaxScaler()
            scaler=scaler.fit(dt)
            a=np.array(text_area_data)
            data = pd.DataFrame(a, columns=['a','b','c','d','e','f','g','i'])
            data=data.iloc[0:14,0:8]
            data=scaler.transform(data)
            fore=[]
            # n_future=3
            n_past=14
            fore.append(data[0:n_past,0:data.shape[1]])
            fore=np.array(fore)
            def for5(fore):
                ff=achankovil_model.predict(fore)
                #l=ff.tolist()
                forcasted = np.repeat(ff.reshape(-1,1),8, axis=1)
                precip_for = scaler.inverse_transform(forcasted)[:, 7]
                return precip_for
            
            kk=for5(fore)
            print(kk)
        elif session['id'] == 3 :
            manimala_model = load_model('final_mAanimala_gru.h5')
            dt=pd.read_csv('manimala_combined.csv')

            scaler=MinMaxScaler()
            scaler=scaler.fit(dt)
            a=np.array(text_area_data)
            data = pd.DataFrame(a, columns=['a','b','c','d','e','f','g','i'])
            data=data.iloc[0:14,0:8]
            data=scaler.transform(data)
            fore=[]
            # n_future=3
            n_past=14
            fore.append(data[0:n_past,0:data.shape[1]])
            fore=np.array(fore)
            def for5(fore):
                ff=manimala_model.predict(fore)
                #l=ff.tolist()
                forcasted = np.repeat(ff.reshape(-1,1),8, axis=1)
                precip_for = scaler.inverse_transform(forcasted)[:, 7]
                return precip_for
            
            kk=for5(fore)
            print(kk)   
        elif session['id'] == 4 :
            periyar_model = load_model('final_periyar_gru.h5')
            dt=pd.read_csv('periyar_combined.csv')

            scaler=MinMaxScaler()
            scaler=scaler.fit(dt)
            a=np.array(text_area_data)
            data = pd.DataFrame(a, columns=['a','b','c','d','e','f','g','i'])
            data=data.iloc[0:14,0:8]
            data=scaler.transform(data)
            fore=[]
            # n_future=3
            n_past=14
            fore.append(data[0:n_past,0:data.shape[1]])
            fore=np.array(fore)
            def for5(fore):
                ff=periyar_model.predict(fore)
                #l=ff.tolist()
                forcasted = np.repeat(ff.reshape(-1,1),8, axis=1)
                precip_for = scaler.inverse_transform(forcasted)[:, 7]
                return precip_for
            
            kk=for5(fore)
            print(kk) 
        elif session['id'] == 5 :
            pampa_model = load_model('final_pampa_lstm.h5')
            dt=pd.read_csv('pampa_combined.csv')

            scaler=MinMaxScaler()
            scaler=scaler.fit(dt)
            a=np.array(text_area_data)
            data = pd.DataFrame(a, columns=['a','b','c','d','e','f','g','i'])
            data=data.iloc[0:14,0:8]
            data=scaler.transform(data)
            fore=[]
            # n_future=3
            n_past=14
            fore.append(data[0:n_past,0:data.shape[1]])
            fore=np.array(fore)
            def for5(fore):
                ff=pampa_model.predict(fore)
                #l=ff.tolist()
                forcasted = np.repeat(ff.reshape(-1,1),8, axis=1)
                precip_for = scaler.inverse_transform(forcasted)[:, 7]
                return precip_for
            
            kk=for5(fore)
            print(kk)
        elif session['id'] == 6:
            meenachil_model = load_model('final_meenachil_GRU_final.h5')
            dt=pd.read_csv('meenachil_finnal.csv')

            scaler=MinMaxScaler()
            scaler=scaler.fit(dt)
            a=np.array(text_area_data)
            data = pd.DataFrame(a, columns=['a','b','c','d','e','f','g','i'])
            data=data.iloc[0:14,0:8]
            
            data=scaler.transform(data)
            fore=[]
            # n_future=3
            n_past=14
            fore.append(data[0:n_past,0:8])
            fore=np.array(fore)
            def for5(fore):
                ff=meenachil_model.predict(fore)
                forcasted = np.repeat(ff.reshape(-1,1),8, axis=1)
                precip_for = scaler.inverse_transform(forcasted)[:, 7]
                print(precip_for)
                return precip_for

            kk=for5(fore)
            print(kk)
        elif session['id'] == 7 :
            muvattupuzha_model = load_model('final_muvattupuzha_gru.h5')
            dt=pd.read_csv('muvattupuzha_final.csv')

            scaler=MinMaxScaler()
            scaler=scaler.fit(dt)
            a=np.array(text_area_data)
            data = pd.DataFrame(a, columns=['a','b','c','d','e','f','g','i'])
            data=data.iloc[0:14,0:8]
            data=scaler.transform(data)
            fore=[]
            # n_future=3
            n_past=14
            fore.append(data[0:n_past,0:data.shape[1]])
            fore=np.array(fore)
            def for5(fore):
                ff=muvattupuzha_model.predict(fore)
                #l=ff.tolist()
                forcasted = np.repeat(ff.reshape(-1,1),8, axis=1)
                precip_for = scaler.inverse_transform(forcasted)[:, 7]
                return precip_for
            
            kk=for5(fore)
            print(kk)

        a=round(kk[0],2)
        b=round(kk[1],2)
        c=round(kk[2],2)
        maxi = int((max(kk)+100)/10) * 10
        print("a",a)
        print("b",b)
        print("c",c)
        return redirect(url_for('page3', final=a,data=b,date=c,d= current_data, maxi = maxi))
    else:
        return render_template('page2')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    final = request.args.get('final')
    data = request.args.get('data')
    date = request.args.get('date')
    d = request.args.get('d')
    maxi = request.args.get('maxi')
    return render_template('page3.html', final=final, data=data, date=date,d = d,maxi = maxi)
# def page3():
#     final_list = request.args.get('final')
#     print(final_list)
#     return render_template('page3.html', final_list=final_list)


if __name__ == '__main__':
    app.run(debug=True)