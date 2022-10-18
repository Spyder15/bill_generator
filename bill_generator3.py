def main():
    while True:

        def parse_value(data):
            # this will give us a list from string
            parse_list_2 = data.split(',')

            return parse_list_2.copy()

        def get_data():
            big_list = []
            take_list = []

            with open("name.txt") as f:
                data1 = f.readline()  # read data from txt file and save in this
                # parse(bhagla) data from string and get list of item
                take_list = parse_value(data1)
                big_list.append(take_list.copy())

            with open("quntity.txt") as f:
                data2 = f.readline()
                take_list = parse_value(data2)
                big_list.append(take_list.copy())

            with open("exp.txt") as f:
                data3 = f.readline()
                take_list = parse_value(data3)
                big_list.append(take_list.copy())

            with open("mfg.txt") as f:
                data4 = f.readline()
                take_list = parse_value(data4)
                big_list.append(take_list.copy())

            with open("price.txt") as f:
                data5 = f.readline()
                take_list = parse_value(data5)
                big_list.append(take_list.copy())

            with open("net_price.txt") as f:
                data6 = f.readline()
                take_list = parse_value(data6)
                big_list.append(take_list.copy())

            return big_list.copy()

        def remove_back_slash_n():
            main_list = get_data()

            for list in main_list:
                last_element = list[len(list)-1]
                last_element = last_element.replace('\n', '')
                list[len(list)-1] = last_element

            return main_list

        data = remove_back_slash_n()
        print(data)

        def check_quntity():
            data = remove_back_slash_n()
            medicine_name = data[0]  # save list(name) of medicine
            quntity = data[1]  # save quntity of medicine
            # enter name by user to check quntity of medicine
            user = input("enter medicine name :")
            user = user.lower()
            user_split = user.split(" ")
            suggestion_index = []  # this list for store suggestion of medicine index number
            suggestion_med_name = []  # this list for store suggestion of medicine name

            # for get suggetion index number of medicine entered by user
            index = -1
            for i in medicine_name:
                index = index + 1
                split_med_name = i.split(" ")

                for keyword1 in split_med_name:
                    for keyword2 in user_split:
                        if keyword1 == keyword2:

                            suggestion_index.append(index)
            print(suggestion_index)

        # for get suggetion medicine name of medicine entered by user
            tmp_index1 = -1
            for i in suggestion_index:
                tmp_index1 = tmp_index1 + 1
                tmp_index = suggestion_index[tmp_index1]

                tmp_med_name = medicine_name[tmp_index]
                suggestion_med_name.append(tmp_med_name)
        # above two (for loop) for give suggestion to user for easily acces of medicine

        # for print medicine from suggestion med name choosen by user
            tmp_index2 = -1
            for item in suggestion_med_name:
                tmp_index2 = tmp_index2 + 1
                print(suggestion_med_name[tmp_index2],
                    "press this number for check quntity", suggestion_index[tmp_index2])
            for_quntity_check = input("enter number\n")
            for_quntity_check = int(for_quntity_check)
            med_final_quntity = quntity[for_quntity_check]
            if med_final_quntity == 0:
                print("medicine is not available")
            else:
                print("medicine is available and quntity is ", med_final_quntity)

        def insert_medicine():
            data = remove_back_slash_n()

            name = data[0]
            print(type(name))
            name_add = input("enter a name...\n")
            name.append(name_add)
            name_index = -1
            f = open("name.txt", "a")
            f.truncate(0)
            for i in name:
                name_index = name_index + 1
                added_name = name[name_index]
                if name_index == len(name) - 1:
                    f.write(added_name)
                else:
                    f.write(added_name)
                    f.write(",")

            quntity = data[1]
            quntity_add = input("enter a quntity\n")
        #  quntity_add = int(quntity_add)
            quntity.append(quntity_add)
            quntity_index = -1
            f = open("quntity.txt", "a")
            f.truncate(0)
            for item in quntity:
                quntity_index = quntity_index + 1
                added_quntity = quntity[quntity_index]
                if quntity_index == len(quntity) - 1:
                    f.write(added_quntity)
                else:
                    f.write(added_quntity)
                    f.write(",")

            exp = data[2]
            exp_add = input("enter a exp...\n")
            exp.append(exp_add)
            exp_index = -1
            f = open("exp.txt", "a")
            f.truncate(0)
            for item in exp:
                exp_index = exp_index + 1
                added_exp = exp[exp_index]
                if exp_index == len(exp) - 1:
                    f.write(added_exp)
                else:
                    f.write(added_exp)
                    f.write(",")

            mfg = data[3]
            mfg_add = input("enter a mfg...\n")
            mfg.append(mfg_add)
            mfg_index = -1
            f = open("mfg.txt", "a")
            f.truncate(0)
            for item in mfg:
                mfg_index = mfg_index + 1
                added_mfg = mfg[mfg_index]
                if mfg_index == len(mfg) - 1:
                    f.write(added_mfg)
                else:
                    f.write(added_mfg)
                    f.write(",")

            price = data[4]
            price_add = input("enter a price...\n")
        #  price_add = int(price_add)
            price.append(price_add)
            price_index = -1
            f = open("price.txt", "a")
            f.truncate(0)
            for item in price:
                price_index = price_index + 1
                added_price = price[price_index]
                if price_index == len(price) - 1:
                    f.write(added_price)
                else:
                    f.write(added_price)
                    f.write(",")

            net_price = data[5]
            net_price_add = input("enter a net price...\n")
        #  net_price_add = int(net_price_add)
            net_price.append(net_price_add)
            net_price_index = -1
            f = open("net_price.txt", "a")
            f.truncate(0)
            for item in net_price:
                net_price_index = net_price_index + 1
                added_net_price = net_price[net_price_index]
                if net_price_index == len(net_price) - 1:
                    f.write(added_net_price)
                else:
                    f.write(added_net_price)
                    f.write(",")
        #  print(data)

        def generate_bill():
            data = remove_back_slash_n()
            cust_list = []  # this is the list which will given to the customer

            # below are all that temporary lists we create to store data inserted by user for customer
            tmp_name = []
            tmp_quntity = []
            tmp_exp = []
            tmp_mfg = []
            tmp_price = []
            tmp_net_price = []

            # after that we append all temporary lists in our cust_list
            cust_name = input("enter customer name...\n")
            medicine_name = data[0]
            quntity = data[1]
            exp = data[2]
            mfg = data[3]
            price = data[4]
            net_price = data[5]
            while True:
                
                med_name_cust = input("enter 1 for purchase medicine or enter 0 for ok...\n")
                med_name_cust = int(med_name_cust)
                
                if med_name_cust == 0:
                    print("this is your bill...")
                    print("custmer name is ", cust_name)
                    cust_list.append(tmp_name.copy())
                    cust_list.append(tmp_quntity.copy())
                    cust_list.append(tmp_exp.copy())
                    cust_list.append(tmp_mfg.copy())
                    cust_list.append(tmp_price.copy())
                    cust_list.append(tmp_net_price.copy())

                    # this below task done for store rest of data after customer get their medicine
                    tmp_index = -1
                    for i in tmp_quntity:
                        tmp_index = tmp_index + 1
                        var = tmp_name[tmp_index]
                        index = medicine_name.index(var)
                        # this line for deduct(minus) customer medicine from database
                        quntity[index] = int(quntity[index]) - \
                                            int(tmp_quntity[tmp_index])
                        quntity[index] = str(quntity[index])

                    tmp_index1 = -1
                    f = open("quntity.txt", "a")
                    f.truncate(0)

                    for items in quntity:
                        tmp_index1 = tmp_index1 + 1
                        return_data = quntity[tmp_index1]
                        if tmp_index1 == len(quntity)-1:
                            f.write(return_data)
                        else:
                            f.write(return_data)
                            f.write(",")
                    print(cust_list)
                    break

                elif med_name_cust == 1:  
                    user = input("enter medicine name :")
                    user = user.lower()
                    user_split = user.split(" ")
                    suggestion_index = []  # this list for store suggestion of medicine index number
                    suggestion_med_name = []  # this list for store suggestion of medicine name

                # for get suggetion index number of medicine entered by user
                index = -1
                for i in medicine_name:
                    index = index + 1
                    split_med_name = i.split(" ")

                    for keyword1 in split_med_name:
                        for keyword2 in user_split:
                            if keyword1 == keyword2:
                                suggestion_index.append(index)
                    # print(suggestion_index)

                # for get suggetion medicine name of medicine entered by user
                tmp_index1 = -1
                for i in suggestion_index:
                    tmp_index1 = tmp_index1 + 1
                    tmp_index = suggestion_index[tmp_index1]
    
                    tmp_med_name = medicine_name[tmp_index]
                    suggestion_med_name.append(tmp_med_name)
                # above two (for loop) for give suggestion to user for easily acces of medicine 

                tmp_index2 = -1
                for item in suggestion_med_name:
                    tmp_index2 = tmp_index2 + 1
                    print(suggestion_med_name[tmp_index2], "press this number for add this medicine to bill", suggestion_index[tmp_index2])
                for_add_in_bill = input("enter number\n")
                for_add_in_bill = int(for_add_in_bill)
                med_name_cust2 = medicine_name[for_add_in_bill]
                
                index = medicine_name.index(med_name_cust2)
                if (quntity[index] == 0):
                        print("medicine is not available ")
                else:
                        cust_quntity = int(input("enter quntity custmoer need..."))
                        if cust_quntity == 0:
                            print("please enter properly")
                            cust_quntity = int(input("enter quntity custmoer need..."))
                        elif cust_quntity > int(quntity[index]):
                            print("entered quntity of medicine is more than available quntity , please enter valid amount of medicine")    
                            cust_quntity = int(input("enter quntity custmoer need..."))
                        elif cust_quntity < 0 :
                            print("entered quntity of medicine is in negative value , please enter properly")   
                            cust_quntity = int(input("enter quntity custmoer need..."))
                            print("your medicine is added in bill you will get bill after you press 0...")
                            tmp_name.append(med_name_cust2)

                            tmp_quntity.append(cust_quntity)

                            tmp_exp.append(exp[index])

                            tmp_mfg.append(mfg[index])

                            tmp_price.append(price[index])

                            tmp_net_price.append(net_price[index])

        print("what you want to do?\n")
        print("1.check quntity\n")
        print("2.add new medicine\n")
        print("3.bill generate\n")
        enter = input("enter your choice...\n")
        enter = int(enter)

        if enter == 1:
            check = check_quntity()

        elif enter == 2:
            new = insert_medicine()

        elif enter == 3:
            generate = generate_bill()


while(True):
    try:
        main()
    except KeyboardInterrupt:
        print("Programm ends here...")
        break
    except:
        print("Enter Valid Input....")
