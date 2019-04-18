import pysftp

with pysftp.Connection(host="mars.edu.cdv.pl", username="mbazych", password="XB7tEp2+", port=1022) as sftp:
    print("Polaczenie udalo sie!")
