import pandas as pd
import re
def encode_label_composed (labels, weight):#higher weight imply the level of contract being more important
    result = []
    for label in labels:
        label = label.lower()
        #print(label)
        encoded_row = ['0']*10
        match = re.search(r'\d', label)
        if match:
            encoded_row[0] = weight*int(match.group())
            match = re.search(r'[a-z]', label)
            if match:
                if match.group() == 'c':
                    encoded_row[4] = 1
                elif match.group() == 'd':
                    encoded_row[5] = 1
                elif match.group() == 'h':
                    encoded_row[6] = 1
                elif match.group() == 's':
                    encoded_row[7] = 1
                elif match.group() == 'n':
                    encoded_row[8] = 1
                else:
                    print("encode_label error: unknown bid")
            else:
                print("encode_label error: unknown bid")
        else:
            encoded_row[0] = int(0)
            match = re.search(r'[a-z]', label)
            if match:
                if match.group() == 'p':
                    encoded_row[1] = 1
                elif match.group() == 'd':
                    encoded_row[2] = 1
                elif match.group() == 'r':
                    encoded_row[3] = 1
                elif match.group() == 'n':
                    encoded_row[9] = 1
                else:
                    print("encode_label error: unknown bid")
            else:
                print("encode_label error: unknown bid")
        result.append(encoded_row)
        #print(encoded_row)
    #print(result)
    return result

import pandas as pd
import re
def encode_label_onehot (labels):
    result = []
    for label in labels:
        label = label.lower()
        #print(label)
        encoded_row = ['0']*39
        class_id = 0
        match = re.search(r'\d', label)
        if match:
            #print("aaa")
            lv = int(match.group())
            match = re.search(r'[a-z]', label)
            if match:
                #print("lv")
                #print(lv)
                if match.group() == 'c':
                    class_id = 5*(lv-1)+4
                elif match.group() == 'd':
                    class_id = 5*(lv-1)+5
                elif match.group() == 'h':
                    class_id = 5*(lv-1)+6
                elif match.group() == 's':
                    class_id = 5*(lv-1)+7
                elif match.group() == 'n':
                    class_id = 5*(lv-1)+8
                else:
                    print("encode_label error: unknown bid")
            else:
                print("encode_label error: unknown bid")
        else:
            encoded_row[0] = int(0)
            match = re.search(r'[a-z]', label)
            if match:
                if match.group() == 'p':
                    class_id = 1
                elif match.group() == 'd':
                    class_id = 2
                elif match.group() == 'r':
                    class_id = 3
                elif match.group() == 'n':
                    class_id = 0
                else:
                    print("encode_label error: unknown bid")
            else:
                print("encode_label error: unknown bid")
        encoded_row[class_id] = 1
        result.append(encoded_row)
        #print(encoded_row)
    #print(result)
    return result

def decode_label (labels, weight):
    result = []
    for label in labels:
        suit = ''
        level = str(round(label[0]))
        if level == '0':
            level = ''
        if label[1] == 1:
            suit = 'p'
        if label[2] == 1:
            suit = 'd'
        if label[3] == 1:
            suit = 'r'
        if label[4] == 1:
            suit = 'c'
        if label[5] == 1:
            suit = 'd'
        if label[6] == 1:
            suit = 'h'
        if label[7] == 1:
            suit = 's'
        if label[8] == 1:
            suit = 'n'
        result.append(level+suit)
    return result