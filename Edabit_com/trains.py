from traceback import print_tb


class Train:
    def __init__(self, destination, time):
        self.destination = destination[-1]
        self.expected_time = time
  

def manage_delays(train_object, dest, delay_mins):
        # print('wadwo',t.des)
        # print('dest from manage delay',dest)
        ##how do i store an instance of class as a variable 
        
        if dest == train_object.destination:
            print('same destination')
            train_object.expected_time += delay_mins
    

    
trains = [
  Train(["Townsville", "Suburbia", "Urbantska"], "13:04"),
  Train(["Farmsdale", "Suburbia", "Lakeside Valley"], "13:20"),
  Train(["Suburbia", "Townsville", "Lakeside Valley"], "13:22")
]

for t in trains:
    manage_delays(t, "Lakeside Valley", 60)

trains[0].expected_time ➞ "13:04"