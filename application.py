from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

import jinja2


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app-route("/application-form")

    """Show application form and collect user input"""

    return render_template("application-form.html")

@app-route("/application" method=['POST'])

    """Post Application form response and details """

    print "Thank You for submitting the details!"

    firstname = request.form.get(firstname)
    lastname =  request.form.get(lastname)
    jobtitle = request.form.get(jobtitle)
    salary = request.form.get(salary)

    # Return response - Thank you, {{}} {{}}, for applying to be a {{}}. Your
    # minimum salary requirement is {{}} dollars

 return render_template("application-response.html", firstname=firstname, lastname=lastname, jobtitle=jobtitle, salary=salary)



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

