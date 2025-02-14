film_Set = {"bem10","moana","moanna2","high school music","peppa"}

# Descobrindo se o valor do type retorna como SET
print(type(film_Set))

# True e 1 são considerados o mesmo valor
exampleSet = {"peppa 2",True, 1, 8.1}
print (exampleSet)

# Adicionar um item no set
film_Set.update(exampleSet)
print(film_Set)

# Remover um item dentro do set
film_Set.remove(True)
film_Set.remove(8.1)
print (film_Set)
