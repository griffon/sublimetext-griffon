import sublime, sublime_plugin
import os, string, re


class GriffonSyntaxCommand(sublime_plugin.EventListener):
    """ Attempts to set Griffon Syntax when appropriate. """


    def __init__(self):
        super(GriffonSyntaxCommand, self).__init__()
        self.path = None
        self.name = None
        self.ext  = None
        self.view = None


    def on_load(self, view):
        self.check_syntax(view)


    def on_post_save(self, view):
        self.check_syntax(view)


    def check_syntax(self, view):
        self.view      = view
        self.file_name = view.file_name()

        if not self.file_name: # buffer has never been saved
            return

        self.set_file_variables()

        if self.ext == '.gdoc':
            self.set_syntax('Textile', 'Textile')
            return

        if self.ext == '.gdoc':
            self.set_syntax('GrailsDoc', 'Griffon/Doc')
            return

        if not self.ext == '.groovy':
            return

        if self.is_model():
            self.set_syntax('GriffonMvcArtifact', 'Griffon/MvcArtifact')
        elif self.is_view():
            self.set_syntax('GriffonMvcArtifact', 'Griffon/MvcArtifact')
        elif self.is_controller():
            self.set_syntax('GriffonMvcArtifact', 'Griffon/MvcArtifact')
        elif self.is_service():
            self.set_syntax('GriffonMvcArtifact', 'Griffon/MvcArtifact')
        else:
            self.set_syntax('Groovy', 'Groovy')


    def is_model(self):
        if 'griffon-app/models' in self.path:
            return True
        return False


    def is_view(self):
        if 'griffon-app/views' in self.path:
            return True
        return False


    def is_controller(self):
        if 'griffon-app/controllers' in self.path:
            return True
        return False


    def is_service(self):
        if 'griffon-app/services' in self.path:
            return True
        return False


    def set_file_variables(self):
        self.path = os.path.dirname(self.file_name)
        self.name = os.path.basename(self.file_name).lower()
        self.name, self.ext = os.path.splitext(self.name)


    def set_syntax(self, syntax, path):
        new_syntax = 'Packages/' + path + '/' + syntax + '.tmLanguage'
        self.view.set_syntax_file(new_syntax)
