import socket
import re
import time

def solve_problem(problem):
    # Simple function to solve the mathematical problem
    return str(eval(problem))

def receive_data(socket):
    # Receive data from the socket until a newline character is found
    data = b""
    while True:
        chunk = socket.recv(1)
        if not chunk or chunk == b'\n':
            break
        data += chunk
    return data.decode()

def main():
    host = "0.cloud.chals.io"
    port = 33312

    try:
        # Connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        # Receive and solve problems until the challenge is completed
        while True:
            data = receive_data(client_socket)
            print(data)

            # Use regular expression to extract the problem
            match = re.search(r'Solve: (.+)', data)
            if not match:
                print("Problem extraction failed. Exiting.")
                break

            problem = match.group(1).strip()

            # Solve the problem
            answer = solve_problem(problem)

            # Send the answer to the server
            client_socket.send(answer.encode())

            # Introduce a delay after sending the answer
            time.sleep(0.1)

            # Wait for the correct response or completion message
            data = receive_data(client_socket)
            print(data)

            # Check if the challenge is completed
            if "Challenge completed" in data:
                print(receive_data(client_socket))
                break

    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Closing the connection.")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        client_socket.close()

if _name_ == "_main_":
    main()
