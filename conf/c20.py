import json

# out_json = open('output.json', 'r+').read()
# out_json_data=json.loads(out_json)
scale = 16


def get_variable_length(message):
    i = 8
    current_message = ""
    current_message += message[0: i - 1]
    while message[i + 7] != 0:
        current_message += message[i: i + 7]
        if i >= len(message):
            break

    return current_message

def twos_comp(val, bits):
    """compute the 2's compliment of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val


def i030(message,out_json_data):
    out_json_data["category"]["dataItems"][3]["WE"]=int(message[0:7], 2)
    return out_json_data

def i055(datafield,out_json_data):
    out_json_data["category"]["dataItems"][6]["fields"]["V"]=datafield[0]
    out_json_data["category"]["dataItems"][6]["fields"]["G"]=datafield[1]
    out_json_data["category"]["dataItems"][6]["fields"]["L"]=datafield[2]
    out_json_data["category"]["dataItems"][6]["fields"]["Mode-1 code in octal representation"]=oct(int(datafield[3:],2))
    # print out_json_data["category"]["dataItems"][6]["fields"]
    return out_json_data
def i105(datafield,out_json_data):
    out_json_data["category"]["dataItems"][11]["fields"]["Geometric Height"]=6.25*(int(datafield,2))

def i170(datafield,out_json_data):
    out_json_data["category"]["dataItems"][15]["fields"]["CNF"]=datafield[0]
    out_json_data["category"]["dataItems"][15]["fields"]["TRE"]=datafield[1]
    out_json_data["category"]["dataItems"][15]["fields"]["CST"]=datafield[2]
    out_json_data["category"]["dataItems"][15]["fields"]["CDM"]=datafield[3:5]
    out_json_data["category"]["dataItems"][15]["fields"]["MAH"]=datafield[5]
    out_json_data["category"]["dataItems"][15]["fields"]["STH"]=datafield[6]
    out_json_data["category"]["dataItems"][15]["fields"]["GHO"]=datafield[7]
    # print out_json_data["category"]["dataItems"][15]["fields"]
    return out_json_data

def i230(datafield,out_json_data):
    out_json_data["category"]["dataItems"][19]["fields"]["COM"]=int(datafield[0:3],2)
    out_json_data["category"]["dataItems"][19]["fields"]["STAT"]=int(datafield[3:6],2)
    out_json_data["category"]["dataItems"][19]["fields"]["MSSC"]=datafield[8]
    out_json_data["category"]["dataItems"][19]["fields"]["ARC"]=datafield[9]
    out_json_data["category"]["dataItems"][19]["fields"]["AIC"]=datafield[10]
    out_json_data["category"]["dataItems"][19]["fields"]["B1A"]=datafield[10:]
    # print  out_json_data["category"]["dataItems"][19]["fields"]
    return out_json_data

def i310(datafield,out_json_data):
    out_json_data["category"]["dataItems"][24]["fields"]["TRG"]=datafield[0]
    out_json_data["category"]["dataItems"][24]["fields"]["MSG"]=int(datafield[1:],2)
    # print out_json_data["category"]["dataItems"][24]["fields"]
    return out_json_data

def i400(datafield,out_json_data):
    out_json_data["category"]["dataItems"][25]["fields"]["REP"]=int(datafield[0:8],2)
    tuxrux=datafield[0:8]
    if tuxrux=="00000000":
        out_json_data["category"]["dataItems"][25]["fields"]["TUx/Rux"]=0
    else:
        if tuxrux=="11111111":
            out_json_data["category"]["dataItems"][25]["fields"]["TUx/Rux"]=1
    return out_json_data

def i010(message,out_json_data):
    mes1=message[0:8]
    mes2=message[8:]
    out_json_data['category']['dataItems'][0]['fields']['SAC'] = str(int(mes1, 2))
    out_json_data['category']['dataItems'][0]['fields']['SIC'] = str(int(mes2, 2))
    # print out_json_data['category']['dataItems'][0]['fields']
    return out_json_data
def i020(message,out_json_data):
    if len(message)==7:
        out_json_data['category']['dataItems'][1]['fields']['SSR'] = message[0]
        out_json_data['category']['dataItems'][1]['fields']['MS'] = message[1]
        out_json_data['category']['dataItems'][1]['fields']['HF'] = message[2]
        out_json_data['category']['dataItems'][1]['fields']['VDL4'] = message[3]
        out_json_data['category']['dataItems'][1]['fields']['UAT'] = message[4]
        out_json_data['category']['dataItems'][1]['fields']['DME'] = message[5]
        out_json_data['category']['dataItems'][1]['fields']['OT'] = message[6]
    else:
        if len(message)==14:
            out_json_data['category']['dataItems'][1]['fields']['SSR'] = message[0]
            out_json_data['category']['dataItems'][1]['fields']['MS'] = message[1]
            out_json_data['category']['dataItems'][1]['fields']['HF'] = message[2]
            out_json_data['category']['dataItems'][1]['fields']['VDL4'] = message[3]
            out_json_data['category']['dataItems'][1]['fields']['UAT'] = message[4]
            out_json_data['category']['dataItems'][1]['fields']['DME'] = message[5]
            out_json_data['category']['dataItems'][1]['fields']['OT'] = message[6]
            out_json_data['category']['dataItems'][1]['fields']['RAB'] = message[7]
            out_json_data['category']['dataItems'][1]['fields']['SPI'] = message[8]
            out_json_data['category']['dataItems'][1]['fields']['CHN'] = message[9]
            out_json_data['category']['dataItems'][1]['fields']['GBS'] = message[10]
            out_json_data['category']['dataItems'][1]['fields']['CRT'] = message[11]
            out_json_data['category']['dataItems'][1]['fields']['SIM'] = message[12]
            out_json_data['category']['dataItems'][1]['fields']['TST'] = message[13]
    print out_json_data['category']['dataItems'][1]['fields']

    # field_items = ['SSR', 'MS', 'HF', 'VDL4', 'UAT', 'DME', 'OT', '']
    # field_output = ['I020/020[Non-Mode S 1090MHz multilateration',
    #                          'Mode-S 1090Mhz multilateration',
    #                          'HF multilateration',
    #                          'VDL Mode 4 multilateration ',
    #                          'UAT multilateration',
    #                          'DME/TACAN multilateration ',
    #                          'Other Technology Multilateration ',
    #                          'Report from field monitor (fixedtransponder) ',
    #                         'Special Position Identification',
    #                         'Chain 2',
    #                         'Transponder Ground bit set ',
    #                         'Corrupted replies in multilateration',
    #                         'Simulated target report',
    #                         'Test Target']
    # field_output_negative = ['I020/020[no Non-Mode S 1090MHz multilateration',
    #                          'no Mode-S 1090Mhz multilateration',
    #                          'no HF multilateration ',
    #                          'no VDL Mode 4 multilateration ',
    #                          'no UAT multilateration',
    #                          'no DME/TACAN multilateration',
    #                          'No Other Technology Multilateration',
    #                          'Report from target transponder ',
    #                          'Absence of SPI',
    #                          'Chain',
    #                          'Transponder Ground bit not set',
    #                          'No Corrupted reply in multilateration',
    #                          'Actual target report',
    #                          'Default '
    #                          ]
    # field_output.reverse()
    # field_output_negative.reverse()
    # for i in range(len(message)):
    #     if(message[i] == 1):
    #         out_json_data['category']['dataItems'][1]['fields'][field_items[i]] = 1
    #         field_output_negative.pop()
    #     else:
    #         out_json_data['category']['dataItems'][1]['fields'][field_items[i]] = 0
    #         field_output.pop()
    # print out_json_data['category']['dataItems'][1]['fields']
    return out_json_data

def i041(message,out_json_data):
    global scale
    latitude= message[0:32]
    print latitude
    longitude= message[32:]
    print longitude
    latitude = twos_comp(int(latitude, 2), len(latitude))
    longitude =  twos_comp(int(longitude,2), len(longitude))
    print latitude
    print longitude
    out_json_data['category']['dataItems'][4]['fields']['latitude'] = str((float(latitude)*180)/(2**(25))) + "deg"
    out_json_data['category']['dataItems'][4]['fields']['longitude'] = str((float(longitude)*180)/(2**(25))) + "deg"
    # print out_json_data['category']['dataItems'][4]['fields']
    return out_json_data
#
def i042(message,out_json_data):
    global scale
    x = twos_comp(int(message[:24],2),len(message[:24]))
    y = twos_comp(int(message[24:],2),len(message[24:]))
    out_json_data['category']['dataItems'][5]['fields']['x'] = x*0.5
    out_json_data['category']['dataItems'][5]['fields']['y'] = y*0.5
    # print out_json_data['category']['dataItems'][5]
    return out_json_data
# i042("0000000000000111")

def i050(message,out_json_data):
    out_json_data['category']['dataItems'][5]['fields']['V']= message[0]
    out_json_data['category']['dataItems'][5]['fields']['G']= message[1]
    out_json_data['category']['dataItems'][5]['fields']['L'] = message[2]
    out_json_data['category']['dataItems'][5]['fields']['Mode-2 reply in octal representation']=oct(int(message[4:],2))
    # print out_json_data['category']['dataItems'][5]
    return out_json_data
def i070(message, out_data):

    if message[0] == 0:
        print "here"
        out_data['category']['dataItems'][8]['fields']['V'] = "0"
    else:
        out_data['category']['dataItems'][8]['fields']['V'] = "1"
    if message[1] == 0:
        out_data['category']['dataItems'][8]['fields']['G'] = "0"
    else:
        out_data['category']['dataItems'][8]['fields']['G'] = "1"
    if message[2] == 0:
        out_data['category']['dataItems'][8]['fields']['L'] = "0"
    else:
        out_data['category']['dataItems'][8]['fields']['L'] = "1"
    out_data['category']['dataItems'][8]['fields']['Flight Level'] =  oct(int(message[4:len(message)],2))
    return out_data
def i090(message,out_json_data):
    if (message[0] == "1"):
        out_json_data['category']['dataItems'][9]['fields']['V'] = "Code validated"
    else:
        out_json_data['category']['dataItems'][9]['fields']['V'] = "Code not validated"

    if message[1] == "1":
        out_json_data['category']['dataItems'][9]['fields']['G'] = "Default"
    else:
        out_json_data['category']['dataItems'][9]['fields']['G'] = "Garbled code"
    out_json_data['category']['dataItems'][9]['fields']['Flight Level'] = int(message[2:],2)*0.25
    return out_json_data
def i110(message,out_json_data):
    number = int(message,2)
    out_json_data['category']['dataItems'][12]['fields']['Measured Height'] = str(number)
    return out_json_data

def i140(message,out_json_data):
    number = float(int(message, 2))/128
    out_json_data['category']['dataItems'][13]['fields']['Time of Day'] = number
    # print out_json_data['category']['dataItems'][13]['fields']
    return out_json_data
def i161(message,out_json_data):
    number = int(message[4:], 2)
    out_json_data['category']['dataItems'][14]['fields']['Track number'] = str(number)
    # print out_json_data['category']['dataItems'][14]['fields']
    return out_json_data
def i202(message,out_json_data):
    numberY = int(message[:16], 2)
    numberX = int(message[16:], 2)
    out_json_data['category']['dataItems'][16]['fields']['Vx'] = str(numberX)
    out_json_data['category']['dataItems'][16]['fields']['Vy'] = str(numberY)
    return out_json_data

def i210(message,out_json_data):
    numberX = int(message[:8], 2)
    numberY = int(message[8:], 2)
    out_json_data['category']['dataItems'][17]['fields']['Vx'] = str(numberX)
    out_json_data['category']['dataItems'][17]['fields']['Vy'] = str(numberY)
    return out_json_data

def i220(message,out_json_data):
    target = int(message[17:],2)
    address = int(message[:17],2)
    out_json_data['category']['dataItems'][18]['fields']['target'] = target
    out_json_data['category']['dataItems'][18]['fields']['address'] = address
    return out_json_data

def i245(message,out_json_data):
    items = ['Callsign or registration not downlinked from transponder',
             'Registration downlinked from transponder',
             'Callsign downlinked from transponder']
    number = int(message[54:],2)
    if number <5:
        out_json_data['category']['dataItems'][20]['fields']['STI']= items[number]
    else:
        out_json_data['category']['dataItems'][20]['fields']['STI'] = 'Not defined'
    out_json_data['category']['dataItems'][20]['fields']['Char1'] = '-'
    out_json_data['category']['dataItems'][20]['fields']['Char2'] = '-'
    out_json_data['category']['dataItems'][20]['fields']['Char3'] = '-'
    out_json_data['category']['dataItems'][20]['fields']['Char4'] = '-'
    out_json_data['category']['dataItems'][20]['fields']['Char5'] = '-'
    out_json_data['category']['dataItems'][20]['fields']['Char6'] = '-'
    return out_json_data

def i250(message,out_json_data):
    out_json_data['category']['dataItems'][21]['fields']['REP'] = int(message[:8],2)
    out_json_data['category']['dataItems'][21]['fields']['MB'] = int(message[8:63],2)
    out_json_data['category']['dataItems'][21]['fields']['BDS1'] = int(message[63:68],2)
    out_json_data['category']['dataItems'][21]['fields']['BDS2'] = int(message[68:],2)
    return out_json_data

def i260(message,out_json_data):
    out_json_data['category']['dataItems'][22]['fields']['MB Data'] = int(message,2)
    return out_json_data

def i300(message, out_data):
    items = ['Unknown',
             'ATC equipment maintenance',
             'Airport maintenance ',
             'Fire ',
             'Bird scarer',
             'Snow plough ',
             'Runway sweeper ',
             'Emergency',
             'Police',
             'Bus',
             'Tug (push/tow) ',
             'Grass cutter',
             ' Fuel ',
             'Baggage',
             'Catering',
             'Aircraft maintenance',
             'Flyco (follow me)']
    out_data['category']['dataItems'][23]['fields']['VFI']=items[int(message,2)]
    return out_data

def i100(message,out_json_data):
    messageNew = "0"+message[17:29];
    V = message[0]
    G = message[1]
    QXi = message[20:]
    exit = ""
    for i in range(len(messageNew)-1):
        exit+= str( int(messageNew[i]) ^ int(messageNew[i+1]) )
    out_json_data['category']['dataItems'][23]['fields']['V'] = V
    out_json_data['category']['dataItems'][23]['fields']['G'] = G
    out_json_data['category']['dataItems'][23]['fields']['Mode-C reply in Gray notation'] = exit
    out_json_data['category']['dataItems'][23]['fields'] = QXi
    return out_json_data
def i500(message,out_json_data):
    if(len(message)==8):
        out_json_data['category']["dataItems"][26]['fields']['DOP']=message[0]
        out_json_data['category']["dataItems"][26]['fields']['SDP'] = message[1]
        out_json_data['category']["dataItems"][26]['fields']['SDH'] = message[2]
    if(message[0]=='1'):
        out_json_data['category']["dataItems"][26]['fields']['DOPx'] = 0.25*int(message[8:24],2)
        out_json_data['category']["dataItems"][26]['fields']['DOPy'] = 0.25*int(message[24:40], 2)
        out_json_data['category']["dataItems"][26]['fields']['DOPxy'] = 0.25*int(message[40:56], 2)
    if((message[1]=='1')&(message[0]=='0')):
        out_json_data['category']["dataItems"][26]['fields']['devx'] = 0.25*int(message[8:24], 2)
        out_json_data['category']["dataItems"][26]['fields']['devy'] = 0.25*int(message[24:40], 2)
        out_json_data['category']["dataItems"][26]['fields']['ro'] = 0.25*int(message[40:56], 2)
    else:
        out_json_data['category']["dataItems"][26]['fields']['devx'] = 0.25*int(message[56:72], 2)
        out_json_data['category']["dataItems"][26]['fields']['devy'] = 0.25*int(message[72:88], 2)
        out_json_data['category']["dataItems"][26]['fields']['ro'] = 0.25*int(message[88:104], 2)
    if((message[0]=='1')&(message[1]=='1')&(message[2]=='1')):
        out_json_data['category']["dataItems"][26]['fields']['devgh'] = 0.25 * int(message[104:120], 2)
    else:
        if ((message[0]=='1')&(message[1]=='0')&(message[2]=='1')):
            out_json_data['category']["dataItems"][26]['fields']['devgh'] = 0.25 * int(message[56:72], 2)
        else:
            if((message[0]=='0')&(message[1]=='0')&(message[2]=='1')):
                out_json_data['category']["dataItems"][26]['fields']['devgh'] = 0.25 * int(message[8:24], 2)
    return out_json_data