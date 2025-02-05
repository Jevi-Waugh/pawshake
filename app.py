from flask import Flask, render_template, request  # importing Flask class
app = Flask(__name__)  # setting this variable to __name__ a special

@app.route('/continue', methods=["GET", "POST"])
def play():
    cost1 = 0
    dogService = int(request.form['dogService'])
    WeeklyWalk = int(request.form['WeeklyWalk'])
    PreferredD = str(request.form['PreferredD'])
    FName = request.form['FName']
    LName = request.form['LName']
    PNum = request.form['PNum']
    EmailAd = request.form['EmailAd']
    Street = request.form['Street']
    SuBurb = request.form['SuBurb']
    PCode = request.form['PCode']
    WalkT = request.form['WalkT']
    if request.method == "POST":
        if dogService == 1 and WeeklyWalk < 6:
            cost1 = WeeklyWalk * 20
        elif dogService == 1 and WeeklyWalk > 5:
            cost1 = WeeklyWalk *18
        elif dogService == 2 and WeeklyWalk < 6:
            cost1 = WeeklyWalk * 30
        elif dogService == 2 and WeeklyWalk > 5:
            cost1 = WeeklyWalk * 28
        elif dogService == 3 and WeeklyWalk < 4:
            cost1 = WeeklyWalk * 38
        elif dogService == 3 and WeeklyWalk > 3 < 6:
            cost1 = WeeklyWalk * 36
        elif dogService == 3 and WeeklyWalk > 5:
            cost1 = WeeklyWalk * 34
        elif dogService == 4 and WeeklyWalk < 4:
            cost1 = WeeklyWalk * 42
        elif dogService == 4 and WeeklyWalk > 3 < 6:
            cost1 = WeeklyWalk * 40
        elif dogService == 4 and WeeklyWalk > 5:
            cost1 = WeeklyWalk * 38
        elif dogService == 5 and WeeklyWalk < 6:
            cost1 = WeeklyWalk * 20
        elif dogService == 5 and WeeklyWalk > 5:
            cost1 = WeeklyWalk * 18
        elif dogService == 6 and WeeklyWalk < 6:
            cost1 = WeeklyWalk * 30
        elif dogService == 6 and WeeklyWalk > 5:
            cost1 = WeeklyWalk * 28
        
        if dogService == 1:
            dogService = str("0.5 hour private walk (1 dog)")
        elif dogService == 2:
            dogService = str("1 hour private walk (1 dog)")
        elif dogService == 3:
            dogService = str("1 hour group walk (2 dogs)")
        elif dogService == 4:
            dogService = str("1 hour group walk (3 dogs)")
        elif dogService == 5:
            dogService = str("0.5 hour pet visit (less than four dogs permitted)")
        elif dogService == 6:
            dogService = str("1 hour pet visit (less than four dogs permitted)")

        if WeeklyWalk == 1:
            WeeklyWalk = str("once")
        elif WeeklyWalk == 2:
            WeeklyWalk = str("twice")
        elif WeeklyWalk == 3:
            WeeklyWalk = str("thrice")
        elif WeeklyWalk == 4:
            WeeklyWalk = str("4 times a week")
        elif WeeklyWalk == 5:
            WeeklyWalk = str("5 times a week")
        elif WeeklyWalk == 6:
            WeeklyWalk = str("6 times a week")
        elif WeeklyWalk == 7:
            WeeklyWalk = str("7 times a week")


        return render_template("booking.html", PreferredD=PreferredD, WalkT=WalkT, 
        FName=FName, LName=LName, cost1=cost1, dogService=dogService, WeeklyWalk=WeeklyWalk, 
        PNum=PNum,EmailAd=EmailAd,Street=Street,SuBurb=SuBurb,PCode=PCode,  play=True)
    else:
        return "Something went wrong"

@app.route('/request', methods=["GET", "POST"])
def play1():
    fques = request.form['fques']
    email2ad = request.form['email2ad']
    orques = request.form['orques']
    binfo = request.form['binfo']
    sub = request.form['sub']
    des = request.form['des']

    return render_template("contactus.html", fques=fques, email2ad=email2ad, orques=orques, binfo=binfo,
     sub=sub,des=des, play1=True)

@app.route('/booking')
def booking():
    return render_template("booking.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/contactus')
def contactus():
    return render_template("contactus.html")


# - - - - - - starts here - - - - - - - - - - - - -
@app.route('/')
def index():
    return render_template("landing.html")

if __name__ == '__main__':
    app.run()


