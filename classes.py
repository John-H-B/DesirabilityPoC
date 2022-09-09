from functions import *
import matplotlib.pyplot as plt
import numpy as np
import ast

class BIB:
    def __init__(self, parameters=None):
        self.type = 'b'
        if parameters is None:
            self.query_for_parameters()
        else:
            assert len(parameters) == 4
            name, m0, m1, m = parameters
            self.name = str(name)
            self.min = float(m0)
            self.max = float(m1)
            assert self.min < self.max
            self.m = float(m)
            self.mid_val = get_bib_mid(self.min, self.max, self.m)
            assert self.mid_val <= self.max
            assert self.mid_val >= self.min
        self.best_val = self.max # only used for building combined utility
        self.worst_val = self.min  # only used for building combined utility



    def query_for_parameters(self):
        print('What is the name of this value of interest?\n')
        self.name = str(input())
        print(f'What is the minimum acceptable value for {self.name}?\n')
        self.min = float(input())
        print(f'For what value of {self.name} would an increase no longer be more desirable? Alternatively,'
              f' what is the maximum possible value for {self.name}\n?')
        self.max = float(input())
        assert self.min < self.max
        print(f'What value of {self.name} would be considered 50% desirable. '
              f'This must be between {self.min} and {self.max}')
        self.mid_val  = float(input())
        assert self.mid_val <= self.max
        assert self.mid_val >= self.min
        self.m = get_bib_m(self.min, self.mid_val, self.max)

    def get_desirability(self, values):
        values = np.asarray(values, dtype='float64').reshape(-1)
        return bigger_is_better(values, self.min, self.max, self.m)

    def get_parameters(self):
        return [self.type, [self.name, self.min, self.max, self.m]]

    def plot(self):
        _x = np.linspace(self.min - 0.5 * (self.max - self.min), self.max + 0.5 * (self.max - self.min), 101)
        _y = self.get_desirability(_x)
        plt.plot(_x, _y)
        plt.xlabel(self.name)
        plt.show()

class SIB:
    def __init__(self, parameters=None):
        self.type = 's'
        if parameters is None:
            self.query_for_parameters()
        else:
            assert len(parameters) == 4
            name, m0, m1, t = parameters
            self.name = str(name)
            self.min = float(m0)
            self.max = float(m1)
            assert self.min < self.max
            self.t = float(t)
            self.mid_val = get_sib_mid(self.min, self.max, self.t)
            assert self.mid_val <= self.max
            assert self.mid_val >= self.min
        self.best_val = self.min  # only used for building combined utility
        self.worst_val = self.max  # only used for building combined utility

    def query_for_parameters(self):
        print('What is the name of this value of interest?\n')
        self.name = str(input())
        print(f'For what value of {self.name} would an decrease no longer be more desirable? Alternatively,'
              f' what is the minimum possible value for {self.name}\n?')
        self.min = float(input())
        print(f'What is the maximum acceptable value for {self.name}?\n')
        self.max = float(input())
        assert self.min < self.max
        print(f'What value of {self.name} would be considered 50% desirable. '
              f'This must be between {self.min} and {self.max}')
        self.mid_val  = float(input())
        assert self.mid_val <= self.max
        assert self.mid_val >= self.min

        self.t= get_sib_t(self.min, self.mid_val, self.max)

    def get_desirability(self, values):
        values = np.asarray(values, dtype='float64').reshape(-1)
        return smaller_is_better(values, self.min, self.max, self.t)

    def get_parameters(self):
        return [self.type, [self.name, self.min, self.max, self.t]]

    def plot(self):
        _x = np.linspace(self.min - 0.5 * (self.max - self.min), self.max + 0.5 * (self.max - self.min), 101)
        _y = self.get_desirability(_x)
        plt.plot(_x, _y)
        plt.xlabel(self.name)
        plt.show()

