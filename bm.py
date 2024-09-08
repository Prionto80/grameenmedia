from flask import Flask, render_template, redirect, url_for, request, send_file, jsonify
from CreateBill import CreateBill
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/docx', methods=["GET", "POST"])
def document():
	if request.method == 'POST':
		bill_no=request.form['bill_no']
		showroom=request.form['showroom']
		invoice = CreateBill(
			billNo=bill_no,
			brand = request.form['brand'],
			showroom = showroom,
			address = request.form['address'],
			mobile = request.form['mobile'],
			board = request.form['board']
		)

		invoice_file = invoice.save_to_bytes()
		return send_file(invoice_file, as_attachment=True, download_name=f"{bill_no} {showroom}.docx", mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
		return redirect(url_for("index"))

	else:
		return render_template('new.html')

@app.route('/submit', methods=["POST"])
def mobile():
	data = request.get_json()
	sno = data.get('sno')
	brand = data.get('brand')
	show = data.get('show')
	addr = data.get('addr')
	mob = data.get('mob')
	board = data.get('board')
	invoice = CreateBill(
			billNo = sno,
			brand = brand,
			showroom = show,
			address = addr,
			mobile = mob,
			board = board,
		)
	invoice_file = invoice.save_to_bytes()
	return send_file(invoice_file, as_attachment=True, download_name=f"{sno} {show}.docx", mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
