# Secure Networking & Encryption – Complete Overview

This document summarizes all topics discussed: SSH, SCP, SFTP, FTP, FTPS, and the major encryption layers used in secure networking.

---

## 1. SSH Family

### SSH (Secure Shell)
Secure remote login protocol used for server administration. Encrypts all communication using public/private key pairs.

### SCP (Secure Copy Protocol)
Secure file transfer method using SSH. Suitable for fast, one-time file transfers.

### SFTP (SSH File Transfer Protocol)
Secure file browsing and transfer over SSH. Supports directory navigation, uploads, downloads, renaming, and deletion.

---

## 2. FTP Family

### FTP (File Transfer Protocol)
Legacy file transfer protocol. No encryption; sends credentials in plain text.

### FTPS (FTP Secure)
FTP enhanced with SSL/TLS encryption. More secure than FTP but uses multiple ports, making firewall configuration complex.

---

## 3. Encryption Protocols & Models

### SSL/TLS (Secure Sockets Layer / Transport Layer Security)
TLS is the modern protocol securing web traffic (HTTPS). Uses certificates to encrypt client–server communication.

### SSH Encryption
Uses asymmetric key pairs to establish secure connections for remote access and file transfer.

### IPSec (Internet Protocol Security)
Network-layer encryption used for VPN tunnels and site-to-site connections.

### PGP/GPG (Pretty Good Privacy / GNU Privacy Guard)
Encrypts files and emails using public-key cryptography. Protects data content rather than the connection.

### AES (Advanced Encryption Standard)
Symmetric encryption algorithm used for data-at-rest protection, disk encryption, and secure storage.

### Kerberos
Authentication protocol used in enterprise networks, especially Windows domains.

### OAuth2 / OpenID Connect
Authentication and authorization frameworks for web applications. Rely on TLS for transport security.

### WireGuard
Modern VPN protocol offering fast, secure tunneling using advanced cryptography.

---

## 4. Comparison Table

| Technology     | Type            | Purpose                     | Secure? | Port(s)          | Uses SSH? | Uses TLS/SSL? |
|----------------|-----------------|-----------------------------|---------|------------------|-----------|----------------|
| **SSH**        | Protocol        | Remote login                | ✔️      | 22               | ✔️        | ❌             |
| **SCP**        | Protocol        | File copy                   | ✔️      | 22               | ✔️        | ❌             |
| **SFTP**       | Protocol        | File browsing & transfer    | ✔️      | 22               | ✔️        | ❌             |
| **FTP**        | Protocol        | File transfer               | ❌      | 21               | ❌        | ❌             |
| **FTPS**       | Protocol        | Secure file transfer        | ✔️      | 21 + data ports  | ❌        | ✔️             |
| **TLS/SSL**    | Protocol        | Secure web traffic (HTTPS)  | ✔️      | 443              | ❌        | ✔️             |
| **IPSec**      | Protocol        | VPN tunnels                 | ✔️      | 500, 4500, ESP   | ❌        | ❌             |
| **PGP/GPG**    | Encryption      | File/email encryption       | ✔️      | N/A              | ❌        | ❌             |
| **AES**        | Algorithm       | Data-at-rest encryption     | ✔️      | N/A              | ❌        | ❌             |
| **Kerberos**   | Auth protocol   | Enterprise authentication   | ✔️      | 88               | ❌        | ❌             |
| **OAuth2/OIDC**| Auth framework  | Web login                   | ✔️      | 443              | ❌        | ✔️ (via TLS)   |
| **WireGuard**  | VPN protocol    | Fast VPN tunneling          | ✔️      | 51820            | ❌        | ❌             |

---

## 5. Summary

Secure networking relies on multiple layers of encryption and protocols. SSH-based tools provide secure remote access and file transfer, while TLS secures web communication. IPSec and WireGuard protect network tunnels, and algorithms like AES ensure data remains encrypted at rest. Together, these technologies form a comprehensive security framework for modern systems.
