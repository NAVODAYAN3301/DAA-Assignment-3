def maximum_units(boxTypes, truckSize):
    
    boxTypes.sort(key=lambda x: x[1], reverse=True)

    total_units = 0
    for number_of_boxes, units_per_box in boxTypes:
        if truckSize == 0:
            break  

       
        boxes_to_take = min(truckSize, number_of_boxes)
        total_units += boxes_to_take * units_per_box
        truckSize -= boxes_to_take  

    return total_units

# Example usage
if __name__ == "__main__":
    
    boxTypes = [[2, 3], [4, 1],[1, 4] ,[3, 2]]  
    truckSize =  5 

    result = maximum_units(boxTypes, truckSize)
    print("Maximum units that can be carried =", result)
