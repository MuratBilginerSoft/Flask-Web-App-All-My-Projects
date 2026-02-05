# region Import Lib

from controller.settings.projectlib import *

# endregion

# region Error Class Created

class Error():

    # region Variable List

    url = "main/error/error.html"
    
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