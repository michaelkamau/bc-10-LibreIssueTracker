#!flask/bin/python
from app import app
import os
port = 5000
app.run(host='0.0.0.0', port=port, debug=False)
