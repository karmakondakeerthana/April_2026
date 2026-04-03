class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.key_to_freq={}
        self.freq_to_key=defaultdict(OrderedDict)
        self.mf=0
    
    def update(self,key):
        freq=self.key_to_freq[key]
        del self.freq_to_key[freq][key]
        if not self.freq_to_key[freq]:
            del self.freq_to_key[freq]
            if self.mf==freq:
                self.mf+=1
        new_freq=freq+1
        self.key_to_freq[key]=new_freq
        self.freq_to_key[new_freq][key]=None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return-1
        self.update(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity==0:
            return
        if key in self.cache:
            self.cache[key]=value
            self.update(key)
            return
        if len(self.cache)>=self.capacity:
            lfu,_=self.freq_to_key[self.mf].popitem(last=False)
            del self.cache[lfu]
            del self.key_to_freq[lfu]
        self.cache[key]=value
        self.key_to_freq[key]=1
        self.mf=1
        self.freq_to_key[1][key]=None
        return 
