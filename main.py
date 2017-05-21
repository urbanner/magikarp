from flask import Flask, render_template
import json
from application import application
import sample
import folders

@application.route('/')
def root():
    return render_template('sample.html')

if __name__ == '__main__':
    application.run(debug=True)
