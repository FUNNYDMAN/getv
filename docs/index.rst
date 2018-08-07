getv
====

getv provides simple way to get last version string from github. It may be useful if you wanna display this info somewhere in your project.

Example usage with Flask
------------------------

.. code-block:: python

    import os

    from flask import Flask

    from getv.main import GetVersion

    app = Flask(__name__)

    getv = GetVersion()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_DIR = os.path.dirname(BASE_DIR)

    PATH_TO_V_FILE = os.path.join(PROJECT_DIR, 'version.txt')


    @app.route('/')
    def index():
        last_v = getv.get_last_version()
        getv.write_or_create_version_file(PATH_TO_V_FILE)
        return 'Project version %s' % last_v


    if __name__ == "__main__":
        app.run()
..

