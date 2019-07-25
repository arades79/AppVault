from client import appvault
from pathlib import Path
import os
import sys

action = sys.argv[1].lower()
if action not in ("encrypt", "run"):
    raise ValueError(f"First argument ('{action}') must be one of "
                     "('encrypt', 'run')")
filename = sys.argv[2]
if not os.path.isfile(filename):
    raise FileNotFoundError(f"Provided filename ('{filename}') does not exist")

filepath = Path(filename)

print("Grabbing communicator...")
comms = appvault.Communicator()
print("Grabbed communicator")

if action == "encrypt":
    # Keep in mind that this won't end up being used since we're encrypting
    # with docker or some special baremetal gcc thing, not on the
    # raspberry pi
    print("Encrypting file...")
    appvault.encrypt(Path(filename),
                     Path(f"{filename}.vault"),
                     comms)
    print("Encrypted file.")
else:
    assert action == "run"
    appvault.run(Path(filepath), comms)
    print("Done executing encrypted file")
