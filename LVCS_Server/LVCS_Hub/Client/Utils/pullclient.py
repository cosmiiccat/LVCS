import socket
import zipfile
import os
import json

class PbClient:
    def __init__(self):
        pass

    # Function to receive file data from client
    def receive_folder(self, conn, folder_name):
        try:
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
    def send_folder(self, sock, folder_path):
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

    def client(self, request_type, folder_path, repo_name):
        # Server configuration
        host = '192.168.29.4'
        port = 12345
        

        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Connect to server
            client_socket.connect((host, port))
            print("Connected to server.")


            if request_type=="pull":
                folder_name = folder_path + ".commits"   #The received folder will be saved with this name
                data = {'type': request_type,'repo':repo_name}
                json_data = json.dumps(data)
                client_socket.send(json_data.encode("utf-8"))
                
                # Receive folder to server
                self.receive_folder(client_socket, folder_name)

                # Unzip the received folder
                os.system(f'unzip {folder_name}.zip -d {folder_name}')
                os.system(f'rm {folder_name}.zip')
                print("Folder unzipped successfully.")

            elif request_type=="push":
                source_folder_path = folder_path
                folder_path = source_folder_path + '.lvcs'  
                data = {'type': request_type,'repo':repo_name}
                json_data = json.dumps(data)
                client_socket.send(json_data.encode("utf-8"))

                # Send folder to the server
                self.send_folder(client_socket, folder_path)
        except Exception as e:
            print("Error:", e)

        finally:
            # Close the socket
            client_socket.close()

    # if __name__ == "__main__":
        # client("pull","/home/abhik/Desktop/cnproject/saved/")
