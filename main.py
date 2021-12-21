# As of December 18th Agera 
from website import create_app
from flask_wtf.csrf import CSRFProtect



app = create_app()
csrf = CSRFProtect(app)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    