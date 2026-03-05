l = [1,2,3,4]
l.append(5)
print(l)
l2=[6,7,8]
l.extend(l2)  #l listesini l2 listesi ile birrleştirir.
print(l)
l.append(l2)  #l listesine l2yi appendlersek l2yi tek bir eleman olarak ekler.
l.insert(3,8)
print(l)
print(l.pop()) #en üstten kaldırır LIFO son giren ilk çıkar.
print(l)
print(l.index(1))  #bulmak istediğin elemanın index numarasını verir.
print(l.count(2))  #listede bulunan elemandan kaç tane olduğunu söyler.
