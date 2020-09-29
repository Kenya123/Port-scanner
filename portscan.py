import pyfiglet
import sys
import socket
import optparse
from datetime import datetime

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)

def connScan(tgtHost, tgtPort):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((tgtHost, tgtPort))
        if result == 0:
            print(f'port {tgtPort} is open!')
           
            
        elif result != 0:
            print(f'port {tgtPort} is closed!')
        s.close()

    except KeyboardInterrupt:
        print("exitting program..")
        sys.exit(0)
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit(0)
    except socket.error:
        print("server is not responding")
        sys.exit(0)



def portScan(tgtHost, tgtPorts):
    tgtIp = socket.gethostbyname(tgtHost)
    for tgtPort in tgtPorts:
        print(f"scanning port {tgtPort} ..")
        connScan(tgtIp, int(tgtPort))
    

def main():
    parser = optparse.OptionParser("usage %prog -H <target host> -p <target ports>")
    parser.add_option("-H", dest="tgtHost", type="string", help="specify target host")
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports')
    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if(tgtHost == None) or (tgtPorts[0] == None):
        print("you must specify target host and port")
        sys.exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
    
