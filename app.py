
from flask import Flask, render_template, request, url_for
import subprocess
import os
import time

app = Flask(__name__)

#subprocess.Popen(['rm',os.path.dirname(os.path.abspath(__file__))+'/main'])
subprocess.Popen(['gcc',os.path.dirname(os.path.abspath(__file__))+'/temp.c','-o','main'])
@app.route('/')
def form():
	return render_template('form_submit.html')


def comp_cmds(lang):
	if lang=='python':
		return subprocess.Popen(['python','main.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	elif lang=='c':
		return subprocess.Popen(['gcc',os.path.dirname(os.path.abspath(__file__))+'/main.c','-o','main'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

@app.route('/compile', methods=['POST'])
def compile():
    name=request.form['language']
    email=request.form['filename']
    src_code=request.form['code']
    if len(src_code)==0:return render_template('404.html')
    f=open('main.c','w')
    f.write(src_code)
    cmd=comp_cmds('c')
    f.close()
    time.sleep(0.7)
    actual=subprocess.Popen(['./main'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    srcode=actual.stdout.read()#request.form['code']
    subprocess.Popen(['rm','main'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #fil=open('srcode.c','w')
    #fil.write(srcode)
    
    #mem=subprocess.Popen(['date'],stdout=subprocess.PIPE)
    
    #out.mem.stdout.read()
    #reader=open('srcode.c','r')
    
    #os.system('./srcode')
    #out=open('output','r')

    #output=out.read()
    #print out
    return render_template('form_action.html', name=name, email=email,code=srcode)

# Run the app :)
if __name__ == '__main__':
    
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)
  # app.run( 
  #       host="0.0.0.0",
  #       port=int("5000")
  # )