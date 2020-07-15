
def isOverlaping(tupleOne, tupleTwo):
    pass

def roomsRequired(tupleArr):
    markerArr = []
    for tupleElem in tupleArr:
        if len(markerArr) == 0: # marker array is empty
            markerArr.append([tupleElem])
        else: # marker array not empty
            inserted = False
            for markerRow in markerArr:
                for markerElem in markerRow:
                    if (tupleElem[0] in range(markerElem)) or (tupleElem[1] in range(markerElem)): # Overlap
                        print("Overlap for : ", tupleElem, " with ", markerArr)
                        continue
                    elif (markerElem[0] in range(tupleElem)) and (markerElem[1] in range(tupleElem)): # Overlap
                        print("Overlap for : ", markerArr, " with ", tupleElem)
                    else: # No overlap


                    


    return markerArr


if __name__ == "__main__":
    inputArr = [(30, 75), (0, 50), (60, 150)]
    print(roomsRequired(inputArr))
