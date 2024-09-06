from flask import Flask, render_template, redirect, url_for, request, send_file
from CreateBill import CreateBill

app = Flask(__name__)


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
			brand = showroom,
			showroom = request.form['showroom'],
			address = request.form['address'],
			mobile = request.form['mobile'],
			board = request.form['board']
		)

		invoice_file = invoice.save_to_bytes()
		return send_file(invoice_file, as_attachment=True, download_name=f"{bill_no} {showroom}.docx", mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

	else:
		return render_template('new.html')


if __name__ == "__main__":
	app.run()
