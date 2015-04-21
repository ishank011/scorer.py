from scorer.system import exitApp
import scorer.fetch_scores as fs
import scorer.notification as notify
import logging
from sys import version_info
from time import sleep
from scorer.ui import getUserInput
from scorer.options import scorer_parser

args = scorer_parser().parse_args()

logger = logging.getLogger("scorer.app")
if args.log_level is 'none':
    logger.setLevel(logging.disable)
if args.log_level is 'info':
    logger.setLevel(logging.INFO)
if args.log_level is 'debug':
    logger.setLevel(logging.DEBUG)
if args.log_level is 'warn':
    logger.setLevel(logging.WARN)
if args.log_level is 'error':
    logger.setLevel(logging.ERROR)

#TODO 
# Find out why the other modules are not logging

fh = logging.FileHandler(args.log_file)
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
if args.debug:
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

def main():
    NO_LIVE_MATCHES = "No Match in progress"
    SLEEP_INTERVAL = args.delay
    logger.info("SLEEP_INTERVAL: {}".format(SLEEP_INTERVAL))

    while True:
        logger.debug("Getting the xml and matches list")
        xml, matches = fs.findMatchesAvailable()
        if(matches[0]==NO_LIVE_MATCHES):
            print "No Live matches are available now:"
            exitApp()
        matches.append("Quit the scorer app")
        try:
            matchChoice= getUserInput(matches)
        except KeyboardInterrupt:
            exitApp()
        if(matchChoice == len(matches) -1 ):
            logger.debug("User chose quit")
            exitApp()
        logger.debug("User's choice: {} {}".format(matchChoice, matches[matchChoice-1]))
        logger.debug("Getting the latest score for the selected match")
        matchID = fs.getMatchID(matchChoice,xml)
        jsonurl = fs.getJsonURL(matchID)
        playingTeams = fs.getPlayingTeamNames(jsonurl)
        while True:
            try:
                title,score = fs.getLastestScore(jsonurl,playingTeams)
                logger.debug("Sending notification for: title:{} score:{}".format(title, score))
                notify.popUpMessage(title, score)
                sleep(SLEEP_INTERVAL)
            except KeyboardInterrupt:
                break

if __name__ == '__main__':
    main()
