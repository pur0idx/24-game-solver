def permute(elements, n=None):
    result = []
    if n is None :
        generatePermutations(elements, [], result)
    else :
        generatePermutationsWithLength(elements, [], result, n)
    return result
        

def generatePermutations(elements, currentPermutation, result):
    if len(elements) == 0:
        result.append(currentPermutation)
        return
    
    for i in range(len(elements)):
        newElements = elements[:i] + elements[i+1:]
        generatePermutations(newElements, currentPermutation + [elements[i]], result)
        
def generatePermutationsWithLength(elements, currentPermutation, result, n):
    if len(currentPermutation) == n :
        result.append(currentPermutation)
        return
    
    for i in range(len(elements)):
        newElements = elements[:i] + elements[i+1:]
        generatePermutationsWithLength(newElements, currentPermutation + [elements[i]], result, n)