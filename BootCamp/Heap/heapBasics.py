class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        left = self.leftChild(i)
        right = self.rightChild(i)
        
        smallest = i
        
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right< n and arr[right] < arr[smallest]:
            smallest = right
        
        if smallest == i:
            return
        
        arr[i], arr[smallest] = arr[smallest],arr[i]
        self.heapify(smallest)
        
       
        # code here
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n-1,-1,-1):
            self.heapify(i)
        # code here
    
    # #Function to sort an array using Heap Sort.    
    # def HeapSort(self, arr, n):
    #     #code here
        
        
        
    #Helper functions
    def leftChild(self,i):
        return (2 * i) +1
    def rightChild(self,i):
        return (2 * i) + 2
    def parent(self,i):
        return (i - 1)//2
    
    
    #functions
    
    def insert(self,element,n):
        arr.append(element)
        self.upheap(n-1)
        
        
    def remove(self,i,n):
        if (i == n -1):
            arr.pop()
        else:
            arr[i],arr[-1] = arr[-1],arr[i]
            arr.pop()
        
        
    def getMin(self,arr):
        mini = arr[0]
        # for i in range(1,len(arr)):
        #     if arr[i] < mini:
        #         mini = arr[i]
        return mini
        
    def upheap(self,i,arr):
        p = self.parent(i)
        if (arr[i] < p):
            p,arr[i] = arr[i],p
            self.upheap(p)
            
    
