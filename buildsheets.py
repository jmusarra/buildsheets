# import the Flask class from the flask module
from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect('/home/jsm/projects/led_build_sheet/buildsheets.db')
cur = conn.cursor()
sql_most_recent = "SELECT * FROM main.meta ORDER BY ship_date DESC LIMIT 3"
cur.execute(sql_most_recent)
a = cur.fetchall()
show_name = a[0][0]
project_manager = a[0][1]
client = a[0][2]
ship_date = a[0][3]
venue = a[0][4]
print(f'Show Name: {show_name}')
print('whoooo')


# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "BEEP BOOP BEEP BOOP"  # return a string

@app.route('/buildsheet')
def welcome():
    return render_template('buildsheet.html')  # render a template

@app.route('/shows')
def get_shows():
    return "make some shows"

@app.route('/playing')
def playing():
    title = "This is fancy Flask title"
    body = "I wrote some text la la la la"
    return render_template('playing.html.jinja', title=title, body=body)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

