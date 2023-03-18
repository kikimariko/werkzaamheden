import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()

#met name de functies add_data en edit_task_data doen me een beetje duizelen. Hier zal vast een betere oplossing voor zijn
#ik heb een sqlite3 database genomen omdat die in het voorbeeld zit dat ik volg, niet omdat ik hier nou per se heel handig in ben.

def create_tabel():
    c.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT,task_kind TEXT,task_material TEXT, task_square REAL, task_status TEXT, task_due_date DATE, task_bill_date DATE, task_special TEXT, task_budget REAL, task_bill REAL)')

def add_data(task, task_kind, task_material, task_square, task_status, task_due_date, task_bill_date, task_special, task_budget, task_bill):
    c.execute('INSERT INTO taskstable(task, task_kind, task_material, task_square, task_status, task_due_date, task_bill_date, task_special, task_budget, task_bill) VALUES (?,?,?,?,?,?,?,?,?,?)',(task, task_kind, task_material, task_square, task_status, task_due_date, task_bill_date, task_special, task_budget, task_bill))
    conn.commit()

def view_all_data():
    c.execute('SELECT * FROM taskstable')
    data = c.fetchall()
    return data

def view_unique_tasks():
    c.execute('SELECT DISTINCT task FROM taskstable')
    data = c.fetchall()
    return data

def get_task(task):
    c.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
    data = c.fetchall()
    return data

def edit_task_data(new_task, new_task_kind, new_task_material, new_task_square, new_task_status, new_task_due_date, new_task_bill_date, new_task_special, new_task_budget, new_task_bill, task, task_kind, task_material, task_square, task_status, task_due_date, task_bill_date, task_special, task_budget, task_bill):
    c.execute("UPDATE taskstable SET task =?,task_kind =?,task_material =?,task_square =?,task_status =?,"
              "task_due_date =?,task_bill_date =?,task_special =?,task_budget =?, task_bill =? WHERE task=? and "
              "task_kind=? and task_material=? and task_square=? and task_status=? and task_due_date=? and "
              "task_bill_date=? and task_special=? and task_budget=? and task_bill=? ",(new_task, new_task_kind,
                                                                                        new_task_material,
                                                                                        new_task_square,
                                                                                        new_task_status,
                                                                                        new_task_due_date,
                                                                                        new_task_bill_date,
                                                                                        new_task_special,
                                                                                        new_task_budget,
                                                                                        new_task_bill, task,
                                                                                        task_kind, task_material,
                                                                                        task_square, task_status,
                                                                                        task_due_date,
                                                                                        task_bill_date, task_special,
                                                                                        task_budget, task_bill))
    conn.commit()
    data =c.fetchall()
    return data