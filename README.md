PAX Web Scraper & SMS Notifier
---
Basically, this bot downloads the PAX Prime homepage, finds the sections that announces badge availability, and compares it against the current 'soon' div. If it matches, nothing happens and it repeats. If they are different, it sends you a text via the SMS gateway specified in the script. You'll need to find the gateway for your carrier. There's a great big list [here](http://www.ukrainecalling.com/email-to-text.aspx).

Configuration
---
If you're using Gmail, you don't need to worry about changing the SMTP configuration. Anything else and you'll have to change it to use that server. You'll need to provide your username and password for the SMTP server.

For the SMS Gateway, the address you'll be **sending** to will look something like this:

    1234567890@vtext.com for Verizon
    
    0987654321@txt.att.com for AT&T
    
and so on.

After that, you just need to let it run.