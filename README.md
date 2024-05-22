# Cisco CLI Automator

This is a quick-and-dirty project to automate the Cisco VPN Connection.

# Setup
1. Prior to setup, you need to have the OTP Link. Retrieve it first in the following format:
```
otpauth://totp/....?secret=<sekret>&period=<period>&digits=<digits>&issuer=<Issuer>
```

2. You need to set up a KeePass Database if you do have one already. THis database **MUST** be secured using a KeePass Database Keyfile.
   (*See 2.2 and 2.3*)
All credentials and usernames are stored in the keepass database. This makes sure, that no sensitive data is leaked. 
Create two different entries in your database, using the KeePass URL, one for the otpauth-URL you retrieved earlier.

2.1 The OTP Url
- You can choose an arbitrary name (e.g., OTP URL). Make sure, that this name is however unique across you database to avoid falsly selected entries.
- You do not need to enter a username or password (you can omit or delete the content of these fields)
- Paste the `otpauth://...`-URL in the KeePass Field *url*.
- Save the database

2.2 The VPN username and password
- You can choose an arbitrary name (e.g., VPN Credentials). Make sure, that this name is however unique across you database to avoid falsly selected entries.
- Enter your *username* AND your *password*
- Save the database+

Now we need to configure the Automator. For this in the [VPNConfig.py](src%2Fcontroller%2FVPNConfig.py) just select the correct entries:
```python
# Add an entry with the name "Eduroam Netzzugangskennwort" and addd your VPN username and password.
self.kbx_entry_vpn_credentials: cfg.Field[str] = cfg.Field("VPN Credentials")

# Add an Entry with the given name (TU Graz OTP Link) and add the oauth url as the field url
self.kbx_entry_otp_link: cfg.Field[str] = cfg.Field("OTP Url")
```
2.3 Also make sure, that the pathes point to the correct KeePass database and key-files [VPNConfig.py](src%2Fcontroller%2FVPNConfig.py):
```python
 self.kbx_database: cfg.Field = cfg.Field(
        Path(r"Link/to/Database.kdbx"),
        friendly_name="KeePass Database File (kbx)",
        description="The KP-Database File")

self.kbx_keyfile: cfg.Field = cfg.Field(
        Path(r"Link/to/DatabaseKeys.keyx"),
        friendly_name="KeePass Key File (keyx)",
        description="The KP-Database Key file for opening")
```


3. You need to have a Cisco VPN Client installed. Make sure, that the ``vpn_cli.exe` is found in the installation directory.

# Installation
Since there are no binaries available so far, we recommend using a `venv` and pip to install the dependecies. They can be found in the `requierements.txt` file.

# Run
If you have setup everything correctly, just run the application.
