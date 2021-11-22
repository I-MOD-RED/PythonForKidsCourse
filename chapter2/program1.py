a = int(8);

print ('{} * 3.57 = '.format(a) + str(a * 3.57) + ' type:{}'.format(type(a * 3.57)));
print (type(10 * 365));

# Chcem aby vo vypise bolo: "Vysledok: 3650 !" s pouzitim funkcie 10 * 365

print ("Vysledok: ", end="");
print (10 * 365, end="");
print ("!");

# Co bude vysledkom nasledovnej funkcie?
print (2 - 2.0);
# Odhadovany vysledok: 0
# skutočný výsledok: 0.0 pokial vo výpočte sa nachádza jedno desatinné číslo, výsledok bude v desatinných číslach taktiež.
