import sys
from ItsAGramLive import ItsAGramLive

#live = ItsAGramLive()

# or if you want to pre-define the username and password without args
live = ItsAGramLive(username=sys.argv[1],password=sys.argv[2])
live.start()
#live.login()
#if login:
#	live.create_broadcast()
#	live.start_broadcast()
#	key = live.stream_key
#	if key:
#		arq = open("app/keys.csv","a")
#		arq.write(key+"\n")
#		arq.close()
