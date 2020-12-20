import logging

from users_base_app import app


if __name__ == "__main__":
    logging.warning("Starting application in debug-mode. "
                    "Note that this mode is only recommended for development purposes")
    app.run(debug=True, port=5001)