import argparse


def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--movies",
                        action="store_true", dest="movies", default=False,
                        help="Display all movies")
    parser.add_argument("-c", "--cinemas",
                        action="store_true", dest="cinemas", default=False,
                        help="Display all cinemas")
    parser.add_argument("-p", "--payments",
                        action="store_true", dest="payments", default=False,
                        help="Display all payments")
    parser.add_argument("-t", "--tickets",
                        action="store_true", dest="tickets", default=False,
                        help="Display all tickets")

    options = parser.parse_args()
    return options


def solution(options):
    app.config.options = options
    app.run(debug=True)
    #raise NotImplementedError("To be implemented.")


if __name__ == "__main__":
    solution(set_options())