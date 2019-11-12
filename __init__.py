#!/usr/bin/env python3

import requests
import re

class Tippin():

    def __init__(self, yourtippin):

        self.yourtippin = yourtippin

        self.request = requests.get(self.yourtippin)
        self.cookies = self.request.cookies
        
    def userid(self):
        return re.findall("var_userid = [\d]+;", self.request.text)[0].replace('var_userid = ','').replace(';','')

    def username(self):
        return self.yourtippin[19:]

    def newinvoice(self, amount=0):

        payload = {
            "userid" : self.userid(), "username" : self.username() , 
            "userplan" : "", "istaco" : 0, "customAmnt" : 0, "customMemo" : "", "customSat": amount
            }
 
        Json = str(requests.post("https://tippin.me/lndreq/newinvoice.php", cookies=self.cookies, data=payload).text)

        Json = Json.replace("true","True")
        Json = Json.replace("false","False")

        return eval(Json)

    def checktransaction(self, invoicejson):

        payload = {"rhash" : invoicejson["rhash"], "node_id" : "1"}

        Json = requests.post("https://tippin.me/lndreq/lookupinvoice.php", cookies=self.cookies, data=payload).text
        Json = Json.replace("false","False")
        Json = Json.replace("true","True")

        return eval(Json)["settled"] == True


