# Analyzing Diffie-Hellman Implementation in Real-World Devices

## 📌 Overview
This project investigates the **Diffie-Hellman (DH) key exchange protocol**, focusing on its mathematical foundations, practical vulnerabilities, and real-world implementations. Using **Wireshark**, **Python**, and cryptographic libraries, we simulated known attacks (like **Logjam**) and analyzed parameter weaknesses in various DH configurations.

We also compared classical DH with **Elliptic Curve Diffie-Hellman (ECDH)** to evaluate security trade-offs and recommended best practices for modern cryptographic implementations.

---

##  Tools & Technologies
- **Language**: Python
- **Libraries**: `sympy`, `gmpy2`, `pycryptodome`, `matplotlib`
- **Network Tool**: Wireshark
- **Security Techniques**:
  - Discrete Logarithm Solvers (Pollard’s rho, Baby-step Giant-step)
  - Parameter Validation (Primality Testing, Generator Validation)
  - Logjam Attack Simulation

---

## Methodology
### Diffie-Hellman Analysis
- Verified prime modulus `p` using the **Miller-Rabin Primality Test**
- Validated generator `g` for cryptographic soundness
- Extracted `p`, `g`, and public keys from **TLS traffic** via Wireshark

### Logjam Attack Simulation
- Downgraded the DH key exchange to 512-bit primes
- Solved the discrete logarithm to recover private keys and decrypt communication
- Demonstrated real-world risk of using small primes

### Classic DH vs ECDH
- Compared performance and security benefits of **Elliptic Curve DH**
- Demonstrated how **ECDLP** offers stronger protection with smaller keys

---

## Results
-  Successfully simulated the **Logjam attack**
-  Found that 512-bit and 1024-bit DH primes are vulnerable to discrete log attacks
-  Demonstrated how ECDH mitigates these risks with better performance and smaller key sizes


---

## My Role
I contributed to:
- Capturing and analyzing DH key exchange parameters using Wireshark
- Writing and testing Python scripts for key recovery and analysis
- Simulating Logjam attacks
- Preparing the final report and technical presentation

---

## Key Findings
- DH is only secure with **large prime numbers (≥ 2048-bit)**
- Logjam can break poorly configured DH exchanges
- Transitioning to **ECDH** is strongly recommended for modern systems
- Python can be used to implement powerful discrete log solvers for analysis

---

## License
This project is intended for academic and educational purposes. You may use the content with proper credit. Consider adding an [MIT License](https://choosealicense.com/licenses/mit/) for reuse.

---

## Contact
For any questions or collaboration inquiries, feel free to reach out via [LinkedIn](https://linkedin.com/in/chinmaychabbi) or GitHub.
