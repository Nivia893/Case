from scapy.all import sniff
from collections import Counter
import argparse

# Função para processar pacotes capturados
def process_packet(packet):
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        proto = packet['IP'].proto
        size = len(packet)

        traffic_data['total_packets'] += 1
        traffic_data['protocols'][proto] += 1
        traffic_data['ip_src'][ip_src] += 1
        traffic_data['ip_dst'][ip_dst] += 1

# Função para exibir estatísticas
def display_statistics():
    print(f"Total de pacotes capturados: {traffic_data['total_packets']}")
    print("Pacotes por protocolo:")
    for proto, count in traffic_data['protocols'].items():
        print(f"Protocolo {proto}: {count} pacotes")

    print("Top 5 endereços IP de origem com mais tráfego:")
    for ip, count in traffic_data['ip_src'].most_common(5):
        print(f"{ip}: {count} pacotes")

    print("Top 5 endereços IP de destino com mais tráfego:")
    for ip, count in traffic_data['ip_dst'].most_common(5):
        print(f"{ip}: {count} pacotes")

# Inicialização dos dados de tráfego
traffic_data = {
    'total_packets': 0,
    'protocols': Counter(),
    'ip_src': Counter(),
    'ip_dst': Counter()
}

# Função principal
def main(interface):
    print(f"Iniciando captura de pacotes na interface {interface}...")
    sniff(iface=interface, prn=process_packet, store=False)
    display_statistics()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analisador de Tráfego de Rede")
    parser.add_argument("interface", help="Interface de rede para captura de pacotes")
    args = parser.parse_args()
    main(args.interface)
