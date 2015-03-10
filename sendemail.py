import smtplib
fromaddr = 'addr'
toaddr = 'addr'
to = ['addr','addr']
cc = []
bcc =[]
msg = "From: %s\r\n" %fromaddr \
	+ "To: %s\r\n"%','.join(to) \
	+ "cc: %s\r\n"%','.join(cc) \
	+ "Bcc: %s\r\n"%','.join(bcc) \
	+ "Subject: Test\r\n" \
	+ "\r\n" \
	+ "This is the third Test" 
toaddrs = [toaddr] + to + cc + bcc
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login("user","password")
server.sendmail(fromaddr,toaddrs,msg)
server.quit()