# File-Transfer-Protocol-using-python
Implementation of FTP
FTP (File Transfer Protocol)
What is FTP (File Transfer Protocol)?
FTP (File Transfer Protocol) is a network protocol for transmitting files between computers over Transmission Control Protocol/Internet Protocol (TCP/IP) connections. Within the TCP/IP suite, FTP is considered an application layer protocol.

In an FTP transaction, the end user's computer is typically called the local host. The second computer involved in FTP is a remote host, which is usually a server. Both computers need to be connected via a network and configured properly to transfer files via FTP. Servers must be set up to run FTP services, and the client must have FTP software installed to access these services.

Although many file transfers can be conducted using Hypertext Transfer Protocol (HTTP) -- another protocol in the TCP/IP suite -- FTP is still commonly used to transfer files behind the scenes for other applications, such as banking services. It is also sometimes used to download new applications via web browsers.
How does FTP work?
FTP is a client-server protocol that relies on two communications channels between the client and server: a command channel for controlling the conversation and a data channel for transmitting file content.

Here is how a typical FTP transfer works:

A user typically needs to log on to the FTP server, although some servers make some or all of their content available without a login, a model known as anonymous FTP.
The client initiates a conversation with the server when the user requests to download a file.
Using FTP, a client can upload, download, delete, rename, move and copy files on a server.
FTP sessions work in active or passive modes:

Active mode. After a client initiates a session via a command channel request, the server creates a data connection back to the client and begins transferring data.
Passive mode. The server uses the command channel to send the client the information it needs to open a data channel. Because passive mode has the client initiating all connections, it works well across firewalls and network address translation gateways.
Active FTP and passive FTP compared
Users can work with FTP via a simple command-line interface -- from a console or terminal window in Microsoft Windows, Apple macOS or Linux -- or with a dedicated graphical user interface. Web browsers can also serve as FTP clients.

Why is FTP important and what is it used for?
FTP is a standard network protocol that can enable expansive file transfer capabilities across IP networks. Without FTP, file and data transfer can be managed with other mechanisms -- such as email or an HTTP web service -- but those other options lack the clarity of focus, precision and control that FTP enables.

FTP is used for file transfers between one system and another, and it has several common use cases, including the following:

Backup. FTP can be used by backup services or individual users to backup data from one location to a secured backup server running FTP services.
Replication. Similar to backup, replication involves duplication of data from one system to another but takes a more comprehensive approach to provide higher availability and resilience. FTP can also be used to facilitate this.
Access and data loading. FTP is also commonly used to access shared web hosting and cloud services as a mechanism to load data onto a remote system.
FTP types
There are several different ways an FTP server and client software can conduct a file transfer using FTP:

Anonymous FTP. This is the most basic form of FTP. It provides support for data transfers without encrypting data or using a username and password. It's most commonly used for download of material that is allowed for unrestricted distribution. It works on port
Password-protected FTP. This is also a basic FTP service, but it requires the use of a username and password, though the service might not be encrypted or secure. It also works on port 21.
FTP Secure (FTPS). Sometimes referred to as FTP Secure Sockets Layer (FTP-SSL), this approach enables implicit Transport Layer Security (TLS) as soon as an FTP connection is established. FTPS was initially used to help enable a more secure form of FTP data transfer. It typically defaults to using port 990.
FTP over explicit SSL/TLS (FTPES). This approach enables explicit TLS support by upgrading an FTP connection over port 21 to an encrypted connection. This is a commonly used approach by web and file sharing services to enable secure file transfers.
Secure FTP (SFTP). This is technically not an FTP protocol, but it functions similarly. Rather, SFTP is a subset of the Secure Shell (SSH) protocol that runs over port 22. SSH is commonly used by systems administrators to remotely and securely access systems and applications, and SFTP provides a mechanism within SSH for secure file transfer.
