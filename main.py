from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)

app.config['DEBUG'] = True

#This portion turned into form.html:
#form = """
#<!DOCTYPE html>
#<html>
#    <body>
#        <form action="/user-signup" method="post">
            # label's 'for' matches input's 'id'
#            <label for="Username">Username</label>
#            <input id="Username" type="text" name="user_name_entry"/>
#etc, etc, etc...
#        </form>
#    </body>
#</html>
#"""

@app.route("/user-signup", methods=['POST'])
def sign_up():
    username = request.form['user_name_entry']
    passphrase = request.form['pass_entry1']
    passconfirmation = request.form['pass_entry2']
    email_py = request.form['email_entry']

# this portion checks the username field
    ptag_error1_py=""
    if username == "":
        ptag_error1_py = "This field may not be left blank."
    if not 3 <= len(username) <= 20:
        ptag_error1_py = ptag_error1_py + "Username must be between 3 and 20 characters. "
    if " " in username:
        ptag_error1_py = ptag_error1_py + "Username may not have any spaces. "

#this portion checks the password & password verification fields
    ptag_error2_py=""
    if passphrase == "":
        ptag_error2_py = "This field may not be left blank. "
    if not 3 <= len(passphrase) <= 20:
        ptag_error2_py = ptag_error2_py + "Password must be between 3 and 20 characters. "
    if " " in passphrase:
        ptag_error2_py = ptag_error2_py + "Password may not have any spaces. "

    ptag_error3_py=""
    if passconfirmation == "":
        ptag_error3_py = "This field may not be left blank. "
    if not 3 <= len(passconfirmation) <= 20:
        ptag_error3_py = ptag_error3_py + "Password must be between 3 and 20 characters. "
    if passconfirmation != "":
        if " " in passconfirmation:
            ptag_error3_py = ptag_error3_py + "Password may not have any spaces. "
    if passphrase != passconfirmation:
        #redir_error = redir_error + "password entries do not match"
        ptag_error3_py = ptag_error3_py + "Password entries must match. "


#turn this portion into a template set_email.html
    ptag_error4_py =""
    if email_py != "":
        #ptag_error4_py="Although submitting your email is optional, if you decide to submit your email, it must be valid. "
        if "@" not in email_py:
            ptag_error4_py = ptag_error4_py + "There is no '@' in your email. "
        count = 0
        for i in email_py:
            if i =="@":
                count = count + 1
        if count > 1:
            ptag_error4_py = ptag_error4_py + "You may only have one '@' in your email. "

        if "." not in email_py:
            ptage_error4_py = ptag_error4_py + "There is no '.' in your email. "
        count = 0
        #it is common for emails to have more than one '.', so consider removing the requirement of a "single '.'"
        for i in email_py:
            if i ==".":
                count = count + 1
        if count > 1:
            ptag_error4_py = ptag_error4_py + "You may only have one '.' in your email. "
        if not 3 <= len(email_py) <= 20:
            ptag_error4_py = ptag_error4_py + "Email must be between 3 and 20 characters. "
        if " " in email_py:
            ptag_error4_py = ptag_error4_py + "Username may not have any spaces. "
        if ptag_error4_py != "":
            ptag_error4_py= ptag_error4_py + "Although submitting your email is optional, if you decide to submit your email, it must be valid. "
        
    errors = ptag_error1_py + ptag_error2_py + ptag_error3_py + ptag_error4_py
    if errors == "":
        #direct to welcome page displaying "Welcome, [username]!"
        return render_template('welcome.html', username_html = username)
        #return redirect("/welcome")

    if errors != "":
        #return redirect("/?error=" + redir_error)
        return render_template('form.html', methods= ('post'), ptag_error1_html = ptag_error1_py,
            ptag_error2_html = ptag_error2_py, ptag_error3_html = ptag_error3_py,
            ptag_error4_html = ptag_error4_py, user_val = username, email_val = email_py)

#@app.route("/welcome", methods=['POST'])
#def welcome():
#    username = "(get username from Sign-Up)"
#    return render_template('welcome.html', methods = ('post'), username_html = username)

@app.route("/")
def index():
    return render_template('form.html')
app.run()