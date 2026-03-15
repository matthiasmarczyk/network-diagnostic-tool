import socket
import subprocess
import platform


def show_hostname():
    hostname = socket.gethostname()
    print(f"\nHostname: {hostname}")


def show_local_ip():
    try:
        ip = socket.gethostbyname(socket.gethostname())
        print(f"Local IP Address: {ip}")
    except Exception as error:
        print("Could not retrieve IP address.")
        print(error)


def check_internet():
    host = "8.8.8.8"

    if platform.system().lower() == "windows":
        command = ["ping", "-n", "1", host]
        encoding = "cp850"
    else:
        command = ["ping", "-c", "1", host]
        encoding = "utf-8"

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding=encoding,
            errors="ignore"
        )

        if result.returncode == 0:
            print("\nInternet connection is working.")
        else:
            print("\nNo internet connection detected.")
    except Exception as error:
        print("Internet test failed.")
        print(error)


def dns_test():
    try:
        ip = socket.gethostbyname("google.com")
        print(f"\nDNS test successful. google.com resolved to {ip}")
    except Exception as error:
        print("\nDNS test failed.")
        print(error)


def main():

    while True:

        print("\nNetwork Diagnostic Tool")
        print("1 - Show hostname")
        print("2 - Show local IP")
        print("3 - Test internet connection")
        print("4 - DNS test")
        print("5 - Exit")

        choice = input("Enter a number: ").strip()

        if choice == "1":
            show_hostname()

        elif choice == "2":
            show_local_ip()

        elif choice == "3":
            check_internet()

        elif choice == "4":
            dns_test()

        elif choice == "5":
            print("\nExiting program.")
            break

        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()