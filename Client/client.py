
# Importing modules 
# Both the modules are inbulit with python so no need of installing them

# Socket module is used for low level networking interface 
import socket

#  Here i used json to structure the data
#  the program can be made without json module to reduce the complexity of the program  i have used jsosn
import json


# Connectivity to the server

class Connect_Init:
    #  Gets "ip"  as an argument as the ip could change 
    def __init__(self, ip):
        # initiate needed things
        self.sock = None

        # the ip of the HOST 
        self.host_ip = ip
        # The port its hosted on
        self.port = 7080

        # initiate connection to the server
        self.connect()

    def connect(self):
        """
        FOR MORE DETAILS 
        https://docs.python.org/3/library/socket.html
        """
        print("connecting to server...")
        #  uses AF_INET protocol  and SOCK_STREAM 

        #  for more details visit the link above
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connecting to server 
        self.sock.connect((self.host_ip, self.port))
        print("connected to server")

        #  Thats all it does when calling Connect_Init
        #  Rest of the function are called seprately

    def recv_msg(self):
        """
        Recives data and returns them 
        """

        # Here i have user 1024 bytes as its just a messaging application 
        # You can increase the size of packets by altering them 
        data = self.sock.recv(1024)
        # if data exits return data
        if data:
            return data

    def send_msg(self, msg):
        """
        Gets the message via an argument 
        and encodes them bytes 
        sends to the server aftewards  
        """
        json_file = json.dumps(msg).encode()
        self.sock.send(json_file)

    def Frame_POST(self, USER_ID, USERNAME, MESSAGE):
        """
        Formating data to send them

        NOTE as of now USER_ID is not used will be implimented aftewards
        """
        data = {'PROTOCOL': "POST",
                'USER_ID': int(USER_ID),
                'USERNAME': USERNAME,
                "MESSAGE": MESSAGE}
        print(data)
        self.send_msg(data)

    def Frame_GET(self,  USER_ID, USERNAME, L_RECORD=0):
        """
        Formating data to recive them
        """
        data = {'PROTOCOL': "POST",
                'USER_ID': int(USER_ID),
                'USERNAME': USERNAME,
                "L_RECORD": L_RECORD}
        self.send_msg(data)
    

