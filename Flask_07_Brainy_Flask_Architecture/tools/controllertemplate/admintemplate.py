# region Import Lib

from controller.settings.projectlib import *

# endregion

# region TemplateClass Created

class TemplateRoute():

    # region Variable List

    url = "index.html"
    
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