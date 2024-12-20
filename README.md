## **2FA Code Retriever**

### **Description**
This is a simple Python tool that retrieves the current 2FA (Time-based One-Time Password, TOTP) code using the **2FA.live** API. By providing a valid secret key, the program generates and displays the current 6-digit 2FA code and exits automatically.

---

### **Features**
- Fetches the current TOTP code for a given secret key.
- Uses the 2FA.live API for computation.
- Lightweight, fast, and easy to use.

---

### **Requirements**
- **Python 3.x**
- **Requests library** (for HTTP requests)

Install the required library using:
```bash
pip install requests
```

---

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/VyyKa/Get2fa.git
   cd Get2fa.git
   ```

2. Ensure dependencies are installed:
   ```bash
   pip install requests
   ```

---

### **Usage**
Run the program using Python and provide your secret key when prompted:

```bash
python 2fa.py
```

#### Example:
```
=== Automatic get 2fa ===
Enter secret key: JBSWY3DPEHPK3PXP
[+] Current 2FA code: 123456
End.
```

---

### **How It Works**
1. The program requests the current TOTP code from the **2FA.live** API using the provided secret key.
2. The API processes the secret key and returns the 6-digit code.
3. The tool displays the code and exits.

---

### **Code Structure**
- `2fa.py` - Main script that fetches and displays the TOTP code.

---

### **Notes**
- **Keep your secret key secure**: Never share or expose your secret key publicly.
- The TOTP code is valid for approximately 30 seconds.
- Ensure an active internet connection to access the 2FA.live API.

---

### **Contributing**
Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements.

---

### **License**
This project is licensed under the MIT License. 

---

### **Author**
- Name: VyyKa
- Role: 3rd-year student at FPT University
- Skills: Python, Java, Pentest
