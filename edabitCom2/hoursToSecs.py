'''Writing a function that converts hours to seconds'''
def how_many_seconds(hour):
    # A simple hour to seconds converter
    # User will provide the hours to be converted to seconds at func call
    minutes = hour * 60 
    seconds =  minutes * 60

    return seconds

how_many_seconds(2)



