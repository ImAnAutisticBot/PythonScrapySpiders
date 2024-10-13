from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def connect_syllabi_db(db_name):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn

def connect_faculty_db():
    conn = sqlite3.connect('faculty.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/<tablename>/', methods=['GET'])
def get_all_from_table(tablename):
    conn = connect_syllabi_db('syllabi.db')
    cursor = conn.cursor()
    tablename = tablename.lower()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tablename,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"error": "Table not found"}), 404

    cursor.execute(f"SELECT * FROM {tablename}")
    rows = cursor.fetchall()

    table_data = [dict(row) for row in rows]
    conn.close()

    return jsonify(table_data)

@app.route('/<tablename>/<identifier>', methods=['GET'])
def get_by_id(tablename, identifier):
    conn = connect_syllabi_db('syllabi.db')
    cursor = conn.cursor()
    tablename = tablename.lower()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tablename,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"error": "Table not found"}), 404

    identifier = identifier.upper()

    # 使用相应的列名进行查询
    cursor.execute(f"SELECT * FROM {tablename} WHERE Course_Number = ?", (identifier,))
    row = cursor.fetchone()

    if row:
        row_dict = dict(row)
        conn.close()
        return jsonify(row_dict)  # 返回完整的行数据
    else:
        conn.close()
        return jsonify({"error": "Record not found"}), 404

@app.route('/prof/', methods=['GET'])
def get_all_from_faculty_table():
    conn = connect_faculty_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM CSEFaculty")
    rows = cursor.fetchall()

    faculty_data = [dict(row) for row in rows]
    conn.close()

    return jsonify(faculty_data)

@app.route('/prof/<professor_name>', methods=['GET'])
def get_faculty_by_name(professor_name):
    conn = connect_faculty_db()
    cursor = conn.cursor()

    # 查询教授的所有信息
    cursor.execute("SELECT * FROM CSEFaculty WHERE Name = ?", (professor_name,))
    row = cursor.fetchone()

    if row:
        professor_data = dict(row)
        ordered_keys = ["Name", "Appointment", "Category", "Address", "Email", "Phone"]
        sorted_professor_data = {key: professor_data[key] for key in ordered_keys if key in professor_data}
        conn.close()
        return jsonify(sorted_professor_data)
    else:
        conn.close()
        return jsonify({"error": "Professor not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
