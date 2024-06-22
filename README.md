### Solana Wallet Generator

This script generates Solana wallets (address and private key) and displays them in a formatted table. It also saves the generated data into files for future use.

### Requirements

Install the necessary dependencies using the following command:
```sh
pip install -r requirements.txt
```

### Files Generated

- `addresses.txt`: Contains the generated wallet addresses.
- `privatekeys.txt`: Contains the corresponding private keys.

### Usage

1. Clone the repository and navigate to the project directory.
2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the script:
   ```sh
   python main.py
   ```
4. Enter the number of wallets you want to generate when prompted.

### Script Details

The script generates Solana wallets using the `pynacl` library and formats the output using the `rich` library.

### Example Output

The generated wallets are displayed in a table with colored headers for easy readability. The format is as follows:

```
+-----+------------------------------------------+--------------------------------------------------+
| No. | Address                                  | Private Key                                      |
+-----+------------------------------------------+--------------------------------------------------+
| 1   | 3nN1QrLfpZKXjMJGZ2eq9RktdeD8             | 5HYGrsdjsdsd87asd78as7d87a7s8d7as8d7a8d          |
+-----+------------------------------------------+--------------------------------------------------+
| 2   | 2EkhJqLvkR9vJhGD4mK8WbcEsdsa3HGD5T8S     | 3JSkLdsjlkdsj4l5kjl4kjk56k45k6k45k6k4k5k         |
+-----+------------------------------------------+--------------------------------------------------+
```

### Contact

For any issues or questions, please contact the repository maintainer.

---

This README provides a concise guide on how to use the Solana Wallet Generator script.