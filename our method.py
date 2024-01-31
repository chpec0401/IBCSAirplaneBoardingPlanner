import numpy as np, pandas as pd, random, matplotlib.pyplot as plt, seaborn as sns
from IPython.display import clear_output
from PyProbs import Probability as pr

class passenger(object):
    def __init__(self,disabled,purse,luggage):
        self.aisle = 0
        self.seat = 0
        self.speed = 99 - 50*pr.Prob(3/100)
        self.purse = pr.Prob(50/100)
        self.carry = pr.Prob(30/100)
        self.purse = 0
        self.carry = 0
        self.timer = 2
        self.first = 1
        self.action = 0
        self.board = 0
        self.wait = 0
        self.walk = 0
        self.bag = 0
        self.stop_counter = 0
        self.prev_stop = 0



def initialize_array(narrow):
    for i in range(32):
        narrow[i][7] = 12
    return narrow

def initialize_timer(p_list):
    for i in range(len(p_list)):
        p_list[i].timer += int(np.random.weibull(2)*(3*p_list[i].purse + 5*p_list[i].carry))
    return p_list

def run_narrow(p_list, narrow,s):
    plt.close("all")
    a = 0
    #fig, ax = plt.subplots()
    #plt.ion()
    #plt.show()
    sit = 0
    time = 0
    seated = []
    viewer = zeros = [[0] * 7 for _ in range(32)]
    while sit < 192:
        time += 1
        for i in range(32):
            change = 0
            if narrow[i][3] != 0 and narrow[i][3].action == 0:
                narrow[i][3].action = 1
                if narrow[i][3].aisle != i:
                    if narrow[i+1][3] == 0:
                        narrow[i][3].prev_stop = 0
                        if random.randrange(100) < narrow[i][3].speed:
                            narrow[i+1][3] = narrow[i][3]
                            narrow[i][3] = 0
                            change = 1
                    else:
                        narrow[i][3].wait += 1
                        if narrow[i][3].prev_stop == 0:
                            narrow[i][3].prev_stop = 1
                            narrow[i][3].stop_counter += 1
                else:
                    if narrow[i][3].first:
                        narrow[i][3].first = 0
                        if narrow[i][7] < 0:
                            narrow[i][3].timer += 5
                        else:
                            narrow[i][3].timer += int(3.07*10**(-5))*np.e**(12-narrow[i][7])
                        narrow[i][7] -= narrow[i][3].purse + narrow[i][3].carry
                        if narrow[i][3].seat == 0:
                            narrow[i][3].timer +=  int(np.random.weibull(2))*(5*narrow[i][1] + 3*narrow[i][2])
                        elif narrow[i][3].seat == 1:
                            narrow[i][3].timer += int(np.random.weibull(2))*(3*narrow[i][2])
                        elif narrow[i][3].seat == 5:
                            narrow[i][3].timer += int(np.random.weibull(2))*(3*narrow[i][4])
                        elif narrow[i][3].seat == 6:
                            narrow[i][3].timer += int(np.random.weibull(2))*(5*narrow[i][5] + 3*narrow[i][4])
                        if narrow[i][3].speed == 49:
                            narrow[i][3].timer *= 2
                        narrow[i][3].bag = narrow[i][3].timer
                    if narrow[i][3].timer != 0:
                        narrow[i][3].timer -= 1
                    else:
                        change = 1
                        if narrow[i][3].seat >= 3:
                            narrow[i][narrow[i][3].seat + 1] = 1
                            sit += 1
                        else:
                            narrow[i][narrow[i][3].seat] = 1
                            sit += 1
                        seated.append(narrow[i][3])
                        narrow[i][3] = 0
            if i == 0:
                if narrow[i][3] == 0 and len(p_list) != 0:
                    narrow[i][3] = p_list.pop()
                    narrow[i][3].action = 1
                    change = 1

        for i in range(32):
            for j in range(7):
                if narrow[i][j] != 0:
                    if j != 3:
                        viewer[i][j] = 10
                    else:
                        if narrow[i][j].speed == 49:
                            viewer[i][j] = 3
                        else:
                            viewer[i][j] = 10
                elif j == 3:
                    viewer[i][j] = 0
                else:
                    viewer[i][j] = 5
        plt.close()

        #plt.draw()
        if time % 6 == 0 or sit > 191:
            plt.savefig('C:\\Users\\Eric Chang\\PycharmProjects\IA\\'+s+'\\' + str(a) + '.png')
            a += 1
            plt.close()
            fig, ax = plt.subplots()
            im = ax.imshow(viewer, cmap='summer', vmin=0, vmax=10)

        for i in range(32):
            if narrow[i][3] != 0:
                narrow[i][3].action = 0
                narrow[i][3].board += 1
    board_time = []
    wait_time = []
    bag_time = []
    stop_counter = []
    for i in range(len(seated)):
        board_time.append(seated[i].board)
        wait_time.append(seated[i].wait)
        bag_time.append(seated[i].bag)
        stop_counter.append(seated[i].stop_counter)
    return time, np.mean(board_time), np.mean(wait_time), np.mean(bag_time), np.mean(stop_counter)
