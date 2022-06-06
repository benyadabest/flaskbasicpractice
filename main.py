from flask import Flask, render_template, redirect, url_for,request
import random

app = Flask(__name__, template_folder='templates')

#question list
q1 = ("Do you clean after yourself?", "yes")
q2 = ("Do you listen to mama and papa?", "yes")
q3 = ("Do you answer the phone when they call?", "yes")
q4 = ("Do you leave bottle caps around the house?", "no")
q5 = ("What is most important thing?", "family")
succmyD = {
    0: q1,
    1: q2,
    2: q3,
    3: q4,
    4: q5,
}

#randomizing question list
thelist = list(range(0,5))
random.shuffle(thelist)
questionlist = []
answerlist = []
answers = []
for i in thelist:
        questionlist.append(succmyD[i][0])
        answerlist.append(succmyD[i][1])


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        score = 0
        ans0 = request.form['ans0']
        ans1 = request.form['ans1']
        ans2 = request.form['ans2']
        ans3 = request.form['ans3']
        ans4 = request.form['ans4']
        answers = [ans0, ans1, ans2, ans3, ans4]
        for i in range(5):
            if answers[i].lower() != answerlist[i].lower():
                score = score + 1
        return redirect(url_for("score", scre=score))
    else:
        return render_template("home.html", questions=questionlist)

@app.route("/<scre>")
def score(scre):
    return render_template("result.html", score=scre)

if __name__ == "__main__":
    app.run(debug=True)
