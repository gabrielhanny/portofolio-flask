from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/works")
def works():
    return render_template("works.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/components")
def components():
    return render_template("components.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

# # ✅ Halaman dinamis (jangan dipakai kalau semua sudah hardcoded)
# @app.route("/<string:page_name>")
# def html_page(page_name):
#     return render_template(f"{page_name}.html")

# ✅ Simpan ke CSV
def write_to_csv(data):
    with open('database.csv', mode='a',newline='',encoding='utf-8') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email, subject, message])

# ✅ Form handler
@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou")
        except Exception as e:
            print("Error:", e)
            return "did not save to database"
    else:
        return "Something went wrong"

if __name__ == "__main__":
    app.run(debug=True)
