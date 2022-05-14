# E-mail Server: enumeration of users within an SMTP server
<br>
This is an enumeration of users within an SMTP server.
Most servers have external security for this. However, it is imperative that this internal test be carried out in a company that has an internal email server (this does not apply so much to the case where you host in large hosting companies).
This enumerator aims to find users inside the SMTP server by brute force among the users that I will define.
<br><br>

- <b>Note:</b> In `sock.connect` port 25 has been defined, but you can brute force the ports as it may be by default some other port in the SMTP service.
