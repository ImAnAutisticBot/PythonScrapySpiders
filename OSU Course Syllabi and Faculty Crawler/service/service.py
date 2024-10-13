from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect('syllabi.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/<tablename>/', methods=['GET'])
def get_all_from_table(tablename):
    conn = connect_db()
    cursor = conn.cursor()

    # 验证表是否存在
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tablename,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"error": "Table not found"}), 404

    # 查询表中的所有数据
    cursor.execute(f"SELECT * FROM {tablename}")
    rows = cursor.fetchall()

    # 将数据转换为 JSON 格式返回
    table_data = [dict(row) for row in rows]
    conn.close()

    return jsonify(table_data)

@app.route('/<tablename>/<identifier>', methods=['GET'])
def get_by_id(tablename, identifier):
    conn = connect_db()
    cursor = conn.cursor()

    # 验证表是否存在
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tablename,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"error": "Table not found"}), 404

    # 根据 identifier 查询匹配的行
    cursor.execute(f"SELECT * FROM {tablename} WHERE course_id = ?", (identifier,))
    row = cursor.fetchone()

    if row:
        # 获取后两个字段的数据
        row_dict = dict(row)
        last_two_columns = list(row_dict.values())[-2:]
        conn.close()
        return jsonify(last_two_columns)
    else:
        conn.close()
        return jsonify({"error": "Record not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
