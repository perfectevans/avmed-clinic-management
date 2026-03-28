from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'avmedclinicc.db'

def get_db():
    conn = sqlite3.connect(DATABASE, timeout=10, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

# ---------------- UNIT ----------------
@app.route('/unit/add', methods=['GET', 'POST'])
def add_unit():
    if request.method == 'POST':
        unit_id = request.form['unit_id']
        name = request.form['name']
        with get_db() as conn:
            conn.execute("INSERT INTO Unit (Unit_ID, Unit_Name) VALUES (?, ?)", (unit_id, name))
        return redirect(url_for('list_unit'))
    return render_template('unit_add.html')

@app.route('/unit/list')
def list_unit():
    with get_db() as conn:
        units = conn.execute("SELECT * FROM Unit").fetchall()
    return render_template('unit_list.html', units=units)

# ---------------- DOCTOR ----------------
@app.route('/doctor/add', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        name = request.form['name']
        gender = request.form['gender']
        specialization = request.form['specialization']
        license_number = request.form['license_number']
        position = request.form['position']
        call_duty_status = request.form['call_duty_status']
        unit_id = request.form['unit_id']
        with get_db() as conn:
            conn.execute("""
                INSERT INTO Doctor 
                (Doctor_ID, Name, Gender, Specialization, License_Number, Position, Call_Duty_Status, Unit_ID)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (doctor_id, name, gender, specialization, license_number, position, call_duty_status, unit_id))
        return redirect(url_for('list_doctor'))
    return render_template('doctor_add.html')

@app.route('/doctor/list')
def list_doctor():
    with get_db() as conn:
        doctors = conn.execute("SELECT * FROM Doctor").fetchall()
    return render_template('doctor_list.html', doctors=doctors)

# ---------------- NURSE ----------------
@app.route('/nurse/add', methods=['GET', 'POST'])
def add_nurse():
    if request.method == 'POST':
        nurse_id = request.form['nurse_id']
        name = request.form['name']
        gender = request.form['gender']
        qualification = request.form['qualification']
        license_number = request.form['license_number']
        shift = request.form['shift']
        position = request.form['position']
        call_duty_status = request.form['call_duty_status']
        unit_id = request.form['unit_id']
        with get_db() as conn:
            conn.execute("""
                INSERT INTO Nurse 
                (Nurse_ID, Name, Gender, Qualification, License_Number, Shift, Position, Call_Duty_Status, Unit_ID)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (nurse_id, name, gender, qualification, license_number, shift, position, call_duty_status, unit_id))
        return redirect(url_for('list_nurse'))
    return render_template('nurse_add.html')

@app.route('/nurse/list')
def list_nurse():
    with get_db() as conn:
        nurses = conn.execute("SELECT * FROM Nurse").fetchall()
    return render_template('nurse_list.html', nurses=nurses)

# ---------------- PATIENT ----------------
@app.route('/patient/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        name = request.form['name']
        age = request.form['age']
        sex = request.form['sex']
        dob = request.form['date_of_birth']
        address = request.form['address']
        phone = request.form['phone_number']
        next_of_kin = request.form['next_of_kin']
        registration_date = request.form['registration_date']
        condition_type = request.form['condition_type']
        hmo_id = request.form['hmo_id']
        with get_db() as conn:
            conn.execute("""
                INSERT INTO Patient 
                (Patient_ID, Name, Age, Sex, Date_of_Birth, Address, Phone_Number, Next_of_Kin, Registration_Date, Condition_Type, HMO_ID)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (patient_id, name, age, sex, dob, address, phone, next_of_kin, registration_date, condition_type, hmo_id))
        return redirect(url_for('list_patient'))
    return render_template('patient_add.html')

@app.route('/patient/list')
def list_patient():
    with get_db() as conn:
        patients = conn.execute("SELECT * FROM Patient").fetchall()
    return render_template('patient_list.html', patients=patients)

# ---------------- HMO ----------------
@app.route('/hmo/add', methods=['GET', 'POST'])
def add_hmo():
    if request.method == 'POST':
        hmo_id = request.form['hmo_id']
        name = request.form['name']
        position = request.form['position']
        email = request.form['email']
        is_head = request.form['is_head']
        with get_db() as conn:
            conn.execute("""
                INSERT INTO HMO (HMO_ID, Name, Position, Email, Is_Head)
                VALUES (?, ?, ?, ?, ?)
            """, (hmo_id, name, position, email, is_head))
        return redirect(url_for('list_hmo'))
    return render_template('hmo_add.html')

@app.route('/hmo/list')
def list_hmo():
    with get_db() as conn:
        hmos = conn.execute("SELECT * FROM HMO").fetchall()
    return render_template('hmo_list.html', hmos=hmos)

# ---------------- APPOINTMENT ----------------
@app.route('/appointment/add', methods=['GET', 'POST'])
def add_appointment():
    if request.method == 'POST':
        appointment_id = request.form['appointment_id']
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        date = request.form['date']
        time = request.form['time']
        status = request.form['status']
        booking_source = request.form['booking_source']
        with get_db() as conn:
            conn.execute("""
                INSERT INTO Appointment 
                (Appointment_ID, Patient_ID, Doctor_ID, Date, Time, Status, Booking_Source)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (appointment_id, patient_id, doctor_id, date, time, status, booking_source))
        return redirect(url_for('list_appointment'))
    return render_template('appointment_add.html')

@app.route('/appointment/list')
def list_appointment():
    with get_db() as conn:
        appointments = conn.execute("SELECT * FROM Appointment").fetchall()
    return render_template('appointment_list.html', appointments=appointments)

# ---------------- VITAL SIGNS ----------------
@app.route('/vitalsigns/add', methods=['GET', 'POST'])
def add_vital_signs():
    if request.method == 'POST':
        vital_id = request.form['vital_id']
        appointment_id = request.form['appointment_id']
        nurse_id = request.form['nurse_id']
        temperature = request.form['temperature']
        pulse = request.form['pulse']
        bp = request.form['blood_pressure']
        respiration_rate = request.form['respiration_rate']
        with get_db() as conn:
            conn.execute("""
                INSERT INTO Vital_Signs 
                (Vital_ID, Appointment_ID, Nurse_ID, Temperature, Pulse, Blood_Pressure, Respiration_Rate)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (vital_id, appointment_id, nurse_id, temperature, pulse, bp, respiration_rate))
        return redirect(url_for('list_vital_signs'))
    return render_template('vital_signs_add.html')

@app.route('/vitalsigns/list')
def list_vital_signs():
    with get_db() as conn:
        vitals = conn.execute("SELECT * FROM Vital_Signs").fetchall()
    return render_template('vital_signs_list.html', vitals=vitals)

# ---------------- PRESCRIPTION ----------------
@app.route('/prescription/add', methods=['GET', 'POST'])
def add_prescription():
    if request.method == 'POST':
        prescription_id = request.form['prescription_id']
        appointment_id = request.form['appointment_id']
        doctor_id = request.form['doctor_id']
        patient_id = request.form['patient_id']
        description = request.form['description']
        date_prescribed = request.form['date_prescribed']
        with get_db() as conn:
            conn.execute("""
                INSERT INTO Prescription 
                (Prescription_ID, Appointment_ID, Doctor_ID, Patient_ID, Description, Date_Prescribed)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (prescription_id, appointment_id, doctor_id, patient_id, description, date_prescribed))
        return redirect(url_for('list_prescription'))
    return render_template('prescription_add.html')

@app.route('/prescription/list')
def list_prescription():
    with get_db() as conn:
        prescriptions = conn.execute("SELECT * FROM Prescription").fetchall()
    return render_template('prescription_list.html', prescriptions=prescriptions)

# ---------------- BILL ----------------
@app.route('/bill/add', methods=['GET', 'POST'])
def add_bill():
    if request.method == 'POST':
        bill_id = request.form['bill_id']
        prescription_id = request.form['prescription_id']
        amount = request.form['amount']
        paid_status = request.form['paid_status']
        payment_date = request.form['payment_date']
        with get_db() as conn:
            conn.execute("""
                INSERT INTO Bill 
                (Bill_ID, Prescription_ID, Amount, Paid_Status, Payment_Date)
                VALUES (?, ?, ?, ?, ?)
            """, (bill_id, prescription_id, amount, paid_status, payment_date))
        return redirect(url_for('list_bill'))
    return render_template('bill_add.html')

@app.route('/bill/list')
def list_bill():
    with get_db() as conn:
        bills = conn.execute("SELECT * FROM Bill").fetchall()
    return render_template('bill_list.html', bills=bills)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)




