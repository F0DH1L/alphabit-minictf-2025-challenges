# Solution: Extracting Data from ICMP Packets

In this challenge, we need to retrieve data exfiltrated through ICMP packets. Using `tshark`, a command-line version of Wireshark, we can filter and extract the embedded data.

---

## Command Used

```bash
tshark -r file.pcappng -Y "icmp.type == 8" -T fields -e data > output.txt
```
then with some modifications on the output deleting the packet number and w got a base64 decoding it w found the flag : 

```bash
cat output.txt | hex -d | base64 -d
```
Alphabit{icmp_d4Ta_3xf1Ltr4t10n}