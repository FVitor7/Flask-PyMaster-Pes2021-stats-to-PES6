import os
from pymaster.app import create_app


app = create_app()


if __name__ == '__main__':
    port = float(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run(debug=True)
