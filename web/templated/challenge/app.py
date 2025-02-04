from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    blacklist = ['print', 'mro', 'system', 'bash', 'range', 'map', 'curl', 'nc', 'request', 'wget', 'globals', 'render_template', 'namespace', '|join', 'debug', 'cycler', 'application', 'passwd', 'config', 'process', '.__class', 'cat', 'echo', 'head', 'less', 'base64', 'join', 'more', 'tail', 'tac', 'nl', 'awk', 'sed', 'attr']

    
    user_input = request.args.get('input') 
    
    if not user_input:
        return "<h1>Good morning Alphabit member! <br> How can I assist you? Please provide input using ?input=.</h1>"
    
    for bad_word in blacklist:
        if bad_word in user_input:
            print(bad_word)
            return "<h1>Sorry, I can't fulfill that request.</h1>"
    
    response_template = f"<h1>- Here is what you asked for: {user_input}!</h1>"
    return render_template_string(response_template)

