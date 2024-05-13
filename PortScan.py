import socket

def check_ports(ip, ports):
    results = []
    for port_num in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                print(f'[*] Try to connect to {ip}: {port_num}')
                result = s.connect_ex((ip, port_num))
                if result == 0:  # Connection successful
                    try:
                        s.send('Python Connect\n'.encode())
                        banner = s.recv(1024)
                        if banner:
                            results.append(f'[+] {port_num} port is opened: {banner.decode("utf-8")}\n')
                    except Exception as e:
                        results.append(f'[+] {port_num} port is opened but error occurred: {str(e)}\n')
                else:  # Connection failed
                    results.append(f"[-] {port_num} port is closed.\n")
        except Exception as e:  # An error occurred during scanning
            results.append(f"[!] Error occurred while scanning {port_num} port: {str(e)}\n")
    return results

if __name__ == "__main__":
    ip = input("Enter the IP address to scan: ")
    port_numbs = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

    results = check_ports(ip, port_numbs)

    with open('port_scan_result.txt', 'w') as f:
        for result in results:
            f.write(result)

    with open('port_scan_result.txt') as f:
        data = f.read()
        print('------------- Result -------------')
        print(data)
