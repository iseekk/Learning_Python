import pickle
import shelve


# pickle

variety = ["łagodny", "pikantny", "kwaszony"]
shape = ["cały", "krojony wzdłuż", "w plasterkach"]
brand = ["Dawtona", "Klimex", "Vortumnus"]

with open('pickle1.dat', 'wb') as f:
    pickle.dump(variety, f)
    pickle.dump(shape, f)
    pickle.dump(brand, f)

with open('pickle1.dat', 'rb') as p:
    v = pickle.load(p)
    sh = pickle.load(p)
    b = pickle.load(p)
    print(v, sh, b)


# shelve

with shelve.open('pickle2.dat') as s:
    s["odmiana"] = ["łagodny", "pikantny", "kwaszony"]
    s["kształt"] = ["cały", "krojony wzdłuż", "w plasterkach"]
    s["marka"] = ["Dawtona", "Klimex", "Vortumnus"]
    s.sync()
    print('\nodmiana:', s['odmiana'])
    print('kształt:', s['kształt'])
    print('marka:', s['marka'])

