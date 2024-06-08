from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)

def create_graph():
    filename = 'demo'

    # random but consistant data
    lst = [2,9,4,6,4]
    x = np.arange(0,len(lst))
    y = np.array(lst)
    z = np.polyfit(x, y, 4)
    p = np.poly1d(z)
    # clear buffer
    plt.clf()
    plt.scatter(x, y, label="data")
    plt.plot( x, p(z), 'r', label="fitted line")
    plt.savefig(f'static/img/{filename}.png')

@app.route('/', methods=['GET'])
def getIndex():
    create_graph()
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)