from flask import  *
import sqlite3
app = Flask(__name__)
app.secret_key = "abc"


#---------------------------------------------------------------------------------------------------

#           "creating database and table"
try:
    con=sqlite3.connect('marks.db')
    print("Database opened successfully")
    con.execute("create table StudentMarks(rank integer primary key autoincrement,roll integer unique,name TEXT ,maths_marks integer,physics_marks integer,chemistry_marks integer,total_marks integer,average integer)")
    print("Table created successfully")
    con.close()
except:
    pass

#---------------------------------------------------------------------------------------------------

#          "creating route for opening Homepage"

@app.route('/',methods=['GET','POST'])
def Home():
    return render_template("Homepage.html")
#------------------------------------------------------------------------------------------------------

#          "methods for entering marks"

@app.route('/EnterMarks',methods=['GET','POST'])
def Entermarks():
    return render_template("Enter_marks.html")

@app.route('/save_details',methods=['GET','POST'])
def save_details():
    if request.method =='POST':
        roll=request.form.get('roll')
        name=request.form.get('name')
        name=name[0].upper()+name[1:]
        maths=request.form.get('maths')
        physics=request.form.get('physics')
        chemistry=request.form.get('chemistry')
        total=(int(maths)+int(physics)+int(chemistry))
        avg=round(total/3,2)
        r=save_marks(roll,name,maths,physics,chemistry,total,avg)
        if r==-1:
            m="This Roll Number has already submitted the marks. If you want to update your marks then click update marks"
            l="/EnterMarks"
            ms = '<script type="text/javascript">alert("'+ m + '");location="' + l + '";</script>'
            return ms
        return render_template("Homepage.html")


def save_marks(Roll,name,maths,physics,chemistry,total,avg):
    con=sqlite3.connect("marks.db")
    cur = con.cursor()
    cur1=con.cursor()
    cur1.execute(f'select roll  from StudentMarks where roll={Roll}')
    a=cur1.fetchall()
    if len(a)==0:
        cur.execute(f'insert into StudentMarks(roll,name,maths_marks,physics_marks,chemistry_marks ,total_marks,average) values(?,?,?,?,?,?,?)',(Roll,name, maths, physics, chemistry, total, avg))
        con.commit()
        con.close()
    else:
        return (-1)
    return (1)



#-------------------------------------------------------------------------------------------------------

#                               updating marks when incorrect marks are entered
@app.route('/update_marks',methods=['GET','POST'])
def update():
    return render_template('update_marks.html')

@app.route('/updated_details',methods=['GET','POST'])
def update_details():
    if request.method =='POST':
        roll=request.form.get('roll')
        maths=request.form.get('maths')
        physics=request.form.get('physics')
        chemistry=request.form.get('chemistry')
        total=(int(maths)+int(physics)+int(chemistry))
        avg=round(total/3,2)
        r=update_marks(roll,maths,physics,chemistry,total,avg)
        if r==-1:
            m="This Roll Number doesn't exist."
            l="/update_marks"
            ms = '<script type="text/javascript">alert("' + m + '");location="' + l + '";</script>'
            return ms
        return render_template("Homepage.html")


def update_marks(Roll,maths,physics,chemistry,total,avg):
    con=sqlite3.connect("marks.db")
    cur = con.cursor()
    cur1=con.cursor()
    cur1.execute(f'select roll  from StudentMarks where roll={Roll}')
    a=cur1.fetchall()
    if len(a)!=0:
        cur.execute(f'update StudentMarks set maths_marks={maths},physics_marks={physics},chemistry_marks={chemistry},total_marks={total},average={avg} where roll={Roll}')
        con.commit()
        con.close()
    else:
        return (-1)
    return (1)

#--------------------------------------------------------------------------------------------------------

#                 "method for leaderboard"

@app.route('/Leaderboard',methods=['GET','POST'])

def Leaderboard():
    con = sqlite3.connect("marks.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from StudentMarks order by average desc")
    rows = cur.fetchall()
    return render_template("LeaderBoard.html", rows=rows)

#---------------------------------------------------------------------------------------------------------

#                                 "sorting and searching methods"
@app.route("/sort_by_name",methods=['GET','POST'])
def Leaderboard1():
    con = sqlite3.connect("marks.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from StudentMarks order by name asc")
    rows = cur.fetchall()
    return render_template("LeaderBoard.html", rows=rows)

@app.route("/sort_by_RollNumber",methods=['GET','POST'])
def Leaderboard2():
    con = sqlite3.connect("marks.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from StudentMarks order by roll asc")
    rows = cur.fetchall()
    return render_template("LeaderBoard.html", rows=rows)

@app.route("/search_by_RollNumber" ,methods=['POST','GET'])
def Leaderboard3():
    rollnumber= request.form.get('roll')
    con = sqlite3.connect("marks.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(f"select * from StudentMarks where roll={rollnumber}")
    rows = cur.fetchall()
    if len(rows)>0:
        return render_template("LeaderBoard.html", rows=rows)
    else:
        flash("'Roll Number not found'")
        return render_template("LeaderBoard.html")





#----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