class our():
    def __init__(self,disabled,purse,luggage):
        time = []
        board_avg = []
        wait_avg = []
        bag_avg = []
        stop_avg = []
        for i in range(1):
            p_list = self.create_passenger_list(disabled,purse,luggage)
            p_list = initialize_timer(p_list)
            narrow = [[0] * 8 for _ in range(32)]
            narrow = initialize_array(narrow)
            a, b, c, d, e = run_narrow(p_list, narrow, 'our')
            time.append(a)
            board_avg.append(b)
            wait_avg.append(c)
            bag_avg.append(d)
            stop_avg.append(e)
        self.t=np.mean(time)
        np_time = np.array(time)
        np_board_avg = np.array(board_avg)
        np_wait_avg = np.array(wait_avg)
        np_bag_avg = np.array(bag_avg)
        np_stop_avg = np.array(stop_avg)
        #np.save('dis2_time.npy', np_time)
        #np.save('dis2_board_avg.npy', np_board_avg)
        #np.save('dis2_wait_avg.npy', np_wait_avg)
        #np.save('dis2_bag_avg.npy', np_bag_avg)
        #np.save('dis2_stop_avg.npy', np_stop_avg)

    def create_passenger_list(self, disabled, purse, luggage):
        p_list = []
        for i in range(32 * 6):
            p_list.append(passenger(disabled, purse, luggage))
            p_list[i].aisle = i // 6
            p_list[i].seat = i % 6
        # p_list.reverse()
        # random.shuffle(p_list)
        temp = p_list[:64]
        random.shuffle(temp)
        p_list[:64] = temp
        temp = p_list[64:128]
        random.shuffle(temp)
        p_list[64:128] = temp
        temp = p_list[128:]
        random.shuffle(temp)
        p_list[128:] = temp
        # random.shuffle(p_list[64:128])
        # random.shuffle(p_list[128:])
        return p_list
    def returnTime(self):
        return self.t
class outsidein():
    def __init__(self,disabled,purse,luggage):
        time = []
        board_avg = []
        wait_avg = []
        bag_avg = []
        stop_avg = []
        for i in range(1):
            p_list = self.create_passenger_list(disabled,purse,luggage)
            p_list = initialize_timer(p_list)
            narrow = [[0] * 8 for _ in range(32)]
            narrow = initialize_array(narrow)
            a, b, c, d, e = run_narrow(p_list, narrow, 'outsidein')
            time.append(a)
            board_avg.append(b)
            wait_avg.append(c)
            bag_avg.append(d)
            stop_avg.append(e)
        self.t=np.mean(time)
        np_time = np.array(time)
        np_board_avg = np.array(board_avg)
        np_wait_avg = np.array(wait_avg)
        np_bag_avg = np.array(bag_avg)
        np_stop_avg = np.array(stop_avg)
        #np.save('dis2_time.npy', np_time)
        #np.save('dis2_board_avg.npy', np_board_avg)
        #np.save('dis2_wait_avg.npy', np_wait_avg)
        #np.save('dis2_bag_avg.npy', np_bag_avg)
        #np.save('dis2_stop_avg.npy', np_stop_avg)

    def create_passenger_list(self, disabled, purse, luggage):
        p_list = []
        for i in range(6):
            for j in range(32):
                p_list.append(passenger(disabled, purse, luggage))
                p_list[i * 32 + j].aisle = j
                p_list[i * 32 + j].seat = i
        p_list_2 = []
        p_list_2.extend(p_list[:32])
        p_list_2.extend(p_list[-32:])
        p_list_3 = []
        p_list_3.extend(p_list[32:64])
        p_list_3.extend(p_list[-64:-32])
        p_list_4 = []
        p_list_4.extend(p_list[64:96])
        p_list_4.extend(p_list[-96:-64])
        random.shuffle(p_list_2)
        random.shuffle(p_list_3)
        random.shuffle(p_list_4)
        p_list[:64] = p_list_2
        p_list[64:128] = p_list_3
        p_list[128:] = p_list_4
        p_list.reverse()
        return p_list
    def returnTime(self):
        return self.t
