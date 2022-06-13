from utils import args, wrappers


@wrappers.error_handler
def main():
    print(args.get_app_args())


if __name__ == "__main__":
    main()
