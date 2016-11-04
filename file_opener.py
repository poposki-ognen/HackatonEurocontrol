
def print_by_eigth(arr):
    for i in range(0,len(arr),8):
            print(arr[i:i+8])

def get_entire_message(file_name):
    file = open(file_name + '.ast','r')
    message_text = ""
    file = file.read()
    print(len(file))
    message_text = "".join("{:08b}".format(ord(c),'b') for c in file)
    return message_text;
#comment


def get_separate_messages(message_text):
    messages = []




def get_configuration_for_category(message):
    category = int(message[:8],2)
    configuration_file = open("conf\\" + str(category) + ".conf")
    configuration_file = configuration_file.read()
    return configuration_file



file = open("conf\\20.conf")
file.seek(5)
file = file.read()
print file


def main(file_name, number_of_cores):

    message = get_entire_message(file_name)
    separate_messages = get_separate_messages(message)

    for message in separate_messages:
        config = get_configuration_for_category(message)
        #implement threading