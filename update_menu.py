from cairosvg import svg2png

asci_dict={'Ä':196,'ä':228,'Ö':214,'ö':246,'Ü':220,'ü':252,'ß':223}

# Get menu from input

# Time span
print('Please enter the menu offer time span')
timespan = input() # Code for input of timespan
#timespan = '18. - 22. November 2024'

# Menu 1
print('Please enter Menu 1:')
menu_1 =input() # Code for input of menu 1
# menu_1 ='Grilled Ribeye Steak with Mashed Potatoes, Garlic Green Beans, and Red Wine Reduction'

# Menu 2
print('Please enter Menu 2:')
menu_2 =input()  # # Code for input of menu 2
# menu_2 ='Roasted Vegetable Risotto with Seasonal Vegetables'

# Variables for lines in SVG
zeile1 =''
zeile2 =''
zeile3 =''
zeile4 =''
zeile5 =''
zeile6 =''

# Replace certain characters by asci-code in text

for i in asci_dict.keys():
    menu_1 = menu_1.replace(i,'&#' + str(asci_dict[i])+';')
    menu_2 = menu_2.replace(i,'&#' + str(asci_dict[i])+';')
    timespan = timespan.replace(i,'&#' + str(asci_dict[i])+';')
print (menu_1,menu_2)

# Insert line breaks depending on length of the menu
if len(menu_1)>30:
    break_pos=menu_1.rfind(' ',0,30)
    if len(menu_1) > 60:
        break_pos_2=menu_1.rfind(' ',0,60)
        zeile3 = ' ' + menu_1[break_pos_2:]
        zeile2 = ' ' + menu_1[break_pos:break_pos_2]
        zeile1 = '&#8226; ' + menu_1[:break_pos]
    elif len(menu_2)<=30:
        zeile3 = menu_1[break_pos:]
        zeile2 = '&#8226; ' + menu_1[:break_pos]
    else:
        zeile2 = menu_1[break_pos:]
        zeile1 = '&#8226; ' + menu_1[:break_pos]
else: 
    zeile2 = '&#8226; ' + menu_1 
if len(menu_2)>29 and len(menu_1)<60:
    break_pos=menu_2.rfind(' ',0,30)
    zeile5 = ' ' + menu_2[break_pos:]
    zeile4 = '&#8226; ' + menu_2[:break_pos]
else:
    break_pos=menu_2.rfind(' ',0,30)
    zeile6 = ' ' + menu_2[break_pos:]
    zeile5 = '&#8226; ' + menu_2[:break_pos]

#Create SVG 
open('weekly_menu2.svg', 'w').write(open('weekly_menu.svg').read().replace('Time',timespan)
                                    .replace('zeile1',zeile1)
                                    .replace('zeile2',zeile2)
                                    .replace('zeile3',zeile3)
                                    .replace('zeile4',zeile4)
                                    .replace('zeile5',zeile5)
                                    .replace('zeile6',zeile6))

#Create PNG
svg2png(bytestring=open('weekly_menu2.svg').read(),write_to='weekly_menu2.png')

print('PNG saved.')