from flask import Flask, render_template, request, json, jsonify, flash, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from application import app, db
from application.models import Messages
from application.forms import ComposeEmailForm   

@app.route('/')
@app.route('/index')
def index():
    #getting db data in JSON format
    msgData = Messages.ConvertToJson(Messages.query.all())
    return render_template("index.html", index=True, msgData=msgData, counter=2)

@app.route("/ComposeEmail", methods=["GET","POST"])
def ComposeEmail():
    #saving message to db
    form = ComposeEmailForm()
    if form.validate_on_submit():
        flash(f"Your message has been successfully delivered", "success")
        senderId    =     form.senderId.data
        reciverId   =     form.reciverId.data
        subject     =     form.subject.data
        message     =     form.message.data
        dt          =     datetime.now().replace(microsecond=0).strftime("%m/%d/%Y, %H:%M:%S")
        data = Messages(senderId, reciverId, subject, message, dt)
        db.session.add(data)
        db.session.commit()
        return redirect("/ComposeEmail")
    return render_template("ComposeEmail.html", ComposeEmail=True, title="New Message", form=form)


@app.route("/removeIndex", methods=["POST","GET"])
def removeIndex():
    flash(f"Your message has been successfully removed", "danger")
    senderId    = request.form.get('senderId')
    reciverId   = request.form.get('reciverId')
    date        = request.form.get('date')
    #get and delete a message from db
    index = Messages.query.filter(Messages.senderId==senderId,Messages.reciverId==reciverId,Messages.date==date).first()
    db.session.delete(index)
    db.session.commit()
    return redirect("/index")

@app.route("/getMessages", methods=["POST","GET"])
def getMessages():
    #getting user id and filter table by it
    userId = request.args.get('userId')
    if len(userId) > 0:
        inbox = Messages.ConvertToJsonNoDic(Messages.query.filter(Messages.reciverId==userId).all())
        sent = Messages.ConvertToJsonNoDic(Messages.query.filter(Messages.senderId==userId).all())
        msgDataUpdated = {
            'inbox': inbox,
            'sent': sent
        }
    else:
        #returing all data to table if user not exist
        msgDataUpdated = Messages.ConvertToJson(Messages.query.all())
    return Response(json.dumps(msgDataUpdated), mimetype="application/json")


  