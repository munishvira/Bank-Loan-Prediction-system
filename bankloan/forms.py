from django.forms import ModelForm
from . models import approvals

class MyForm(ModelForm):
	class Meta:
		model=approvals
		fields = ['firstname','lastname','Dependants','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term'
			,'Credit_History','Gender','Married','Education','Self_Employed','Property_Area']
