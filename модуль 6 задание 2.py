def shift_up(c, heap_):
    while heap_[c] > heap_[(c-1)//2] and (c-1)//2 >= 0:
        heap_[c], heap_[(c-1)//2] = heap_[(c-1)//2], heap_[c]
        c = (c-1)//2
    return c+1

def shift_down(c, heap_):
    while 2*c+1 < len(heap_):
        left = 2*c+1
        right = 2*c+2
        child = left
        if  right < len(heap_) and heap_[left] < heap_[right]:
            child = right
        if heap_[child] <= heap_[c]:
            break
        heap_[c], heap_[child] = heap_[child], heap_[c]
        c = child
    return c+1

def add(item, heap_):  #добавление элемента
    heap_.append(item)
    return shift_up(len(heap_)-1, heap_)

def extract(heap_):   #извлечение элемента
    if len(heap)==1:
        x = heap_.pop()
        return [0, x]
    else:
        heap_[0], heap_[len(heap_)-1] = heap_[len(heap_)-1], heap_[0]
        x = heap_.pop()
        y = shift_down(0, heap_)
        return [y, x]

def extract_2_o(item, heap_):  
    v = heap[len(heap)-1]
    heap_[item], heap_[len(heap_)-1] = heap_[len(heap_)-1], heap_[item]  #меняем местами
    index_ = heap.pop()
    if v > index_:
        shift_up(item, heap_)
    else:
        shift_down(item, heap_)
    return index_


n = list(map(int,input().split()))
final_heap = []
heap = []
for i in range(n[1]):
    op = list(map(int, input().split()))
    if op[0] == 1:
        if heap:
            final_heap.append(extract(heap))
        else:
            final_heap.append(-1)
    elif op[0] == 2:
        if len(heap) < n[0]:
            final_heap.append(add(op[1], heap))
        else:
            final_heap.append(-1)
    else:
        if len(heap) >= op[1] and op[1] > 0:
            final_heap.append(extract_2_o(op[1]-1, heap))
        else:
            final_heap.append(-1)

for i in final_heap:
    if type(i) == list:
        print(*i)
    else:
        print(i)
print(*heap)