import pandas as pd
import joblib
import csv
from datetime import date

def single_result(data):
	classifier = joblib.load('SVM_Classifier.pkl')
	
	val = classifier.predict_proba([data])
	if val[0][0]<= val[0][1]:
		return f'\nResult: Positive\nBenign: {val[0][0]*100:{0}.{3}}%\nMelignant: {val[0][1]*100:{0}.{3}}%'
	else:
		return f'\nResult: Negative\nBenign: {val[0][0]*100:{0}.{3}}%\nMelignant: {val[0][1]*100:{0}.{3}}%'

def multiple_result(address):
	classifier = joblib.load('SVM_Classifier.pkl')
	
	df = pd.read_csv(address)
	ID = df.iloc[:,0].values
	data = df.iloc[:,1:].values
	today = date.today()
	with open('Prediction Results['+str(today)+'].csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['ID','Result','Benign %','Melignant %'])
			    
		for i in range(len(ID)):
			val = classifier.predict_proba( [data[i]] )
			        
			if val[0][0] <= val[0][1]:
				writer.writerow([ID[i],'Positive', f'{val[0][0]*100:{0}.{3}}%', f'{val[0][1]*100:{0}.{3}}%'])
			else:
				writer.writerow([ID[i],'Negative', f'{val[0][0]*100:{0}.{3}}%', f'{val[0][1]*100:{0}.{3}}%'])
	return 'Prediction Result file has been created'