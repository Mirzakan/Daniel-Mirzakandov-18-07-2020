from application import db

#class model to initilazie database
class Messages(db.Model):
    __tablename__ = 'Messages'
    id = db.Column(db.Integer, primary_key=True)
    senderId = db.Column(db.String(50))
    reciverId = db.Column(db.String(50))
    subject = db.Column(db.String(50))
    message = db.Column(db.Text())
    date = db.Column(db.String(50))

    def __init__(self, senderId, reciverId, subject, message, date):
        self.senderId = senderId
        self.reciverId = reciverId
        self.subject = subject
        self.message = message
        self.date = date 

    def ConvertToJson(msgData):
        dic = {}
        obj = []
        for i in msgData:
            dic = {}
            dic['senderId'] = i.senderId
            dic['reciverId'] = i.reciverId
            dic['subject'] = i.subject
            dic['message'] = i.message
            dic['date'] = i.date
            obj.append(dic)

        messages = {
            'inbox': obj,
            'sent': obj
        }
        return messages

    #converting with out index in dic
    def ConvertToJsonNoDic(msgData):
        dic = {}
        obj = []
        for i in msgData:
            dic = {}
            dic['senderId'] = i.senderId
            dic['reciverId'] = i.reciverId
            dic['subject'] = i.subject
            dic['message'] = i.message
            dic['date'] = i.date
            obj.append(dic)
        return obj  