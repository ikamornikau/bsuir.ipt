def error_handler(f):
    def wrapped():
        try:
            f()
        except Exception as err:
            print(f"serializer: error while running program: {err}")

    return wrapped
