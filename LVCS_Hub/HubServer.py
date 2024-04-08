import socket
import os
import threading
import zipfile
import json
from service import LVCS

# Function to receive file data from client
def receive_folder(conn, folder_name):
    try:
        if not os.path.exists(folder_name):
            # If the folder doesn't exist, create it
            os.makedirs(folder_name)
            
        with open(folder_name + '.zip', 'wb') as file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)
        print(f"Folder '{folder_name}' received successfully.")
    except Exception as e:
        print("Error occurred during folder reception:", e)

# Function to send folder to server
def send_folder(sock, folder_path):
    try:
        # Compress the folder
        base_name = folder_path.split('/')[-1]
        zip_name =  base_name + '.zip'
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))

        sock.send(base_name.encode())

        # Send the compressed folder
        
        with open(zip_name, 'rb') as file:
            for data in file:
                sock.sendall(data)
        print("Folder sent successfully.")
        os.system(f'rm {zip_name}')
    except Exception as e:
        print("Error occurred during folder transmission:", e)


def handle_client(conn, addr):
    print(f"Connection established with {addr} , client_socket {conn}")
        
    received_data = conn.recv(1024).decode('utf-8', 'ignore')
    print(received_data)
    request = json.loads(received_data)
    print(request)
    repo_name = request["repo"]
    if request["type"]=="pull":
        source_folder_path = '/home/abhik/Desktop/LVCS_test/server/'+repo_name+"/"
        folder_path = source_folder_path + '.lvcs' 
        # Send folder to the client
        send_folder(conn, folder_path)
    elif request["type"]=="push":
        target_folder_path = '/home/abhik/Desktop/LVCS_test/server/'+repo_name+"/"
        folder_name = target_folder_path + '.commits'

        # Receive folder from client
        receive_folder(conn, folder_name)

        # Unzip the received folder
        os.system(f'unzip {folder_name}.zip -d {folder_name}')
        os.system(f'rm {folder_name}.zip')
        print("Folder unzipped successfully.",target_folder_path,"Hii")

        print(target_folder_path)
        LVCS_PULL = LVCS()
        LVCS_PULL.pull(target_folder_path)

    # Close the connection
    conn.close()

    



def main():
    # Server configuration
    # host = '0.0.0.0'
    host = '172.16.2.199'
    port = 12345
    folder_name = 'received_folder'

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print("Server is listening...")

    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
        

if __name__ == "__main__":
    main()
