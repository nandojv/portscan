import nmap

primo_port_scanne = nmap.PortScanner()
prima_scansione = primo_port_scanne.scan("146.59.227.185", "22,80,8080,53", "-v")

#iterazione
for host in primo_port_scanne.all_hosts():
    print("host scansionato: ", (host))
    print("il suo stato e:", primo_port_scanne[host].state())
#entare nel merito del protocollo

for protocollo in primo_port_scanne[host].all_protocols():
    print("il protocollo e : ", protocollo )
    port =primo_port_scanne[host][protocollo].keys()
#ottenere porta
for porte in port :
    print("porta numero : ", (porte, "stato: ", primo_port_scanne[host][protocollo][porte]["state"]))

