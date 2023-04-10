
English_Alphabets = 'abcdefghijklmnopgrstuvwxyz'

print(English_Alphabets[0])
print(English_Alphabets[-1])#z mit - wird von hinten mit -1 angefangen
print(English_Alphabets[-2])#y
print(English_Alphabets[0:26])#abcdefghijklmnopgrstuvwxyz
print(English_Alphabets[0:26:2])#acegikmogsuwy das dritte Feld(2) wirkt, dass eines ja eines nein vom Anfang
# bis zum Ende ausgegeben wird
print(English_Alphabets[0:26:3])#adgjmpsvy hier wird das erste vom 3-Tupel ausgeben(vom rechts zu links)
print(English_Alphabets[::-1])#zyxwvutsrgponmlkjihgfedcba
print(English_Alphabets[::-3])#zwtgnkheb hier wird das erste vom 3-Tupel ausgeben(vom links  zu rechts )
print(English_Alphabets[-1:-11:-3])#zwtg

