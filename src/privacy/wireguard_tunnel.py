import os

class WireGuardTunnelConfigurator:
    def __init__(self, interface_name="wg0", server_ip="10.0.0.1/24"):
        self.interface_name = interface_name
        self.server_ip = server_ip

    def generate_peer_config(self, client_private_key: str, server_public_key: str, endpoint: str) -> str:
        config = f"""[Interface]
PrivateKey = {client_private_key}
Address = 10.0.0.2/32
DNS = 1.1.1.1

[Peer]
PublicKey = {server_public_key}
Endpoint = {endpoint}:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
"""
        return config
