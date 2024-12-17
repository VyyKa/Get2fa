import requests

def get_2fa_code(secret_key):

    url = f"https://2fa.live/tok/{secret_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check HTTP Error
        
        # Extract OTP code from JSON response
        data = response.json()
        otp = data.get("token")
        
        if otp:
            print(f"[+] Current 2FA code: {otp}")
            return otp
        else:
            print("[-] Can not get 2FA.")
    except requests.exceptions.RequestException as e:
        print(f"[-] Not connected: {e}")

if __name__ == "__main__":
    print("=== Automatic get 2fa ===")
    secret_key = input("Enter secret key: ").strip()
    get_2fa_code(secret_key)
    print("End.")
