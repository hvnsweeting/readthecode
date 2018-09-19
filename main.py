import importlib
# import os
import sys
import webbrowser

# TODO allow user set binary to open
# TODO display options and allow user use
# we want to open in a web browser, maybe as option
webbrowser._tryorder = [w for w in webbrowser._tryorder
                        if w.lower() != 'macosx']


def cli():
    libname = sys.argv[1]
    lib = importlib.import_module(libname)

    try:
        path = lib.__path__[0]
    except AttributeError:
        path = lib.__file__

    # TODO make this an option
    # if os.path.isfile(path):
    #     path = os.path.dirname(path)
    print('Opening {} '.format(path))
    webbrowser.open_new_tab("file://{}".format(path))
