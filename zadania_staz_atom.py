import pandas as pd
df = pd.read_csv('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv',engine='python',sep=';')

def zad1():
    gender = input("For only women filter type: [w].\nFor only men filter type: [m].\nFor all type: [a]\nTo leave: [exit]\n")
    df_zad1=df[df.Przystąpiło_zdało=='przystąpiło']
    df2 = df_zad1[df_zad1.Terytorium!="Polska"]
    while True:
        if gender.lower() == 'a':
            df3 = df2.groupby(['Terytorium','Rok']).mean()
            print(df3)
        elif gender.lower() == 'w':
            df3 = df2[df2.Płeć=='kobiety']
            df4 = df3.groupby(['Terytorium','Rok']).mean()
            print(df4)
        elif gender.lower() == 'm':
            df3 = df2[df2.Płeć=='mężczyźni']
            df4 = df3.groupby(['Terytorium','Rok']).mean()
            print(df4)
        elif gender.lower() == 'exit':
            break
        else:
            print("U can type only: 'a','w' or 'm'!")
        gender = input("For only women filter type: [w].\nFor only men filter type: [m].\nFor all type: [a]\nTo leave: [exit]\n")

def zad2():
    df_zad2 = df[df.Terytorium!="Polska"]
    gender = input("For only women filter type: [w].\nFor only men filter type: [m].\nFor all type: [a]\nTo leave: [exit]\n")
    while True:
        if gender.lower() == 'a':

            df_p = df_zad2[df_zad2.Przystąpiło_zdało=="przystąpiło"]
            df_p1= df_p.groupby(['Terytorium','Rok']).sum()
            df_p2 = df_p1.rename(columns={'Liczba osób': 'Przystąpiło'})

            df_z = df_zad2[df_zad2.Przystąpiło_zdało=="zdało"]
            df_z1= df_z.groupby(['Terytorium','Rok']).sum()
            df_z2 = df_z1.rename(columns={'Liczba osób': 'Zdało'})

            df_pz = df_p2.join(df_z2)

            df_pz['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2)).astype(str)+" %"
            print(df_pz)
        if gender.lower() == 'w':
            df_wom = df_zad2[df_zad2.Płeć=='kobiety']
            df_p = df_wom[df_wom.Przystąpiło_zdało=="przystąpiło"]
            df_p1= df_p.groupby(['Terytorium','Rok']).sum()
            df_p2 = df_p1.rename(columns={'Liczba osób': 'Przystąpiło'})

            df_z = df_wom[df_wom.Przystąpiło_zdało=="zdało"]
            df_z1= df_z.groupby(['Terytorium','Rok']).sum()
            df_z2 = df_z1.rename(columns={'Liczba osób': 'Zdało'})

            df_pz = df_p2.join(df_z2)

            df_pz['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2)).astype(str)+" %"

            print(df_pz)
        if gender.lower() == 'm':
            df_man = df_zad2[df_zad2.Płeć=='mężczyźni']
            df_p = df_man[df_man.Przystąpiło_zdało=="przystąpiło"]
            df_p1= df_p.groupby(['Terytorium','Rok']).sum()
            df_p2 = df_p1.rename(columns={'Liczba osób': 'Przystąpiło'})

            df_z = df_man[df_man.Przystąpiło_zdało=="zdało"]
            df_z1= df_z.groupby(['Terytorium','Rok']).sum()
            df_z2 = df_z1.rename(columns={'Liczba osób': 'Zdało'})

            df_pz = df_p2.join(df_z2)

            df_pz['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2)).astype(str)+" %"

            print(df_pz)
        if gender.lower() == 'exit':
            break
        else:
            print("U can type only: 'a','w' or 'm'!")
        gender = input("For only women filter type: [w].\nFor only men filter type: [m].\nFor all type: [a]\nTo leave: [exit]\n")

def zad3():
    df_zad2 = df[df.Terytorium!="Polska"]
    gender = input("For only women filter type: [w].\nFor only men filter type: [m].\nFor all type: [a]\nTo leave: [exit]\n")
    while True:
        if gender.lower() == 'a':
            df_p = df_zad2[df_zad2.Przystąpiło_zdało=="przystąpiło"]
            df_p1= df_p.groupby(['Rok','Terytorium']).sum()
            df_p2 = df_p1.rename(columns={'Liczba osób': 'Przystąpiło'})

            df_z = df_zad2[df_zad2.Przystąpiło_zdało=="zdało"]
            df_z1= df_z.groupby(['Rok','Terytorium']).sum()
            df_z2 = df_z1.rename(columns={'Liczba osób': 'Zdało'})

            df_pz = df_p2.join(df_z2)
            df_pz['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2))

            df_zad3 = df_pz.groupby(['Rok','Terytorium']).max()
            df_zad3['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2))
            df_show = df_zad3.reset_index().values
            max_list = []
            adder = 0
            while adder < 144:
                for i in range(0+adder,16+adder):
                    max_list.append(df_show[i][4])
                max_value = max(max_list)
                max_year = df_show[adder + max_list.index(max_value)][0]
                max_woj = df_show[adder + max_list.index(max_value)][1]
                print(max_year,'-',max_woj)
                max_list = []
                adder += 16

        elif gender.lower() == 'w':
            df_wom2 = df_zad2[df_zad2.Płeć=='kobiety']
            df_p = df_wom2[df_wom2.Przystąpiło_zdało=="przystąpiło"]
            df_p1= df_p.groupby(['Rok','Terytorium']).sum()
            df_p2 = df_p1.rename(columns={'Liczba osób': 'Przystąpiło'})

            df_z = df_wom2[df_wom2.Przystąpiło_zdało=="zdało"]
            df_z1= df_z.groupby(['Rok','Terytorium']).sum()
            df_z2 = df_z1.rename(columns={'Liczba osób': 'Zdało'})

            df_pz = df_p2.join(df_z2)
            df_pz['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2))

            df_zad3 = df_pz.groupby(['Rok','Terytorium']).max()
            df_zad3['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2))
            df_show = df_zad3.reset_index().values

            max_list = []
            adder = 0
            while adder < 144:
                for i in range(0+adder,16+adder):
                    max_list.append(df_show[i][4])
                max_value = max(max_list)
                max_year = df_show[adder + max_list.index(max_value)][0]
                max_woj = df_show[adder + max_list.index(max_value)][1]
                print(max_year,'-',max_woj)
                max_list = []
                adder += 16
        elif gender.lower() == 'm':
            df_man2 = df_zad2[df_zad2.Płeć=='mężczyźni']
            df_p = df_man2[df_man2.Przystąpiło_zdało=="przystąpiło"]
            df_p1= df_p.groupby(['Rok','Terytorium']).sum()
            df_p2 = df_p1.rename(columns={'Liczba osób': 'Przystąpiło'})

            df_z = df_man2[df_man2.Przystąpiło_zdało=="zdało"]
            df_z1= df_z.groupby(['Rok','Terytorium']).sum()
            df_z2 = df_z1.rename(columns={'Liczba osób': 'Zdało'})

            df_pz = df_p2.join(df_z2)
            df_pz['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2))

            df_zad3 = df_pz.groupby(['Rok','Terytorium']).max()
            df_zad3['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2))
            df_show = df_zad3.reset_index().values

            max_list = []
            adder = 0
            while adder < 144:
                for i in range(0+adder,16+adder):
                    max_list.append(df_show[i][4])
                max_value = max(max_list)
                max_year = df_show[adder + max_list.index(max_value)][0]
                max_woj = df_show[adder + max_list.index(max_value)][1]
                print(max_year,'-',max_woj)
                max_list = []
                adder += 16
        elif gender.lower() == 'exit':
            break
        else:
            print("U can type only: 'a','w' or 'm'!")
        gender = input("For only women filter type: [w].\nFor only men filter type: [m].\nFor all type: [a]\nTo leave: [exit]\n")

def zad4():
    df_zad2 = df[df.Terytorium!="Polska"]
    gender = input("For only women filter type: [w].\nFor only men filter type: [m].\nFor all type: [a]\nTo leave: [exit]\n")
    while True:
        if gender.lower() == 'a':
            df_p = df_zad2[df_zad2.Przystąpiło_zdało=="przystąpiło"]
            df_p1= df_p.groupby(['Terytorium','Rok']).sum()
            df_p2 = df_p1.rename(columns={'Liczba osób': 'Przystąpiło'})

            df_z = df_zad2[df_zad2.Przystąpiło_zdało=="zdało"]
            df_z1= df_z.groupby(['Terytorium','Rok']).sum()
            df_z2 = df_z1.rename(columns={'Liczba osób': 'Zdało'})

            df_pz = df_p2.join(df_z2)
            df_pz['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2))

            df_show2 = df_pz.groupby(['Terytorium','Rok']).max()
            df_show2 = df_show2.reset_index().values
            #print(df_show2)
            counter = 0
            while counter < 144:
                if counter == 135:
                    for i in range(0+counter,8+counter):
                        temp_1 = df_show2[i][4]
                        year_1 = df_show2[i][1]
                        temp_2 = df_show2[i+1][4]
                        year_2 = df_show2[i+1][1]
                        if temp_2 < temp_1:
                            print('Województwo',df_show2[i][0],':', year_1,"->",year_2)
                        counter += 8
                else:
                    for i in range(0+counter,9+counter):
                        temp_1 = df_show2[i][4]
                        year_1 = df_show2[i][1]
                        temp_2 = df_show2[i+1][4]
                        year_2 = df_show2[i+1][1]
                        if temp_2 < temp_1:
                            print('Województwo',df_show2[i][0],':', year_1,"->",year_2)
                    counter += 9
        elif gender.lower() == 'w':
            df_wom3 = df_zad2[df_zad2.Płeć=='kobiety']
            df_p = df_wom3[df_wom3.Przystąpiło_zdało=="przystąpiło"]
            df_p1= df_p.groupby(['Terytorium','Rok']).sum()
            df_p2 = df_p1.rename(columns={'Liczba osób': 'Przystąpiło'})

            df_z = df_wom3[df_wom3.Przystąpiło_zdało=="zdało"]
            df_z1= df_z.groupby(['Terytorium','Rok']).sum()
            df_z2 = df_z1.rename(columns={'Liczba osób': 'Zdało'})

            df_pz = df_p2.join(df_z2)
            df_pz['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2))

            df_show2 = df_pz.groupby(['Terytorium','Rok']).max()
            df_show2 = df_show2.reset_index().values
            #print(df_show2)
            counter = 0
            while counter < 144:
                if counter == 135:
                    for i in range(0+counter,8+counter):
                        temp_1 = df_show2[i][4]
                        year_1 = df_show2[i][1]
                        temp_2 = df_show2[i+1][4]
                        year_2 = df_show2[i+1][1]
                        if temp_2 < temp_1:
                            print('Województwo',df_show2[i][0],':', year_1,"->",year_2)
                        counter += 8
                else:
                    for i in range(0+counter,9+counter):
                        temp_1 = df_show2[i][4]
                        year_1 = df_show2[i][1]
                        temp_2 = df_show2[i+1][4]
                        year_2 = df_show2[i+1][1]
                        if temp_2 < temp_1:
                            print('Województwo',df_show2[i][0],':', year_1,"->",year_2)
                    counter += 9
        elif gender.lower() == 'm':
            df_man3 = df_zad2[df_zad2.Płeć=='mężczyźni']
            df_p = df_man3[df_man3.Przystąpiło_zdało=="przystąpiło"]
            df_p1= df_p.groupby(['Rok','Terytorium']).sum()
            df_p2 = df_p1.rename(columns={'Liczba osób': 'Przystąpiło'})

            df_z = df_man3[df_man3.Przystąpiło_zdało=="zdało"]
            df_z1= df_z.groupby(['Rok','Terytorium']).sum()
            df_z2 = df_z1.rename(columns={'Liczba osób': 'Zdało'})

            df_pz = df_p2.join(df_z2)
            df_pz['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2))

            df_show2 = df_pz.groupby(['Terytorium','Rok']).max()
            df_show2 = df_show2.reset_index().values
            #print(df_show2)
            counter = 0
            while counter < 144:
                if counter == 135:
                    for i in range(0+counter,8+counter):
                        temp_1 = df_show2[i][4]
                        year_1 = df_show2[i][1]
                        temp_2 = df_show2[i+1][4]
                        year_2 = df_show2[i+1][1]
                        if temp_2 < temp_1:
                            print('Województwo',df_show2[i][0],':', year_1,"->",year_2)
                        counter += 8
                else:
                    for i in range(0+counter,9+counter):
                        temp_1 = df_show2[i][4]
                        year_1 = df_show2[i][1]
                        temp_2 = df_show2[i+1][4]
                        year_2 = df_show2[i+1][1]
                        if temp_2 < temp_1:
                            print('Województwo',df_show2[i][0],':', year_1,"->",year_2)
                    counter += 9
        elif gender.lower() == 'exit':
            break
        else:
            print("U can type only: 'a','w' or 'm'!")
        gender = input("For only women filter type: [w].\nFor only men filter type: [m].\nFor all type: [a]\nTo leave: [exit]\n")

def zad5():
    df_zad2 = df[df.Terytorium!="Polska"]
    gender = input("For only women filter type: [w].\nFor only men filter type: [m].\nFor all type: [a]\nTo leave: [exit]\n")
    while True:
        if gender.lower() == 'a':
            df_p = df_zad2[df_zad2.Przystąpiło_zdało=="przystąpiło"]
            df_p1= df_p.groupby(['Terytorium','Rok']).sum()
            df_p2 = df_p1.rename(columns={'Liczba osób': 'Przystąpiło'})

            df_z = df_zad2[df_zad2.Przystąpiło_zdało=="zdało"]
            df_z1= df_z.groupby(['Terytorium','Rok']).sum()
            df_z2 = df_z1.rename(columns={'Liczba osób': 'Zdało'})

            df_pz = df_p2.join(df_z2)
            df_pz['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2))

            df_zad5 = df_pz.groupby(['Terytorium','Rok']).max()
            df_comp = []
            df_zad5_output = ''
            df_zad5_output2 = ''
            type_1 = input('Type the name of 1st voivodeship:')
            type_2 = input('Type the name of 2nd voivodeship:')
            if type_1.isalpha() and type_2.isalpha():
                if type_1.capitalize() == type_2.capitalize():
                    print("Type two DIFFERENT voivodeship!")
                else:
                    df_zad5.reset_index().values
                    #print(df_zad5.reset_index().values)
                    for i in df_zad5.reset_index().values:
                        if i[0] == type_1.capitalize():
                            df_comp.append(i)
                        elif i[0] == type_2.capitalize():
                            df_comp.append(i)
                    if len(df_comp) < 18:
                        print("Type proper names of voivodeship!")
                    else:
                        df_df5 = pd.DataFrame(df_comp)
                        df_final_i_hope = df_df5.reset_index().values

                        for i in range(0,9):
                            max_1 = df_final_i_hope[i][5]
                            max_2 = df_final_i_hope[i+9][5]
                            if max_1 > max_2:
                                df_zad5_output = str(df_final_i_hope[i][2]) + ' - ' + 'Województwo: ' + str(df_final_i_hope[i][1]) + "\n"
                                df_zad5_output2 = df_zad5_output2 + str(df_zad5_output)
                            elif max_1 < max_2:
                                df_zad5_output = str(df_final_i_hope[i][2]) + ' - ' + 'Województwo: ' + str(df_final_i_hope[i+9][1]) + "\n"
                                df_zad5_output2 = df_zad5_output2 + str(df_zad5_output)
                        print(df_zad5_output2)
            else:
                print("Type letters only!")

        elif gender.lower() == 'w':
            df_wom4 = df_zad2[df_zad2.Płeć=='kobiety']
            df_p = df_wom4[df_wom4.Przystąpiło_zdało=="przystąpiło"]
            df_p1= df_p.groupby(['Terytorium','Rok']).sum()
            df_p2 = df_p1.rename(columns={'Liczba osób': 'Przystąpiło'})

            df_z = df_wom4[df_wom4.Przystąpiło_zdało=="zdało"]
            df_z1= df_z.groupby(['Terytorium','Rok']).sum()
            df_z2 = df_z1.rename(columns={'Liczba osób': 'Zdało'})

            df_pz = df_p2.join(df_z2)
            df_pz['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2))

            df_zad5 = df_pz.groupby(['Terytorium','Rok']).max()
            df_comp = []
            df_zad5_output = ''
            df_zad5_output2 = ''
            type_1 = input('Type the name of 1st voivodeship:')
            type_2 = input('Type the name of 2nd voivodeship:')
            if type_1.isalpha() and type_2.isalpha():
                if type_1.capitalize() == type_2.capitalize():
                    print("Type two DIFFERENT voivodeship!")
                else:
                    df_zad5.reset_index().values
                    #print(df_zad5.reset_index().values)
                    for i in df_zad5.reset_index().values:
                        if i[0] == type_1.capitalize():
                            df_comp.append(i)
                        elif i[0] == type_2.capitalize():
                            df_comp.append(i)
                    if len(df_comp) < 18:
                        print("Type proper names of voivodeship!")
                    else:
                        df_df5 = pd.DataFrame(df_comp)
                        df_final_i_hope = df_df5.reset_index().values

                        for i in range(0,9):
                            max_1 = df_final_i_hope[i][5]
                            max_2 = df_final_i_hope[i+9][5]
                            if max_1 > max_2:
                                df_zad5_output = str(df_final_i_hope[i][2]) + ' - ' + 'Województwo: ' + str(df_final_i_hope[i][1]) + "\n"
                                df_zad5_output2 = df_zad5_output2 + str(df_zad5_output)
                            elif max_1 < max_2:
                                df_zad5_output = str(df_final_i_hope[i][2]) + ' - ' + 'Województwo: ' + str(df_final_i_hope[i+9][1]) + "\n"
                                df_zad5_output2 = df_zad5_output2 + str(df_zad5_output)
                        print(df_zad5_output2)
            else:
                print("Type letters only!")

        elif gender.lower() == 'm':
            df_man4 = df_zad2[df_zad2.Płeć=='mężczyźni']
            df_p = df_man4[df_man4.Przystąpiło_zdało=="przystąpiło"]
            df_p1= df_p.groupby(['Rok','Terytorium']).sum()
            df_p2 = df_p1.rename(columns={'Liczba osób': 'Przystąpiło'})

            df_z = df_man4[df_man4.Przystąpiło_zdało=="zdało"]
            df_z1= df_z.groupby(['Rok','Terytorium']).sum()
            df_z2 = df_z1.rename(columns={'Liczba osób': 'Zdało'})

            df_pz = df_p2.join(df_z2)
            df_pz['Zdawalność']=(round(df_pz['Zdało']/df_pz['Przystąpiło']*100,2))

            df_zad5 = df_pz.groupby(['Terytorium','Rok']).max()
            df_comp = []
            df_zad5_output = ''
            df_zad5_output2 = ''
            type_1 = input('Type the name of 1st voivodeship:')
            type_2 = input('Type the name of 2nd voivodeship:')
            if type_1.isalpha() and type_2.isalpha():
                if type_1.capitalize() == type_2.capitalize():
                    print("Type two DIFFERENT voivodeship!")
                else:
                    df_zad5.reset_index().values
                    #print(df_zad5.reset_index().values)
                    for i in df_zad5.reset_index().values:
                        if i[0] == type_1.capitalize():
                            df_comp.append(i)
                        elif i[0] == type_2.capitalize():
                            df_comp.append(i)
                    if len(df_comp) < 18:
                        print("Type proper names of voivodeship!")
                    else:
                        df_df5 = pd.DataFrame(df_comp)
                        df_final_i_hope = df_df5.reset_index().values

                        for i in range(0,9):
                            max_1 = df_final_i_hope[i][5]
                            max_2 = df_final_i_hope[i+9][5]
                            if max_1 > max_2:
                                df_zad5_output = str(df_final_i_hope[i][2]) + ' - ' + 'Województwo: ' + str(df_final_i_hope[i][1]) + "\n"
                                df_zad5_output2 = df_zad5_output2 + str(df_zad5_output)
                            elif max_1 < max_2:
                                df_zad5_output = str(df_final_i_hope[i][2]) + ' - ' + 'Województwo: ' + str(df_final_i_hope[i+9][1]) + "\n"
                                df_zad5_output2 = df_zad5_output2 + str(df_zad5_output)
                        print(df_zad5_output2)
            else:
                print("Type letters only!")
        elif gender.lower() == 'exit':
            break
        else:
            print("U can type only: 'a','w' or 'm'!")
        gender = input("For only women filter type: [w].\nFor only men filter type: [m].\nFor all type: [a]\nTo leave: [exit]\n")
zad5()
