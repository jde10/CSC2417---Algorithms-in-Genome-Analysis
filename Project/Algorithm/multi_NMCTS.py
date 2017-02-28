from Node import Node
import itertools
import datetime
import numpy as np
import math as m
import random

class NMonteCarlo:
    def __init__(self, sequence, id, name, pair_time, total_time, multi):

        print 'Initiated'
        self.id = id
        self.sequence = sequence
        self.seq1 = []
        self.seq2 = []
        self.multi = multi
        self.cp = m.sqrt(2) #1 / m.sqrt(2)
        # for pairwise aligments
        seconds = pair_time
        self.calculation_time = datetime.timedelta(seconds=seconds)

        #for the complete algorithm
        big_seconds = total_time # 10800 is 3 hours, 3600 is 1 hour, 7200 is 2 hours
        self.big_calculation_time = datetime.timedelta(seconds=big_seconds)

        # scores
        self.m = 0 # match
        self.w = 3 # mismatch
        self.g = 2 # insertion or deletion


        # Start
        final_state, seq_order, id_in_order = self.upper_search()

        np.savez('align_'+ name, alignment=final_state, order=seq_order, id_order=id_in_order)




    def complete_node(self, v):
        if (v.i < len(self.seq1)) and (v.j < len(self.seq2)) and (v.hasLeftChild() is False):
            # left child missing
            return False
        if (v.i < len(self.seq1)) and (v.hasMiddleChild() is False):
            # middle child missing
            return False
        if (v.j < len(self.seq2)) and (v.hasRightChild() is False):
            # right child missing
            return False
        else:
            return True

    def back_up(self, v, delta_reward):

        while True:
            if v.parent is not None:
                v.N += 1
                v.Q = delta_reward #changed this, used to be +=  -----------------------------------------
                v = v.parent
            else:
                break

    def rdefault_policy(self, v):
        # type: (v) -> Node
        n_state = v.s
        ith = v.i
        jth = v.j
        n_rew = v.Q

        while ith < (len(self.seq1)) and jth < (len(self.seq2)):
            rand_act = np.random.choice(np.arange(-1, 2), p=[0.9, 0.05, 0.05])
            acted = False

            if rand_act == -1 and ith < len(self.seq1) and jth < len(self.seq2):
                if self.seq1[ith] == self.seq2[jth]:
                    n_state=[[''.join(n_state[0])+self.seq1[ith]],[''.join(n_state[1])+self.seq2[jth]]]
                    ith += 1
                    jth += 1
                    n_rew += self.m
                else:
                    n_state = [[''.join(n_state[0]) + self.seq1[ith]], [''.join(n_state[1]) + self.seq2[jth]]]
                    ith += 1
                    jth += 1
                    n_rew += self.w
            elif rand_act == 0 and ith < len(self.seq1):
                n_state=[[''.join(n_state[0]) + self.seq1[ith]], [''.join(n_state[1]) + '-']]
                ith += 1
                n_rew += self.g
            elif rand_act == 1 and jth < len(self.seq2):
                n_state=[[''.join(n_state[0]) + '-'], [''.join(n_state[1]) + self.seq2[jth]]]
                jth += 1
                n_rew += self.g

        #v.Q = n_rew
        return n_rew

    def best_child(self, v, c):

        if v.hasThreeChildren():
            ev = np.zeros(shape=(3, 1))
            v_l = v.leftChild
            v_m = v.middleChild
            v_r = v.rightChild

            ev[0] = (v_l.Q / v_l.N) + c * np.sqrt((2 * np.log(v.N)) / v_l.N)
            ev[1] = (v_m.Q / v_m.N) + c * np.sqrt((2 * np.log(v.N)) / v_m.N)
            ev[2] = (v_r.Q / v_r.N) + c * np.sqrt((2 * np.log(v.N)) / v_r.N)

            child_index = np.argmin(ev)

            if child_index == 0:
                return v_l
            elif child_index == 1:
                return v_m
            elif child_index == 2:
                return v_r

        elif v.hasMidandRightChildren():
            ev = np.zeros(shape=(2, 1))
            v_m = v.middleChild
            v_r = v.rightChild
            ev[0] = (v_m.Q / v_m.N) + c * np.sqrt((2 * np.log(v.N)) / v_m.N)
            ev[1] = (v_r.Q / v_r.N) + c * np.sqrt((2 * np.log(v.N)) / v_r.N)

            child_index = np.argmin(ev)

            if child_index == 0:
                return v_m
            else:
                return v_r

        elif v.rightChild is not None and v.leftChild is not None:
            ev = np.zeros(shape=(2, 1))
            v_l = v.leftChild
            v_r = v.rightChild
            ev[0] = (v_l.Q / v_l.N) + c * np.sqrt((2 * np.log(v.N)) / v_l.N)
            ev[1] = (v_r.Q / v_r.N) + c * np.sqrt((2 * np.log(v.N)) / v_r.N)

            child_index = np.argmin(ev)

            if child_index == 0:
                return v_l
            else:
                return v_r

        elif v.middleChild is not None and v.leftChild is not None:
            ev = np.zeros(shape=(2, 1))
            v_l = v.leftChild
            v_m = v.middleChild
            ev[0] = (v_l.Q / v_l.N) + c * np.sqrt((2 * np.log(v.N)) / v_l.N)
            ev[1] = (v_m.Q / v_m.N) + c * np.sqrt((2 * np.log(v.N)) / v_m.N)

            child_index = np.argmin(ev)

            if child_index == 0:
                return v_l
            else:
                return v_m

        elif v.leftChild is not None and v.rightChild is None and v.middleChild is None:
            return v.leftChild
        elif v.leftChild is None and v.rightChild is not None and v.middleChild is None:
                return v.rightChild
        elif v.leftChild is None and v.rightChild is None and v.middleChild is not None:
                return v.middleChild

    def rexpand(self, v):
        while True:
            rand_act = np.random.choice(np.arange(-1, 2), p=[0.9, 0.05, 0.05])
            if rand_act == -1 and (v.hasLeftChild() is False) and v.i < (len(self.seq1)) and v.j < (len(self.seq2)):
                if self.seq1[v.i] == self.seq2[v.j]:
                    # match
                    v_n = Node(visited=1, reward=v.Q+self.m, action=v.a+['m'],
                               state=[[''.join(v.s[0])+self.seq1[v.i]], [''.join(v.s[1])+self.seq2[v.j]]], i=v.i+1, j=v.j+1, parent=v)
                    v.leftChild = v_n
                    return v_n

                else:
                    # mismatch
                    v_n = Node(visited=1, reward=v.Q+self.w, action=v.a + ['w'],
                               state=[[''.join(v.s[0])+self.seq1[v.i]], [''.join(v.s[1])+self.seq2[v.j]]], i=v.i+1, j=v.j+1,
                               parent=v)
                    v.leftChild = v_n
                    return v_n

            if rand_act == 0 and (v.hasMiddleChild() is False) and (v.i < (len(self.seq1))):
                # deletion
                v_n = Node(visited=1, reward=v.Q+self.g, action=v.a+['d'],
                           state=[[''.join(v.s[0])+self.seq1[v.i]], [''.join(v.s[1])+'-']], i=v.i+1, j=v.j, parent=v)
                v.middleChild = v_n
                return v_n

            if rand_act == 1 and (v.hasRightChild() is False) and v.j < (len(self.seq2)):
                # insertion
                v_n = Node(visited=1, reward=v.Q+self.g, action=v.a+['i'],
                           state=[[''.join(v.s[0])+'-'], [''.join(v.s[1])+self.seq2[v.j]]], i=v.i, j=v.j+1, parent=v)
                v.rightChild = v_n
                return v_n



    def tree_policy(self, v):

        while v.i < (len(self.seq1)) or v.j < (len(self.seq2)):
            # do while v is non terminal
            if self.complete_node(v) is False:
                return self.rexpand(v)
            else:
                v = self.best_child(v, self.cp)
        return v

    def UCTSearch(self):

        # Create root node v_0 with state s_0
        v_0 = Node(visited=1, reward=0, action=[], state=[[], []], i=0, j=0, left=None,
                   middle=None, right=None, parent=None)

        # Computational Budget

        begin = datetime.datetime.utcnow()

        while datetime.datetime.utcnow() - begin < self.calculation_time:
            v_l = self.tree_policy(v_0)
            # ask about this, i am sending the node
            delta_reward = self.rdefault_policy(v_l)
            self.back_up(v_l, delta_reward)

        v = v_0
        while True:
            if v.isLeaf() is False:
                v = self.best_child(v, 0)
            else:
                return v.s
        #return self.best_child(v_0, 0).s

    def inner_search(self, s1, s2):
        # type: (list, list) -> list
        self.seq1 = ''.join(s1)
        self.seq2 = ''.join(s2)

        v_0 = Node(visited=1, reward=0, action=[], state=[[], []], i=0, j=0, left=None,
                   middle=None, right=None, parent=None)

        # Computational Budget

        begin = datetime.datetime.utcnow()

        while datetime.datetime.utcnow() - begin < self.calculation_time:
            v_l = self.tree_policy(v_0)
            # ask about this, i am sending the node
            delta_reward = self.rdefault_policy(v_l)
            self.back_up(v_l, delta_reward)

        v = v_0
        while True:
            if v.isLeaf() is False:
                v = self.best_child(v, 0)
            else:
                return v.s, v.Q

    def flatten_align(self, align):
        flat = []
        s1 = ''.join(align[0])
        s2 = ''.join(align[1])
        for i in range(len(s1)):
            if s1[i] != '-':
                if i == 0:
                    flat.append(s1[i])
                else:
                    flat = [''.join(flat) + s1[i]]
            elif s1[i] == '-' and s2[i] == '-':
                if i == 0:
                    flat.append(s1[i])
                else:
                    flat = [''.join(flat) + s1[i]]
            elif s1[i] == '-' and s2[i] != '-':
                if i == 0:
                    flat.append(s2[i])
                else:
                    flat = [''.join(flat) + s2[i]]
        return flat

    def update_alignment(self, multiple, s1, new_align):
        update = []
        k = 0
        s1 = ''.join(s1)
        seq = ''.join(new_align[0])

        for i in range(len(seq)):
            if k < len(s1):
                if s1[k] == seq[i]:
                    for j in range(len(multiple)):
                        prev = ''.join(multiple[j])
                        if k == 0:
                            update.append(prev[k])
                        else:
                            update[j] = [''.join(update[j]) + prev[k]]
                    k += 1
            else:
                for j in range(len(multiple)):
                    if k == 0:
                        update.append('-')
                    else:
                        update[j] = [''.join(update[j]) + '-']
        update.append(new_align[1])
        return update

    def upper_default_policy(self, s1, s2):
        i = 0
        j = 0
        n_state = [[],[]]
        rew = 0

        while i < (len(s1)) and j < (len(s2)):
            rand_act = np.random.choice(np.arange(-1, 2), p=[0.9, 0.05, 0.05])
            acted = False

            if rand_act == -1 and i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    n_state=[[''.join(n_state[0])+s1[i]],[''.join(n_state[1])+s2[j]]]
                    i += 1
                    j += 1
                    rew += self.m
                else:
                    n_state = [[''.join(n_state[0]) + s1[i]], [''.join(n_state[1]) + s2[j]]]
                    i += 1
                    j += 1
                    rew += self.w
            elif rand_act == 0 and i < len(s1):
                n_state=[[''.join(n_state[0]) + s1[i]], [''.join(n_state[1]) + '-']]
                i += 1
                rew += self.g
            elif rand_act == 1 and j < len(s2):
                n_state=[[''.join(n_state[0]) + '-'], [''.join(n_state[1]) + s2[j]]]
                j += 1
                rew += self.g

        return rew

    def random_sequence(self, items, sq1):
        sel_align = []
        sel_rew = np.infty

        minrewi = 0
        for j in range(self.multi):
            for i in range(len(items)):
                it = items[i]
                sq2 = ''.join(self.sequence[it])
                alignment, reward = self.inner_search(sq1, sq2)

                if reward < sel_rew:
                    sel_align = alignment
                    sel_rew = reward
                    minrewi = i

        return items[minrewi], sel_align, sel_rew

    def random_combination(self, items, comb):

        sel_align = []
        sel_rew = np.infty

        minrewi = 0
        for j in range(self.multi):
            for i in range(len(comb)):
                pair = comb[i]
                sq1 = ''.join(self.sequence[pair[0]])
                sq2 = ''.join(self.sequence[pair[1]])
                alignment, reward = self.inner_search(sq1, sq2)

                if reward < sel_rew:
                    sel_align = alignment
                    sel_rew = reward
                    minrewi = i


        return comb[minrewi], sel_align, sel_rew

    def best_MSA(self, multiple, order, order_id, Q):

        best = np.argmin(Q)

        return multiple[best], order[best], order_id[best]

    def upper_search(self):
        n = len(self.sequence)
        iter = 0
        all_multiple = []
        all_orders = []
        all_order_id = []
        Q = []

        #save all alignments or best, only set one true
        save_best = True

        save_all = False

        # Computational Budget

        big_begin = datetime.datetime.utcnow()

        while datetime.datetime.utcnow() - big_begin < self.big_calculation_time:
            # Start variables
            items = range(n)
            comb = list(itertools.combinations(items, 2))
            s1 = []
            s_order = []
            multiple = []
            id_in_order = []

            # levels
            for i in range(n-1):
                if i == 0:
                    # Choose the best pair of sequences to align
                    c_try, alignment, reward = self.random_combination(items, comb)
                    Q.append(reward)
                    # Flatten the alignment
                    s1 = self.flatten_align(alignment)

                    # Update the set of sequences that have not been aligned
                    items = list(set(items) - set(c_try))

                    # Add the alignments to the multiple alignment
                    multiple.append(alignment[0])
                    multiple.append(alignment[1])
                    s_order.append(c_try[0])
                    s_order.append(c_try[1])
                    id_in_order.append(self.id[c_try[0]])
                    id_in_order.append(self.id[c_try[1]])


                else:
                    # Choose the next best sequence to align
                    n_s2, alignment, reward = self.random_sequence(items, s1)
                    Q[iter] += reward
                    # Update previous alignments to the multiple alignment
                    multiple = self.update_alignment(multiple, s1, alignment)

                    # Flatten the new alignment
                    s1 = self.flatten_align(alignment)

                    # Update the number of sequences missing:
                    items = list(set(items) - set([n_s2]))
                    s_order.append(n_s2)
                    id_in_order.append(self.id[n_s2])

            iter += 1

            all_multiple.append(multiple)
            all_orders.append(s_order)
            all_order_id.append(id_in_order)

        if save_all is True:

            return all_multiple, all_orders, all_order_id

        else:
            return self.best_MSA(all_multiple, all_orders, all_order_id, Q)