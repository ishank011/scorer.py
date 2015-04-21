import argparse

def scorer_parser():
    parser = argparse.ArgumentParser(description="A simple tool to send cricket notification as desktop notifications")
    
    parser.add_argument("-d", "--debug", help="Enable debugging output", action="store_true")
    parser.add_argument("-t", "--delay", help="Set the delay for notifications in seconds", type=int)
    parser.add_argument("-c", "--config-file", help="Path to config file, defaults to scorerrc", type=argparse.FileType("r"))
    parser.add_argument("-l", "--log-file", help="Path to log file, defaults to scorer.log", type=argparse.FileType("w"))

    return parser
