import argparse
from .devops.system_info import get_system_info

def main():
    parser = argparse.ArgumentParser(description="Description: Smart DevOps Bot CLI")
    parser.add_argument("--hello", help="Say hello", action="store_true")
    parser.add_argument("--sysinfo", help="Get system info", action="store_true")
    args = parser.parse_args()

    if args.hello:
        print("Hello from Smart DevOps Bot CLI!")
    elif args.sysinfo:
        sys_info = get_system_info()
        print("System Information:")
        for key, value in sys_info.items():
            print(f"{key}: {value}")
    else:
        print("Use --hello or --help to test the CLI")

if __name__ == "__main__":
    main()
