# region Import Lib

from controller.settings.projectlib import *

# endregion

# region SignIn Created

class SignIn():

    # region Variable List

    url = "main/guest/signin.html"
    
    # endregion

    # region Get

    def Get(self):

        return render_template(self.url)

    # endregion

    # region Post

    def Post(self):

        return render_template(self.url)

    # endregion

# endregion