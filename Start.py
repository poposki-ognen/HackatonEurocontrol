# message="140084ff ed 47 84 32 4e 41 00 6d eb f1 00 8c 1c 21 002b a1 7a 02 fa c6 05 ff cc 04 75 18 2c 77 fd 0301 9d 05 f0 4b cd d0 80 4d 84 f3 1c b8 20 00 0010 00 00 00 00 00 00 00 00 00 18 82 20 00 3d 0808 05 10 01 00 80 f6 00 00 10 fa 81 03 00 00 0000 17 ca 3c 01 30 a8 00 00 40 ff fd 31 35 20 04e2 50 e8 e9 eb 30 bf ef ff 60 00 f6 15 80 d0 0005 00 2c 00 0c 00 46 00 d4 00 6c 00 58 00 2f 003a"
# message=message.replace(" ","");
# message=bin(message)
# print message
scale = 16
# binarno = bin(int(message, scale))[2:].zfill(len(message)*4)
# message = binarno
# print "posle"
# print binarno
from conf.c20 import *

global temporary
temporary=""
length = 0

def get_fspec(message):

    global current_len
    global current_cat
    global current_seek
    global current_fspec
    i =0
    current_message = ""
    cut_places = 1
    while message[i + 7] != "0":
        current_message += message[i: i + 7]
        i += 8
        cut_places +=1
    current_message += message[i: i + 7]
    return current_message, cut_places

def get_variable_length(message):
    i =0
    current_message = ""

    while message[i + 7] != "0":
        current_message += message[i: i + 7]
        i += 8
    current_message += message[i: i + 7]
    return current_message


FUNC=[i010,i020,i140,i041,i042,i161,i170,i070,i202,i090,i100,i220,i245,i110,i105,i210,i300,i310,i500,i400,i250,i230,i260,i030,i055,i050]



def decode(message,data_output,data_input):

    FSPEC = get_fspec(message);




