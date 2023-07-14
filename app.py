from flask import Flask, render_template, url_for, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    passenger_id = request.form['passenger_id']
    password = request.form['password']
    conn = sqlite3.connect('db/passengerdb.db')
    cursor = conn.cursor()
    sql = "select * from passengers where passenger_id = ? and password = ?"
    cursor.execute(sql,(passenger_id,password))
    if cursor.fetchone() is None:
        conn.close()
        return render_template('login.html', login_error="Invalid Passenger ID or Password")
    else:
        conn.close()
        return redirect(url_for('home', passenger_id=passenger_id))

@app.route('/home', methods=['POST','GET'])
def home():
    passenger_id = request.args.get('passenger_id')
    return render_template('home.html', passenger_id=passenger_id)

@app.route('/register_form')
def register_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    passenger_id = request.form['passenger_id']
    conn = sqlite3.connect('db/passengerdb.db')
    cursor = conn.cursor()

    cursor.execute("select * from passengers where passenger_id = ?",(passenger_id,))
    if cursor.fetchone() is not None:
        conn.close()
        return render_template('register.html', reg_error="Passenger ID already exists")
       
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    address = request.form['address']
    phone = request.form['phone']

    sql = "insert into passengers (passenger_id, name, email, password, address, phone) values (?, ?, ?, ?, ?, ?)"
    cursor.execute(sql,(passenger_id,name,email,password,address,phone))
    conn.commit()
    conn.close()
    return redirect(url_for('regsuccess', passenger_id=passenger_id))

@app.route('/regsuccess/<passenger_id>')
def regsuccess(passenger_id):
    return render_template('regsuccess.html', passenger_id=passenger_id)

@app.route('/bookticket', methods=['POST','GET'])
def bookticket():
    passenger_id = request.args.get('passenger_id')
    return render_template('booking.html', passenger_id=passenger_id)

@app.route('/bookticketcheck',methods=['POST'])
def bookticketcheck():
    passenger_id = request.args.get('passenger_id')
    pnr_number = request.form['pnr_number']
    travel_date = request.form['travel_date']
    source_airport = request.form['source_airport']
    destination_airport = request.form['destination_airport']
    ticket_status = request.form['ticket_status']
    seat_preference = request.form['seat_preference']
    meal_preference = request.form['meal_preference']
    
    conn = sqlite3.connect('db/passengerdb.db')
    cursor = conn.cursor()
    sql = "insert into bookings (pnr_number, passenger_id, travel_date, source_airport, destination_airport, status, seat_preference, meal_preference) values (?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(sql,(pnr_number,passenger_id,travel_date,source_airport,destination_airport,ticket_status,seat_preference,meal_preference))
    conn.commit()
    conn.close()
    return redirect(url_for('bookingsuccess',passenger_id=passenger_id,pnr_number=pnr_number))

@app.route('/bookingsuccess')
def bookingsuccess():
    passenger_id = request.args.get('passenger_id')
    pnr_number = request.args.get('pnr_number')
    return render_template('bookingsuccess.html', passenger_id=passenger_id, pnr_number=pnr_number)

@app.route('/view_tickets')
def view_tickets():
    passenger_id = request.args.get('passenger_id')
    conn = sqlite3.connect('db/passengerdb.db')
    cursor = conn.cursor()
    sql = "select * from bookings where passenger_id = ?"
    cursor.execute(sql,(passenger_id,))
    tickets_data = cursor.fetchall()
    print(tickets_data)
    if tickets_data is None:
        return "No tickets booked"
    else:
        return render_template('viewtickets.html', tickets_data=tickets_data, passenger_id=passenger_id)

if __name__ == "__main__":
    #app.run() 
    #use just app.run() if running locally and comment below line and uncomment above line. Below line is for making the app work on zeet
    app.run(debug=False, host='0.0.0.0')