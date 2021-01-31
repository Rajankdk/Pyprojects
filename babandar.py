from datetime import datetime
import random
from main import kita


#pan number setting
class process:
    def isomaking(self,ip,port,pan,terminal,Mti,acquirer,currency,source,destination,pcode):
        a = pan
        al = (len(a))
        if al > 19:
            raise ('pan out of range')


        else:
            al = str(al)
            pan = al + a

        # mti setting
        # mti = (input("enter Mti:"))
        mti = Mti

        if mti not in ('0200','0500'):
            print('mti not valid')

        # acquirer id setting
        ai = acquirer
        # ai = str(input('acquirer id:'))
        ail = len(ai)
        if ail > 11:
            print('id out of range')
        elif ail <= 9:
            ai = '0' + str(ail) + ai
        else:
            ai = str(ail) + ai

        # currency code setting
        # cc49 = input('Enter Currency Code:')
        cc49 = currency
        cc49l = len(cc49)
        if (cc49l) > 3:
            print('ccode out of range')

        # SOURCE AC SETTING
        # sac = input('enter source account number:')
        sac = source
        sacl = len(sac)
        if sacl > 99:
            print('account out of range')
        elif sacl <= 9:
            print('acount range insufficient')
        else:
            sac = str(sacl) + sac

        # DESTINATION AC SETTINGS
        # dac = input('enter destination account number:')
        if pcode =='350000':
            dac = '0'
        else:
            dac = destination

        if pcode =='350000':
            dacl = '0'
        else:
            dacl = len(dac)



        #if dacl > 99:
            #rint('account out of range')
        #elif dacl <= 9:
            #print('acount range insufficient')
        #else:
        dac = str(dacl) + dac

        # TERMINAL ID SETTINGS
        # tid = input("Enter Terminalid:")
        tid = terminal
        tidl = len(tid)
        if tidl > 8:
            print('terminal id out of range')



        # HARDCODED PARAMETERS
        bite = '0'
        Bitmap = 'F23E448128E490000000000006000030'
        # die = bite + Bitmap + mti + al + a
        # print(die)
        pcode = pcode #'400000'
        if pcode=='350000':
            amt = '000000000000'  # '000000001200'
        else:
            amt ='000000001200'


        # amt=input("Enter amount in paisa:")
        # if len(amt)>12:
        # print('amount out of range')
        # else:
        # die = bite + Bitmap + mti + al + a + pcode+amt
        # print(die)
        now = datetime.now()
        format = "%m%d%H%M%S"
        time1 = now.strftime(format)
        # die = bite + Bitmap + mti + al + a+ pcode+amt+time1
        # print(die)
        tracenum = str(random.randint(123456, 245689))
        # die = bite + mti + Bitmap + al + a + pcode + amt + time1 + tracenum
        # print(die)
        now = datetime.now()
        format = "%H%M%S"
        localtran = now.strftime(format)
        # die = bite + mti + Bitmap + al + a + pcode + amt + time1 + tracenum + localtran
        now = datetime.now()
        format = "%m%d"
        localtran2 = now.strftime(format)
        # die = bite + mti + Bitmap + al + a + pcode + amt + time1 + tracenum + localtran + localtran2
        now = datetime.now()
        format = "%Y%m"
        localtran3 = now.strftime(format)
        localtran3 = localtran3[2:]
        # die = bite + mti + Bitmap + al + a + pcode + amt + time1 + tracenum + localtran + localtran2 + localtran3
        now = datetime.now()
        format = "%m%d"
        localtran4 = now.strftime(format)
        # die = bite + mti + Bitmap + pan + pcode + amt + time1 + tracenum + localtran + localtran2 + localtran3 + localtran4
        mertype = '6011'
        pos = '901'
        pos2 = '00'

        # die = bite + mti + Bitmap + pan + pcode + amt + time1 + tracenum + localtran + localtran2 + localtran3 + localtran4 + mertype +pos + pos2 +ai
        t35 = '00'
        rrnum = str(random.randint(123456789126, 945632156789))
        # else:
        # die = bite + mti + Bitmap + pan + pcode + amt + time1 + tracenum + localtran + localtran2 + localtran3 + localtran4 + mertype +pos + pos2 + ai + t35 +rrnum + tid
        # print(die)
        ca42 = '               '
        ca43 = '                                        '
        ca46 = '000'
        pin = '                '
        f123 = '000'
        f124 = '000'

        die = mti + Bitmap + pan + pcode + amt + time1 + tracenum + localtran + localtran2 + localtran3 + localtran4 + mertype + pos + pos2 + ai + t35 + rrnum + tid + ca42 + ca43 + ca46 + cc49 + pin + sac + dac + f123 + f124
        bite = str(len(die))
        die = '0'+ bite + die
        kitavanda=kita()
        kitavanda.dogra(ip,port,die)
























