from wtforms import Form, BooleanField, StringField, PasswordField, IntegerField, SelectField, validators

fields = {"age": int,
          "job": ["admin.","unknown","unemployed","management","housemaid","entrepreneur","student",
                                       "blue-collar","self-employed","retired","technician","services"],
          "marital": ["married","divorced","single"],
          "education": ["unknown","secondary","primary","tertiary"],
          "default": ["no", "yes"],
          "balance": int,
          "housing": ["no", "yes"],
          "loan": ["no", "yes"],
          "contact": ["unknown", "telephone", "cellular"],
          "day": int,
          "month": ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"],
          "duration": int,
          "campaign": int,
          "pdays": int,
          "previous": int,
          "poutcome": ["unknown", "other", "failure", "success"],
          "y": ["no", "yes"]}

rkws = {"onchange": "{this.fieldChanged}"}
class TrialForm(Form):
	age = IntegerField("Age", render_kw=rkws)
	job = SelectField("job", choices=[(name, name) for name in fields['job']], render_kw=rkws)
	marital = SelectField("marital", choices=[(name, name) for name in fields['marital']], render_kw=rkws)
	education = SelectField("education", choices=[(name, name) for name in fields['education']], render_kw=rkws)
	default = BooleanField("Default", render_kw=rkws)
	balance = IntegerField("Balance", render_kw=rkws)
	housing = BooleanField("Housing", render_kw=rkws)
	loan = BooleanField("Loan", render_kw=rkws)
	contact = SelectField("contact", choices=[(name, name) for name in fields['contact']], render_kw=rkws)
	day = IntegerField("Day", render_kw=rkws)
	month = SelectField("Month", choices=[(name, name) for name in fields['month']], render_kw=rkws)
	duration = IntegerField("Duration", render_kw=rkws)
	campaign = IntegerField("Campaign", render_kw=rkws)
	pdays = IntegerField("Pdays", render_kw=rkws)
	previous = IntegerField("Previous", render_kw=rkws)
	poutcome = SelectField("Poutcome", choices=[(name, name) for name in fields['poutcome']], render_kw=rkws)
