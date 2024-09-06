from flask import Flask, render_template, redirect, url_for, request, send_file
from CreateBill import CreateBill

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/docx', methods=["GET", "POST"])
def document():
	if request.method == 'POST':
		invoice = CreateBill(
			billNo=request.form['bill_no'],
			brand = request.form['brand'],
			showroom = request.form['showroom'],
			address = request.form['address'],
			mobile = request.form['mobile'],
			board = request.form['board']
		)

		invoice_file = invoice.save_to_bytes()
		return send_file(invoice_file, as_attachment=True, download_name="bill.docx", mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
		return redirect(url_for("index"))

	else:
		return render_template('new.html')


if __name__ == "__main__":
	app.run()