import os
from flaks inmport Flask

app = Flask(__name__)

@app.route('/')
def index():
   return "<h1>Hello There!</h1>"

app.run(host=os.getenv('IP'), os.getenv('PORT')), debug=True)