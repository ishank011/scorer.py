import argparse

def scorer_parser():
    parser = argparse.ArgumentParser(description="A simple tool to send cricket notification as desktop notifications")
    
    parser.add_argument("-d", "--debug", help="Enable debugging output", action="store_true")
    parser.add_argument("-t", "--delay", help="Set the delay for notifications in seconds, defaults to 60 seconds", type=int, default=60)
    # parser.add_argument("-c", "--config-file", help="Path to config file, defaults to scorerrc", type=argparse.FileType("r"))
    parser.add_argument("-l", "--log-file", help="Path to log file, defaults to scorer.log", default="scorer.log")
    parser.add_argument("--log-level", help="Set the level of logging", choices=['none', 'info', 'debug', 'warn', 'error'], default='info')
    parser.add_argument("-v", "--version", action="version", version='%(prog)s 2.0')

    return parser
