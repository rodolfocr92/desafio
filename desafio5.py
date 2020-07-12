
def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if fim - inicio > 1 :
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
        
def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    i, j = 0, 0
    for k in range(inicio, fim):
        if i >= len(left):
            lista[k] = right[j]
            j += 1
        elif j >= len(right):
            lista[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            lista[k] = left[i]
            i += 1
        else:
            lista[k] = right[j]
            j += 1          
            
def bubblesort(lista):
    k = len(lista)
    for j in range(k - 1):
        for i in range(k - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                
if __name__ == "__main__":
    Mi=[9,8,7,6,5,4,3,2,1]
    Mr=[2,2,2,4,4,4,5,5,5,5,8,8,8,8,7,77,3,3,3,3,7,5,5,4,4,1,2,2,5,5,8,8,4,4,4,7,9,9,9,6,6,15,48,47,6,52,652,69]
    print(mergesort(Mi))
    print(bubblesort(Mr))
    

    
            
    
    
        