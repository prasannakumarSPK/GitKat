from flask import Flask, render_template, request, jsonify
import csv
import requests
from requests.auth import HTTPBasicAuth


app = Flask(__name__)
@app.route('/')
def index():
	return render_template('form.html')



@app.route('/execute', methods=['POST'])
def execute():
	RollNo = request.form['name']
	with open('data/GitRepos.csv') as csvfile:
		readCSV = csv.reader(csvfile,delimiter=',')
		for row in readCSV:
			# print("****welcome")
			rollno = row[2]
			git_user = row[3]
			if(RollNo==rollno  and IsValidRepositoryExist(git_user)):
				
				lst = GetNamesOfRepositorys(git_user)
				print(lst)
				res=""
				# <a href="https://www.w3schools.com" target="_blank"
				x=" target="
				y = x+"_blank"
				path="<a href="+"https://github.com/"
				for e in lst:
					print("enter here")
					a = "<h3>"+path+git_user+"/"+e+y+">"+e+"</a>"+"</h3>"
					res+=a
				# res='prasannakumarSPK'
				return jsonify({'name' : res})
				# return jsonify({'name' : lst[0]})

			else:
				continue
	

	return jsonify({'error' : 'Missing data!'})

def GetNamesOfRepositorys(gitUserName):
		lst=[]
		#Note:in github /repos contains entire details of all repositories(for more Details refer Git docs )
		response = requests.get(url="https://api.github.com/users/"+gitUserName+"/repos",
			auth=HTTPBasicAuth('prasannakumarSPK','c5461dfa58f3ecdac04cc2b83db890e64b3ee75a'))
		for e in response.json():
			lst.append(e['name'])

		return lst



def IsValidRepositoryExist(gitUserName):
	response = requests.get(url="https://api.github.com/users/"+gitUserName,
	auth=HTTPBasicAuth('prasannakumarSPK','c5461dfa58f3ecdac04cc2b83db890e64b3ee75a'))#here we go to github data 
	Data = response.json() #the data is taken as json
	if "message" in Data:#if invalid or not given any username for git then it shows "message": "Not Found"
		return False
	return True

if __name__ == '__main__':
	app.run(debug=True)