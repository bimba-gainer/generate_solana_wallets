from nacl.signing import SigningKey
import base58
from rich.console import Console
from rich.table import Table

def generate_wallets(num_wallets):
    addresses = []
    private_keys = []

    for i in range(num_wallets):
        signing_key = SigningKey.generate()
        private_key = signing_key.encode()
        public_key = signing_key.verify_key.encode()
        address = base58.b58encode(public_key).decode('utf-8')
        private_key_encoded = base58.b58encode(private_key + public_key).decode('utf-8')  # Объединение приватного и публичного ключа

        addresses.append(address)
        private_keys.append(private_key_encoded)

    with open('addresses.txt', 'w') as af, open('privatekeys.txt', 'w') as pkf:
        for address, private_key in zip(addresses, private_keys):
            af.write(f"{address}\n")
            pkf.write(f"{private_key}\n")

    wallets = list(zip(addresses, private_keys))
    display_wallets(wallets)

def display_wallets(wallets):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("No.", style="dim")
    table.add_column("Address", style="cyan")
    table.add_column("Private Key", style="green")

    for i, (address, private_key) in enumerate(wallets, start=1):
        table.add_row(str(i), address, private_key)

    console.print(table)

if __name__ == "__main__":
    print("How many wallets do you want to generate?")
    num_wallets = int(input("Enter the number: "))
    generate_wallets(num_wallets)
