#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request, Response, redirect, url_for
import logging
from logging import Formatter, FileHandler
import os
import qi

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    # Running pepper code
    session = qi.Session()
    try:
        session.connect("tcp://" + "192.168.0.41" + ":" + str(9559))
        system_service = system_service = session.service("ALSystem")
        system_service.shutdown()
    except RuntimeError:
        forward_message = "Can't connect to Naoqi at ip \"" + "192.168.0.41" + "\" on port " + str(9559) +".\n" + "Please check your script arguments. Run with -h option for help."
    # Moving forward code
    forward_message = "Moving Forward..."
    return render_template('pages/placeholder.home.html', forward_message=forward_message);


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')

# Error handlers.

@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
