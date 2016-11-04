
current_seek = 0
current_cat = ""
current_len = 0
current_fspec = ""
data_name = "Hackathon.ast"

def print_by_eigth(arr):
    for i in range(0,len(arr),8):
            print(arr[i:i+8])

def get_entire_message(file_name):
    file = open(file_name + '.ast','r')
    message_text = ""
    file = file.read()
    print(len(file))
    message_text = "".join("{:08b}".format(ord(c),'b') for c in file)
    return message_text


def get_separate_messages(message_text):
    messages = []




def get_configuration_for_category(message):
    category = int(message[:8],2)
    configuration_file = open("conf\\" + str(category) + ".conf")
    configuration_file = configuration_file.read()
    return configuration_file


def get_message_category():
    file = open(data_name ,"r")
    file.seek(current_seek)
    file = file.read(1)
    current_cat = "".join("{:08b}".format(ord(c),'b') for c in file)
    current_cat = int(current_cat,2)
    return current_cat

def get_message_length():
    file = open(data_name, "r")
    file.seek(current_seek+1)
    file = file.read(2)
    current_len_local = "".join("{:08b}".format(ord(c),'b') for c in file)
    current_len_local = int(current_len_local,2)
    current_len = current_len_local
    return current_len

def get_message():
    global current_len
    global current_cat
    global current_seek
    file = open(data_name, "r")
    file.seek(current_seek)
    file = file.read(current_len)
    message = "".join("{:08b}".format(ord(c), 'b') for c in file)
    current_seek += current_len
    return message


current_cat = get_message_category()
current_len = get_message_length()
message = get_message()
print current_cat , current_len , message
current_cat = get_message_category()
current_len = get_message_length()
message = get_message()
print current_cat , current_len , message

def main(file_name, number_of_cores):
    data_name = file_name
    # message = get_entire_message(file_name)
    # separate_messages = get_separate_messages(message)
    #
    # for message in separate_messages:
    #     try:
    #         config = get_configuration_for_category(message)
    #     except:
    #         print "no config found"
    #     #implement threading

    message_category = get_message_category()

    # while message_category != "":

