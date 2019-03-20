"""
Encryption functions for Appvault client program
"""


from .communicator import Communicator, SerialWriter


def encrypt(infile, outfile, comms=None):
    """Encrypts a file and stores on the host machine.

    Parameters
    ----------
    infile: :class:`os.PathLike`
        The name of the file to be encrypted.
    outfile: :class:`os.PathLike`
        The name that the encrypted file should be saved as.
    comms: Optional[:class:`Communicator`]
        The Communicator to use when transferring and receiving data.
        Defaults to user input.

    """
    comms = Communicator() if comms is None else comms
    with open(infile, "rb") as infile_open, \
            open(outfile, "wb") as outfile_open:
        unencrypted_data = infile_open.read()
        SerialWriter(comms, b"enr").write(unencrypted_data, also_flush=True)
        id, encrypted_bytes = comms.read_id_and_bytes()
        assert id == b"enc", f"ID: {id}"
        #encrypted_bytes = comms.request_encryption_bytes(unencrypted_data)
        outfile_open.write(encrypted_bytes)
