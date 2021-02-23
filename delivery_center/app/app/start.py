import pandas as pd
import numpy as np
import os
import time
import subprocess

df = pd.read_csv("app/users.csv")

nomes = np.array(df['nome'])
senhas = np.array(df['senha'])

arq = open("app/keys.csv",'w')
arq.close()
for nome,senha in zip(nomes,senhas):
##	print(nome,senha)
	os.system("python3 app/conta.py {} {}".format(nome,senha))
	cmd= ['python3', 'app/conta.py', nome, senha]
#	print(nome,senha)
	os.system("python3 app/conta.py  {} {}".format(nome,senha))
	#print(result)

	process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#	arq = open("app/keys.csv","a")
#        arq.write(key)
#        arq.close()

	while process.poll() is None:
		restul = process.stdout.readline()
		if '* Server Key: ' in str(restul):
			key = str(restul.decode()).replace('* Server Key: ','')
			print(key)
			arq.write(key)
			break
	arq.close()
	#print(process.stdout.read())
#	process.stdout.close()



time.sleep(1)
os.system("python3 run_server.py &")

