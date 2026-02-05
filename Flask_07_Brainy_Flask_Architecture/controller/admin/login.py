# region Import Lib

from controller.settings.projectlib import *

# endregion

# region LoginClass Created

class Login():

    # region Variable List

    url = "main/guest/login.html"
    
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