class TIB:
    def __init__(self, parameters=None):
        self.type = 't'
        if parameters is None:
            self.query_for_parameters()
        else:
            assert len(parameters) == 6
            name, m0, target, m1, m,t = parameters
            self.name = str(name)
            self.min = float(m0)
            self.target = float(target)
            self.max = float(m1)
            assert self.min < self.target
            assert self.target < self.max
            self.m = float(m)
            self.mid_val_low = get_bib_mid(self.min, self.target, self.m)
            self.t = float(t)
            self.mid_val_high = get_sib_mid(self.target, self.max, self.t)

            assert self.mid_val_high <= self.max
            assert self.mid_val_high >= self.target
            assert self.mid_val_low <= self.target
            assert self.mid_val_low >= self.min
        self.mid_val = self.mid_val_low  # only used for building combined utility
        self.best_val = self.target  # only used for building combined utility
        self.worst_val = self.min  # only used for building combined utility


    def query_for_parameters(self):
        print('What is the name of this value of interest?\n')
        self.name = str(input())
        print(f'What is the minimum acceptable value for {self.name}?\n')
        self.min = float(input())
        print(f'What is the target value for {self.name}?\n')
        self.target = float(input())
        print(f'What is the maximum acceptable value for {self.name}?\n')
        self.max = float(input())
        assert self.min < self.target
        assert self.target < self.max
        print(f'What value of {self.name} between {self.min} and {self.target} '
              f'would be considered 50% desirable.')
        self.mid_val_low = float(input())
        assert self.mid_val_low < self.target
        assert self.mid_val_low > self.min
        self.m = get_bib_m(self.min, self.mid_val_low, self.target)
        print(f'What value of {self.name} between {self.target} and {self.max} '
              f'would be considered 50% desirable.')
        self.mid_val_high = float(input())
        assert self.mid_val_high < self.max
        assert self.mid_val_high > self.target
        self.t = get_sib_t(self.target, self.mid_val_high, self.max)



    def get_desirability(self, values):
        values = np.asarray(values, dtype='float64').reshape(-1)
        return target(values,self.min, self.max, self.target, self.m, self.t)

    def get_parameters(self):
        return [self.type, [self.name, self.min, self.target, self.max, self.m, self.t]]

    def plot(self):
        _x = np.linspace(self.min - 0.5 * (self.max - self.min), self.max + 0.5 * (self.max - self.min), 101)
        _y = self.get_desirability(_x)
        plt.plot(_x, _y)
        plt.xlabel(self.name)
        plt.show()

class Combined_Desirability:
    def __init__(self):

        self.desirability_functions = []
        getting_input = True
        while getting_input:
            request = input(f'Do you have a save_string to for quick setup? Type Y/N')
            if (request == 'N') or (request == 'n'):
                self.verbose_setup()
                print(f'save_string: {self.get_quick_setup()} ')
                getting_input = False
            if (request == 'Y') or (request == 'y'):
                quick_setup = input('Please paste the save_string')

                invididual_desirability_functions, self.weights = ast.literal_eval(quick_setup)
                assert len(invididual_desirability_functions) == len(self.weights)
                for invididual_desirability_function in invididual_desirability_functions:
                    request, parameters = invididual_desirability_function
                    if request == 'b':
                        self.desirability_functions.append(BIB(parameters))
                    elif request == 's':
                        self.desirability_functions.append(SIB(parameters))
                    elif request == 't':
                        self.desirability_functions.append(TIB(parameters))
                    else:
                        print('Unknown type of desirability function')
                        assert False
                getting_input = False
            else:
                print('I am sorry, I do not know that one!')

    def verbose_setup(self):
        more = True
        print(f' \n\n\n\nHello, welcome to the setup for this desirability function. \n'
              f'You can set up as many sub-objective functions as you would like.\n'
              f'As a suggestion if you are considering multiple objectives; you should first do the objective that will be most easy to consider trading-off \n  against other objectives. \n '
              f'You will be ask to type b, s, t, or end. \n '
              f'b is for objectives where bigger is better \n '
              f's is for objectives where smaller is better \n '
              f't is for objectives where there is a target value and range of values that are better \n'
              f'end should only be typed when all objectives are set up \n'
              f'Please use a unique and memorable name without special characters for each objective')
        while more:
            request = input(f'Type b,s,t, or end')
            if request == 'end':
                more = False
            elif request == 'b':
                self.desirability_functions.append(BIB())
            elif request == 's':
                self.desirability_functions.append(SIB())
            elif request == 't':
                self.desirability_functions.append(TIB())
            else:
                print('I am sorry, I do not know that one!')

        self.weights = [1.0]
        root = self.desirability_functions[0]
        for idx in range(1, len(self.desirability_functions)):
            current = self.desirability_functions[idx]
            value = float(input(f'\nwhat {root.name} VALUE would be needed for you to consider \n'
                                f'{current.name} = {current.mid_val},{root.name}={root.mid_val} to be equivalent to \n'
                                f'{current.name} = {current.best_val},{root.name}=VALUE '
                                f'(This must be between {root.worst_val} and {root.mid_val}\n'))
            value = root.get_desirability(np.asarray([value]))[0]
            assert value < 0.5
            assert value > 0
            self.weights.append(-np.log2(2 * value))
            print(self.weights)

    def get_desirability(self, values):
        values = np.asarray(values, dtype='float64').reshape(-1,len(self.desirability_functions))
        ds = np.zeros_like(values)
        Ds = np.zeros((np.shape(values)[0],1))
        for col in range(values.shape[1]):
            ds[:,col] = self.desirability_functions[col].get_desirability(values[:,col])
        for row in range(values.shape[0]):
            Ds[row] = np.prod(ds[row, :] ** self.weights)**(1/np.sum(self.weights))
        return Ds


    def get_quick_setup(self):
        invididual_desirability_functions = []
        for idf in self.desirability_functions:
            type, parameters = idf.get_parameters()
            invididual_desirability_functions.append([type,parameters])

        quick_setup = [
            invididual_desirability_functions,
            self.weights
        ]
        return quick_setup
