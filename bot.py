from flask import Flask, render_template, request
import Retrieval

app = Flask(__name__)

@app.route('/reply', methods = ['POST'])
def reply():
	msg = str(request.form['msg'])
	retrived_list = Retrieval.main(msg)
	return render_template('reply.html', city = retrived_list[2], temp_c = retrived_list[0], condition = retrived_list[1])

@app.route('/msg')
def msg():
	return render_template('msg.html')


if __name__ == '__main__':
	app.run(debug=True)