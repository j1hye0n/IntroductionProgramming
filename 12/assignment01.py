class LoggedList(list) :

    def __init__(self,iterable=None) :
        if iterable is None :
            iterable =[]
        super().__init__(iterable)

        self.path = 'LoggedList.txt'
    
    def log(self, method) :
        with open(self.path,'at') as f:
            f.write(f"{method}\n")

    def append(self,item) :
        super().append(item)
        self.log(f"[append] {item}")
    
    def remove(self,item) :
        super().remove(item)
        self.log(f'[remove] {item}')

    def pop(self, index=-1) :
        value = super().pop(index)
        self.log(f'[pop] index={index} value={value}')
        return value
    
    def __setitem__(self, index, value) :
        old = super().__getitem__(index)
        super().__setitem__(index,value)        # __setitem__ 은 리턴값이 없는 함수
        self.log(f'[setitem] index={index} old={old} new={value}')