# ----------------------------------------------------------------------
# C1. Saraksta kopsavilkums
# ----------------------------------------------------------------------

# Kodā izveido sarakstu ar sešiem skaitļiem. Izvadi to skaitu, summu, vidējo, lielāko un mazāko. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Sarakstu, kurā glabā skaitļus, nosauc ar vārdu vertibu_kopa.

saraksts = [3, 5, 9, 1, 3, 7]

print ("Sarakstā ir", len(saraksts), "skaitļi")
print ("Saraksta summa ir: ", sum(saraksts))
S = sum(saraksts) / len(saraksts)
print ("videja atzime", S)
print (max(saraksts),"Ir maksimala atzime")
print (min(saraksts),"Ir minimala atzime")
