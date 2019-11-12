<h1 align="center">
  <img alt="Gympoint" title="Gympoint" src="https://tippin.me/images/20190424_join_logo_trans.png" width="300px" />
</h1>

<h3 align="center">
 "Now you can use lightnework in your applications in a simple and easy to use way".
</h3>

## 🚀 How to use?

1 - Just enter your project folder and download the repository.
```
cd my_project
```
```
git clone https://github.com/capslockone/tippin/
```

2 - Ready now and just import the module for your application

```
import tippin

tippin = Tippin("https://tippin.me/@raphaeltorresme") # insert your tippin page here

newinvoice = tippin.newinvoice(amount=50) # generates a 50 satoshi payment invoice
getinvoice = newinvoice["message"] # get the invoice address

while True:
    if tippin.checktransaction(newinvoice) == True: # check if you hear payment at the generated address
        print("Your invoice has been paid :) ")
        break
        
```

⚠️ Warning you should make a special handling if the internet crashes you can implement this in code :)

Made by Raphael Torres https://twitter.com/raphaeltorresme

Make a donation to the project https://tippin.me/@raphaeltorresme

LICENSE https://github.com/capslockone/tippin/blob/master/LICENSE.md
