from flask import Flask, escape, request, jsonify
import ibm_db_dbi
import ibm_db

app = Flask(__name__)

db = 'MOVIE'
hostname = '172.16.114.53'
port = '50002'
userid = 'db2inst2'
pwd = 'password1'

conn_str = 'database={0};hostname={1};port={2};protocol=tcpip;uid={3};pwd={4}'.format(
    db, hostname, port, userid, pwd)
ibm_db_conn = ibm_db.connect(conn_str, '', '')
# Connect using ibm_db_dbi
conn = ibm_db_dbi.Connection(ibm_db_conn)


@app.route('/')
def hello():
    return f'Hello Container World!!'


@app.route('/api/all')
def api():
    # Fetch data using ibm_db_dbi
    select = "SELECT * FROM \"Movie\".\"basics\" FETCH FIRST 100 ROWS ONLY"
    cur = conn.cursor()
    cur.execute(select)
    return jsonify(cur.fetchall())
    cur.close()


@app.route('/api/search/<title>')
def getMovieByTitle(title):
    # Fetch data using ibm_db_dbi
    select = "SELECT  * FROM \"Movie\".\"basics\" WHERE \"primaryTitle\" like '{}%'".format(
        title)
    cur = conn.cursor()
    cur.execute(select)
    return jsonify(cur.fetchall())
    cur.close()


@app.route('/api/movies')
def getMovies():
    # Fetch data using ibm_db_dbi
    select = "SELECT  * FROM \"Movie\".\"basics\" WHERE \"titleType\" = \'movie\' FETCH FIRST 100 ROWS ONLY "
    cur = conn.cursor()
    cur.execute(select)
    return jsonify(cur.fetchall())
    cur.close()


@app.route('/api/tvseries')
def getTvseries():
    # Fetch data using ibm_db_dbi
    select = "SELECT  * FROM \"Movie\".\"basics\" WHERE \"titleType\" = \'tvSeries\' FETCH FIRST 100 ROWS ONLY"
    cur = conn.cursor()
    cur.execute(select)
    return jsonify(cur.fetchall())
    cur.close()


if __name__ == "__main__":
    app.run(host='localhost', port=8088)
