from skpy import Skype, SkypeChats, SkypeChat

username = "callmeboomberry@gmail.com"
password = "ayrssr8r"
sk = Skype(username, password)

# send message to skype chat
content = "this is auto message from python code"
ch = sk.chats["19:40c026b0b9034c5aa62aa81bf8097ff7@thread.skype"]
# # ch.sendMsg(content)

#try get message from skype chat
# ch = sk.chats["19:40c026b0b9034c5aa62aa81bf8097ff7@thread.skype"]
schat = SkypeChat(id="19:40c026b0b9034c5aa62aa81bf8097ff7@thread.skype")
print(schat)








"""
{
    "19:40c026b0b9034c5aa62aa81bf8097ff7@thread.skype": SkypeGroupChat(
        id="19:40c026b0b9034c5aa62aa81bf8097ff7@thread.skype",
        alerts=True,
        topic="testapi",
        creatorId="live:.cid.5eb7241c00f1b5dc",
        userIds=["live:.cid.5eb7241c00f1b5dc", "parelyit", "live:srisakul.tat"],
        adminIds=["live:.cid.5eb7241c00f1b5dc", "parelyit", "live:srisakul.tat"],
        open=False,
        history=True,
    )
}
"""