class HeapMin : 
    def __init__(self):
        self._nos = 0
        self._heap = []
    
    def adiciona_no (self, u, indice):
        self._heap.append([u, indice])
        self._nos += 1
        f : int = self._nos
        while True :
            if f == 1 :
                break
            p : int = f // 2
            if self._heap[p - 1][0] <= self._heap[f - 1][0]:
                break
            else :
                self._heap[p - 1], self._heap[f - 1] = self._heap[f - 1], self._heap[p - 1]
                f = p


    def mostra_no(self):
        print(self._heap)

    def remove_no(self):
        x = self._heap[0]
        self._heap[0] = self._heap[self._nos - 1]
        self._heap.pop()
        self._nos -= 1 
        p = 1
        while True :
            f = 2 * p
            if f > self._nos: 
                break
            if f+1 <= self._nos:
                if self._heap[f][0] < self._heap[f-1][0]:
                    f += 1
            if self._heap[p-1][0] <= self._heap[f-1][0]:
                break
            else:
                self._heap[f-1], self._heap[p-1] = self._heap[p-1], self._heap[f-1]
                p = f
        return x
    
    def tamanho(self):
        return self._nos
