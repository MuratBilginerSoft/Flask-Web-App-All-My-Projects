# region Import Lib

from controller.settings.projectlib import *
from controller.settings.routefunctions import *

# endregion

# region Flask Sınıfından Bir Proje Yarat

app = Flask(__name__) # Bir Flask Projesi Yaratıldı.

# endregion

#region Flask App Variables

app.config['DEBUG'] = True

app.static_folder = appConfig["StaticFolder"]
app.secret_key = appConfig["SecretKey"] 

#endregion

# region App Databasae Variables 

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#endregion

# region DB Create

DB.init_app(app) # App üzerinde çalışacak bir SqlAlchemy DB Modeli Yaratıldı.

# endregion

# region Create Class Object

routeFunctionObj = RouteFunction()

# endregion

#region App Route

app.add_url_rule("/", methods = ["GET", "POST"], view_func = routeFunctionObj.Index) # Index
app.add_url_rule("/signin", methods = ["GET", "POST"], view_func = routeFunctionObj.SignIn ) # SignIn
app.add_url_rule("/login", methods = ["GET", "POST"], view_func = routeFunctionObj.Login ) # Login
app.add_url_rule("/dashboard", methods = ["GET", "POST"], view_func = routeFunctionObj.Dashboard ) # Dashboard
app.add_url_rule("/error", methods = ["GET", "POST"], view_func = routeFunctionObj.Error) # Error
app.add_url_rule("/logout", methods = ["GET", "POST"], view_func = routeFunctionObj.Logout) # Logout

# endregion

# region Project Start

appObj = FlaskStart(app, __name__)

appObj.Start()  # Uygulama Başladı.

# endregion