class reversepy():
    def __init__(self,disabled,purse,luggage):
        time = []
        board_avg = []
        wait_avg = []
        bag_avg = []
        stop_avg = []
        for i in range(1):
            p_list = self.create_passenger_list(disabled,purse,luggage)
            p_list = initialize_timer(p_list)
            narrow = [[0] * 8 for _ in range(32)]
            narrow = initialize_array(narrow)
            a, b, c, d, e = run_narrow(p_list, narrow, 'reversepy')
            time.append(a)
            board_avg.append(b)
            wait_avg.append(c)
            bag_avg.append(d)
            stop_avg.append(e)
        self.t=np.mean(time)
        np_time = np.array(time)
        np_board_avg = np.array(board_avg)
        np_wait_avg = np.array(wait_avg)
        np_bag_avg = np.array(bag_avg)
        np_stop_avg = np.array(stop_avg)
        #np.save('dis2_time.npy', np_time)
        #np.save('dis2_board_avg.npy', np_board_avg)
        #np.save('dis2_wait_avg.npy', np_wait_avg)
        #np.save('dis2_bag_avg.npy', np_bag_avg)
        #np.save('dis2_stop_avg.npy', np_stop_avg)

    def create_passenger_list(self,disabled,purse,luggage):
        p_list = []
        for i in range(4):
            for j in range(48):
                p_list.append(passenger(disabled,purse,luggage))
                if i == 0:
                    if j % 2 == 0:
                        p_list[48 * i + j].seat = 0
                    else:
                        p_list[48 * i + j].seat = 5
                    p_list[48 * i + j].aisle = 31 - j // 2
                if i == 1:
                    if j < 16:
                        if j % 2 == 0:
                            p_list[48 * i + j].seat = 0
                        else:
                            p_list[48 * i + j].seat = 5
                        p_list[48 * i + j].aisle = 31 - (j // 2 + 24)
                    else:
                        if j % 2 == 0:
                            p_list[48 * i + j].seat = 1
                        else:
                            p_list[48 * i + j].seat = 4
                        p_list[48 * i + j].aisle = 31 - (j // 2 - 8)
                if i == 2:
                    if j < 32:
                        if j % 2 == 0:
                            p_list[48 * i + j].seat = 1
                        else:
                            p_list[48 * i + j].seat = 4
                        p_list[48 * i + j].aisle = 31 - (j // 2 + 16)
                    else:
                        if j % 2 == 0:
                            p_list[48 * i + j].seat = 2
                        else:
                            p_list[48 * i + j].seat = 3
                        p_list[48 * i + j].aisle = 31 - (j // 2 - 16)
                if i == 3:
                    if j % 2 == 0:
                        p_list[48 * i + j].seat = 2
                    else:
                        p_list[48 * i + j].seat = 3
                    p_list[48 * i + j].aisle = 31 - (j // 2 + 8)
        p_list_1 = p_list[:48]
        p_list_2 = p_list[48:96]
        p_list_3 = p_list[96:144]
        p_list_4 = p_list[144:]
        random.shuffle(p_list_1)
        random.shuffle(p_list_2)
        random.shuffle(p_list_3)
        random.shuffle(p_list_4)
        p_list[:48] = p_list_1
        p_list[48:96] = p_list_2
        p_list[96:144] = p_list_3
        p_list[144:] = p_list_4
        p_list.reverse()
        return p_list
    def returnTime(self):
        return self.t
class backfront():
    def __init__(self,disabled,purse,luggage):
        time = []
        board_avg = []
        wait_avg = []
        bag_avg = []
        stop_avg = []
        for i in range(1):
            p_list = self.create_passenger_list(disabled,purse,luggage)
            p_list = initialize_timer(p_list)
            narrow = [[0] * 8 for _ in range(32)]
            narrow = initialize_array(narrow)
            a, b, c, d, e = run_narrow(p_list, narrow, 'backfront')
            time.append(a)
            board_avg.append(b)
            wait_avg.append(c)
            bag_avg.append(d)
            stop_avg.append(e)
        self.t=np.mean(time)
        np_time = np.array(time)
        np_board_avg = np.array(board_avg)
        np_wait_avg = np.array(wait_avg)
        np_bag_avg = np.array(bag_avg)
        np_stop_avg = np.array(stop_avg)
        #np.save('dis2_time.npy', np_time)
        #np.save('dis2_board_avg.npy', np_board_avg)
        #np.save('dis2_wait_avg.npy', np_wait_avg)
        #np.save('dis2_bag_avg.npy', np_bag_avg)
        #np.save('dis2_stop_avg.npy', np_stop_avg)

    def create_passenger_list(self, disabled, purse, luggage):
        p_list = []
        for i in range(32 * 6):
            p_list.append(passenger(disabled, purse, luggage))
            p_list[i].aisle = i // 6
            p_list[i].seat = i % 6
        # p_list.reverse()
        # random.shuffle(p_list)
        temp = p_list[:64]
        random.shuffle(temp)
        p_list[:64] = temp
        temp = p_list[64:128]
        random.shuffle(temp)
        p_list[64:128] = temp
        temp = p_list[128:]
        random.shuffle(temp)
        p_list[128:] = temp
        # random.shuffle(p_list[64:128])
        # random.shuffle(p_list[128:])
        return p_list
        return p_list
    def returnTime(self):
        return self.t
print(our(0.2,0.2,0.2).returnTime())