from cloudcv import CloudCV
import signal
import argparse
import os

#------------------------------Initial Setup :- Argument Parser--------------------------
parser = argparse.ArgumentParser()
parser.add_argument("config", type=str, help="Full Path to config file")
parser.add_argument("-I", "--input", type=str, help="Full Path to the Input Folder")
parser.add_argument("-O", "--output", type=str, help="Full Path to the Output Folder")
parser.add_argument("-E", "--executable", type=str, help="Executable Name: \n1.) ImageStitch or \n 2.)VOCRelease5")
parser.add_argument("--nologin", help="Specify this argument to ignore logging in. However some features can be used only when logged in.",
                    action="store_true")
args = parser.parse_args()
#----------------xxx-------------Argument Parser Code Ends---------------------xxx----------------------


def parseCommandLineArgs():
    parsedDict = {}
    if args.input:
        parsedDict['input'] = args.input
    if args.output:
        parsedDict['output'] = args.output
    if args.executable:
        parsedDict['exec'] = args.executable
    return parsedDict, args.config, not args.nologin

if __name__ == "__main__":
    parsedDict, config_file, login_required = parseCommandLineArgs()
    print parsedDict

    ccv = CloudCV(login_required)
    
    if(login_required):
        ccv.dropbox_authenticate()

    ccv.execute(os.getcwd() + '/' + str(config_file), parsedDict)
    ccv.execute(os.getcwd() + '/' + str(config_file), parsedDict)

    #TODO
    #p.visualize() or p.job_history()