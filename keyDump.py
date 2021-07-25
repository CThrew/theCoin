from pycoin.key import Key
from pycoin.networks import registry
from pycoin.symbols.btc import network as BTC

minHex = '0000000000000000000000000000000000000000000000008000000000000000'
minInt = int(minHex, 16)

#maxHex = '000000000000000000000000000000000000000000000000ffffffffffffffff'
maxHex = '0000000000000000000000000000000000000000000000009000000000000000'
maxInt = int(maxHex, 16)

for curInt in range(minInt, maxInt):
        
    for strNet in registry.iterate_symbols():
        
        curNet = registry.network_for_netcode(strNet)
        priKey = curNet.keys.private(secret_exponent=curInt)

        print(priKey)
    
    
    
    