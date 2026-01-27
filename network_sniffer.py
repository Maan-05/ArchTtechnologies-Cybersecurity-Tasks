from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):
    # We only care about IP packets for this basic analysis
    if IP in packet:
        ip_layer = packet[IP]
        
        # Determine protocol type for the display
        protocol = "Other"
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
            
        # Print a clean summary of the captured packet
        print(f"[{protocol}] Source: {ip_layer.src} --> Destination: {ip_layer.dst}")

print("Starting Basic Network Sniffer... (Press Ctrl+C to stop)")
# store=0 prevents memory leaks during long captures
sniff(prn=process_packet, store=0)