from check_hub_in_stock import is_hub_available
from send_message import send_message


def main():
    message = is_hub_available()
    send_message(message)


if __name__ == "__main__":
    main()