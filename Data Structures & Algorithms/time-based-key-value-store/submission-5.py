class TimeMap:

    def __init__(self):
        # initilize a data structure
        self.store={}
        
    # add a key value pair at a given timestamp into the hashmap
    def set(self, key: str, value: str, timestamp: int) -> None:
        # one key, multiple values (at diff timestamps)
        # add (value, timestamp) into the array represented by key
        if key not in self.store:
            self.store[key]=[]
   
        self.store[key].append((value,timestamp))

        
    # get a value from a given key from the hashmap timestamp_prev <= timestamp (return largest timestamp, if not return "")
    def get(self, key: str, timestamp: int) -> str:
        # retrieve keys values at a certain timestamp
        
        # if the key is not there, return ""
        potential_values = self.store.get(key)
        if not potential_values:
            return ""

        left,right=0,len(potential_values)-1
        best_value=""
        while left <= right:
            mid = (right + left)//2
            value,t=potential_values[mid]

            if t <= timestamp:
                best_value = value
                left=mid+1
            else:
                right=mid-1
        return best_value 

