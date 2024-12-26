python3 ./mozilla2hashcat.py key4.db > hash.txt
hascat -m 26100 hash.txt ~/Downloads/rockyou.txt
#this will take time