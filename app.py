# # def isPalindrome(str):
# #     for i, letter in enumerate(str, 1):
# #         if letter == str[-i]:
# #             continue
# #         else:
# #             return False
# #     return True

# # print(isPalindrome("trueitrue"))

# # def isPalindrome(str):
# #     occur = {}
# #     for letter in str:
# #         if letter in occur:
# #             occur[letter] += 1
# #         else:
# #             occur[letter] = 1

# #         # if char == str[-i]:
# #         #     continue
# #         # else:
# #         #     return False

# #     odd_letter_count = 0
# #     for letter in occur.values():
# #         if letter % 2 != 0:
# #             odd_letter_count += 1

# #     return odd_letter_count <= 1
# # def order(a):
# #     for x in a:
# #         if x > a[-1]:
# #             return "descending"
# #         elif x < a[-1]:
# #             return "ascending"
# #         else:
# #             return "not sorted"


# # print(order([1, 7, 12]))

# # def max_non_decreasing_subarray(a):
# #     max_length = 1
# #     current_length = 1
# #     for i in range(1, len(a)):
# #         if a[i] >= a[i-1]:
# #             current_length += 1
# #         else:
# #             current_length = 1

# #         if current_length > max_length:
# #             max_length = current_length
# #     return max_length

# # print(max_non_decreasing_subarray([1, 2, 3, 1, 1, 5, 2, 1, 2, 3, 4]))


# # def filter_bible(scripts, book_id, chapter_id):
# #     founded_scripts = []
# #     for script in scripts:
# #         if script[:2] == book_id:
# #             if script[2:5] == chapter_id:
# #                 founded_scripts.append(script)
# #     return founded_scripts

# # # test = "01001001"
# # # print(test[2:4])


# # scripts = ["01001001", "01001002", "01002001", "01002002",
# #            "01002003", "02001001", "02001002", "02001003"]
# # print(filter_bible(scripts, "01", "001"))


# # def toPostFixExpression(expression):
# # operators = {
# #     '%': 4,
# #     '/': 3,
# #     '*': 2,
# #     '+': 1,
# #     '-': 0,
# # }
# # result = []
# # found_operators = []
# # for element in expression:
# #     if element == '(' or element == ')':
# #         pass
# #     elif element not in operators:
# #         result.append(element)
# #     else:
# #         found_operators.append(element)
# #         size = len(found_operators)
# #         if len(found_operators) > 1:
# #             if operators[found_operators[-1]] >= operators[found_operators[0]]:
# #                 found_operators.pop()
# #                 found_operators.insert(0, element)

# # return result + found_operators


# # def exp_to_postfix(expression):
# #     operators = {
# #         '%': 4,
# #         '/': 3,
# #         '*': 2,
# #         '+': 1,
# #         '-': 0,
# #     }
# #     result = []
# #     found_operators = []
# #     # stack = []

# #     for element in expression:

# #         if element not in operators and element != '(' and element != ')':
# #             result.append(element)

# #         elif element in operators:
# #             while found_operators and found_operators[-1] != '(' and operators[found_operators[-1]] >= operators[element]:
# #                 result.append(found_operators.pop())
# #             found_operators.append(element)

# #         elif element == '(':
# #             found_operators.append(element)

# #         elif element == ')':
# #             while found_operators[-1] != '(':
# #                 result.append(found_operators.pop())
# #             found_operators.pop()

# #     while found_operators:
# #         result.append(found_operators.pop())

# #     return result


# # print(exp_to_postfix(["20",
# #                       "+",
# #                       "3",
# #                       "*",
# #                       "(",
# #                       "5",
# #                       "*",
# #                       "4",
# #                       ")"]))
# # expression = ["2", "+", "3", '-', '(', '2', '*', '2', ')', '%', '+']
# # print(exp_to_postfix(expression))
# # print(exp_to_postfix(["(", "(", "(", "1", "+", "2", ")", "*",
# #       "3", ")", "+", "6", ")", "/", "(", "2", "+", "3", ")"]))


# # def Cipher_Zeroes(N):
# #     visible_zeros = {"0": 1, "6": 1, "8": 2, "9": 1}
# #     amount_of_nulls = 0

# #     for num in N:
# #         if num in visible_zeros:
# #             amount_of_nulls += visible_zeros[num]

# #     if (amount_of_nulls % 2) == 0 and amount_of_nulls > 0:
# #         amount_of_nulls -= 1
# #     elif (amount_of_nulls % 2) != 0 and amount_of_nulls > 0:
# #         amount_of_nulls += 1
# #     else:
# #         pass

# #     if amount_of_nulls > 0:
# #         amount_of_nulls += 1 - amount_of_nulls % 2
# #     return format(amount_of_nulls, 'b')

# # def Cipher_Zeroes(N):
# #     visible_zeros = {"0": 1, "6": 1, "8": 2, "9": 1}
# #     amount_of_nulls = sum([visible_zeros.get(num, 0) for num in N])

# #     if amount_of_nulls > 0:
# #         amount_of_nulls += 1 - amount_of_nulls % 2

# #     return format(amount_of_nulls, 'b')


# # print(Cipher_Zeroes("4900"))

# # def generate_powers_of_n(n, k):
# #     powers = [n**i for i in range(k) if n**i <= k]
# #     return powers


# # def gen_n_pow(n, k):
# #     powers = [1]
# #     power = n
# #     while power <= k:
# #         powers.append(power)
# #         power *= n
# #     return powers


# # def kthTerm(n, k):
# #     sequence = [1]
# #     powers = gen_n_pow(n, k)
# #     # print(powers)
# #     while len(sequence) < k:
# #         biggest_power = powers[-1]
# #         nums = [element + biggest_power for element in sequence if element +
# #                 biggest_power not in sequence]
# #         # add the smallest element so I could be sure that my list will be ascending
# #         sequence.append(min(nums))
# #         powers = gen_n_pow(n, k)
# #     return sequence[k-1]


# # def kthTerm(n, k):
# #     seq = []

# #     for i in range(1, 2):
# #         seq.append(n**i)
# #         for j in seq:
# #             if len(seq) < k:
# #                 seq.append(n**i + j)
# #             else:
# #                 continue

# #     # while len(seq) < k:
# #     return seq

# # def kthTerm(n: int, k: int) -> int:
# #     values = []
# #     for i in range(k):
# #         values.append(n ** i)
# #         for j in values[:-1]:
# #             if len(values) >= k:
# #                 return values[k - 1]
# #             values.append((n ** i) + j)
# #     return values[k - 1]

# # # print(results)
# # # 1 2 3

# # print(kthTerm(2, 4))


# # for element in q:
# #     # print(f"q: numb: {element} in P placed at: {p.index(element)}")
# #     p_indxs.append(p.index(element))
# # p.index(element)

# # for element in p:
# #     # print(f"p: numb: {element} in Q placed at: {q.index(element)}")
# #     q_indxs.append(q.index(element))

# # print(p)
# # print(p_indxs)


# from copy import deepcopy
# import copy
# import rstr
# import random
# import re
# from math import sqrt
# import math


# def double_string(data):
#     my_value_set = set(data)
#     count = 0
#     for i in data:
#         for si in my_value_set:
#             if i + si in data:
#                 count += 1
#                 break
#     return count

#     my_value_set = set(data)
#     return sum(1 for i in data for si in my_value_set if i + si in data)


# data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
# data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
# # print(double_string(data))
# # print(double_string(data))
# # print(len([i for i in data if any(i + i == c for c in data)]))
# # def double_string(data):
# #     count = 0
# #     for s in data:
# #         for i in range(len(data)):
# #             if i == data.index(s):
# #                 continue
# #             if s == data[i] + data[i] or s == data[i]*2:
# #                 count += 1
# #                 break
# #     return count

# data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
# # data = ['aaaa', 'aaaaaaaa', 'aaaa', 'qwer']
# # print(double_string(data))


# # def morse_number(num):
# #     morse_dict = {
# #         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
# #         '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
# #     }

# #     # Convert the input number to a string and pad it with zeros to ensure it has three digits
# #     num_str = str(num).zfill(3)

# #     # Encrypt each digit separately and concatenate the results
# #     encrypted = ''
# #     for digit in num_str:
# #         if digit == '0':
# #             encrypted += morse_dict[digit] + ' '
# #         elif digit in '12345':
# #             encrypted += morse_dict[digit] + ' '
# #         else:
# #             morse_digit = morse_dict[str(
# #                 int(digit) - 5)].replace('.', 'X').replace('-', '.').replace('X', '-')
# #             encrypted += morse_digit + ' '

# #     return encrypted.strip()


# # print(morse_number("18062002"))


# # def max_population(data):
# #     max_pop = 0
# #     max_loc = ""
# #     for line in data:
# #         # Use regular expression to extract population and name
# #         match = re.match(r'^\d+,[a-z_]+,(\d+),[yn]$', line)
# #         if match:
# #             pop = int(match.group(1))
# #             if pop > max_pop:
# #                 max_pop = pop
# #                 max_loc = line.split(',')[1]
# #     return max_loc, max_pop

# def max_population(data):
#     max_pop = 0
#     max_loc = ""
#     for line in data:
#         match = re.match(r'^\d+,[a-z_]+,(\d+),[yn]$', line)
#         if match and int(match.group(1)) > max_pop:
#             max_pop = int(match.group(1))
#             max_loc = line.split(',')[1]
#     return max_loc, max_pop


# data = ["id,name,poppulation,is_capital",
#         "3024,eu_kyiv,24834,y",
#         "3025,eu_volynia,20231,n",
#         "3026,eu_galych,23745,n",
#         "4892,me_medina,18038,n",
#         "4401,af_cairo,18946,y",
#         "4700,me_tabriz,13421,n",
#         "4899,me_bagdad,22723,y",
#         "6600,af_zulu,09720,n"]

# # print(max_population(data))


# def figure_perimeter(s):
#     lb_x, lb_y = map(int, s[s.index('LB')+2:s.index('#RB')].split(':'))
#     rb_x, rb_y = map(int, s[s.index('RB')+2:s.index('#LT')].split(':'))
#     lt_x, lt_y = map(int, s[s.index('LT')+2:s.index('#RT')].split(':'))
#     rt_x, rt_y = map(int, s[s.index('RT')+2:].split(':'))

#     s1 = sqrt((lb_x - rb_x)**2 + (lb_y - rb_y)**2)
#     s2 = sqrt((rb_x - rt_x)**2 + (rb_y - rt_y)**2)
#     s3 = sqrt((rt_x - lt_x)**2 + (rt_y - lt_y)**2)
#     s4 = sqrt((lt_x - lb_x)**2 + (lt_y - lb_y)**2)

#     return s1 + s2 + s3 + s4


# test1 = "#LB0:1#RB5:1#LT4:5#RT8:3"
# # print(figure_perimeter(test1))


# def morse_number(nums):
#     output = ''
#     for n in nums:
#         n = int(n)
#         r = n - 5

#         if n > 5:
#             for dashtrack in range(r):
#                 output += '-'
#                 n -= 1

#                 if n < 6:
#                     for dotdtrack in range(n-r):
#                         output += '.'

#         elif n < 6:

#             for dotdtrack in range(n):
#                 output += '.'

#             while n < 5:
#                 output += '-'
#                 n += 1

#         output += ' '
#     return output


# # print(morse_number("18062002"))
# def generate_key(pattern):
#     key_pattern = '[0-9]{4}-[0-9]{2}[A-Z]{3}-[A-Z]{5}-[0-9]{2}[A-Z]{2}[A-Z]{1}-[A-Z]{3}[0-9]{2}-[0-9]{2}[A-Z]{3}'
#     key_year = '2023'
#     result = rstr.xeger(pattern)
#     return result.replace(result[0:4], key_year)


# # def pretty_message(string):
# #     return re.sub(r'([a-z]+?)\1+', r'\1', string)

#     # result = re.sub(rep_chars, r'\1', data)
#     # return data


# data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
# # print(pretty_message(data))


# # print(kth_term(30, 100))

# # pretty_message(data)


# # def pretty_message(data: str):
# #     pattern = r'([a-z]*?)\1+'
# #     txt = re.sub(pattern, r'\1', data)
# #     return txt


# # print(pretty_message(data))


# # def outer(name):
# #     def inner():
# #         return f"Hello, {name}!"
# #     return inner


# # alice = outer("Alice")
# # print(alice())


# # def create(pass_for_Tom):
# #     return lambda x: pass_for_Tom == x


# # tom = create("pass_for_Tom")
# # print(tom("pass_for_Tom"))

# # def divisor(num):
# #     div = 1
# #     while div <= num:
# #         if num % div == 0:
# #             yield div
# #         div += 1
# #     while True:
# #         yield None


# # two = divisor(2)
# # print(next(two))
# # print(next(two))
# # print(next(two))
# # print(next(two))
# # two = divisor(3)
# # print(next(two))
# # print(next(two))


# # type your code here
# def parse_args_kwargs(args, kwargs):
#     _args = [str(arg) + ', ' if args.index(arg) >
#              len(args) else str(arg) for arg in args]

#     _kwargs = [str(arg[1]) + ', ' if arg.index(arg[1]) >
#                len(kwargs.items()) else str(arg[1]) for arg in kwargs.items()]

#     return _args + _kwargs


# def logger(func):
#     def inner(*args, **kwargs):
#         values = parse_args_kwargs(args, kwargs)
#         template = ', '.join([i for i in values])
#         returned_value = func(*args, **kwargs)
#         print(
#             f'Executing of function {func.__name__} with arguments ' + template + '...')
#         return returned_value
#     return inner


# @logger
# def concat(*args, **kwargs):
#     return ''.join(map(str, parse_args_kwargs(args, kwargs)))


# @ logger
# def sum(a, b):
#     return a+b


# @ logger
# def print_arg(arg):
#     print(arg)


# # print(concat(2, 6, 2, 2, 3))
# # concat('first string', second=2, third='second string')
# # concat('first string', second=2, third='second string')
# # print(concat(1))
# # print(concat('first string', second=2, third='second string'))
# # print_arg(2)
# # sargs = []
# # for arg in args:
# #     if args.index(arg) > len(args):
# #         sargs.append(str(arg) + ', ')
# #     else:
# #         sargs.append(str(arg))

# # _args = [str(arg) + ', ' if args.index(arg) >
# #          len(args) else str(arg) for arg in args]

# # _kwargs = [str(arg[1]) + ', ' if arg.index(arg[1]) >
# #            len(kwargs.items()) else str(arg[1]) for arg in kwargs.items()]
# # result = _args + _kwargs
# # kar = []
# # for arg in kwargs.items():
# #     if arg.index(arg[1]) > len(kwargs.items()):
# #         kar.append(str(arg[1]) + ', ')
# #     else:
# #         kar.append(str(arg[1]))

# # kwvalue = []
# # for v in kwargs.items():
# #     s = kwargs.pop(v)
# #     print(s)
# #     # if v.index(v[1]) < len(kwargs.items()):


# # def randomWord(seq):
# #     edited_seq = list(seq)

# #     while True:
# #         try:
# #             rand_word = random.choice(edited_seq)
# #             yield edited_seq[edited_seq.index(rand_word)]
# #             edited_seq.pop(edited_seq.index(rand_word))

# #             if len(edited_seq) == 0:
# #                 yield None
# #                 edited_seq = list(seq)

# #         except IndexError as e:
# #             yield None
# #             edited_seq.pop(rand_word)
# #             rand_word = random.choice(edited_seq)
# #             yield edited_seq[edited_seq.index(rand_word)]
# #             edited_seq.pop(edited_seq.index(rand_word))

# #             # if rand_word == '':
# #             #     yield None
# #             #     edited_seq.pop(edited_seq.index(rand_word))
# #             # else:
# #             #     yield edited_seq[edited_seq.index(rand_word)]
# #             #     edited_seq.pop(edited_seq.index(rand_word))

# #             if len(edited_seq) == 0:
# #                 yield None
# #                 edited_seq = list(seq)

#     # while len(edited_seq) == 0:
#     #     yield None
#     #     edited_seq = seq


# # def randomWord(seq):
# #     edited_seq = list(seq)

# #     while True:
# #         rand_word = random.choice(edited_seq)
# #         yield edited_seq[edited_seq.index(rand_word)]
# #         edited_seq.pop(edited_seq.index(rand_word))

# #         if len(edited_seq) == 0:
# #             edited_seq = list(seq)
# # #             yield None

# # def randomWord(words):
# #     copy_words = list(words)
# #     while True:
# #         random.shuffle(copy_words)
# #         for word in copy_words:
# #             yield word

# #         if len(copy_words) == 0:
# #             copy_words = list(words)
# #             yield None

# # el_list = ['s', 'z', '']
# # books = randomWord(el_list)

# # print(next(books))
# # print(next(books))
# # print(next(books))
# # print(next(books))
# # print(next(books))
# # print(next(books))
# # print(next(books))
# # print(next(books))


# def create_account(user_name: str, password: str, secret_words: list):
#     def password_validation(_password: str) -> bool:
#         pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{6,}$"
#         return bool(re.match(pattern, _password))

#     if not password_validation(password):
#         raise ValueError("Password doesn't meet requirements")

#     def check(c_password: str, c_secret_words: list) -> bool:
#         if not password_validation(c_password):
#             raise ValueError("Password doesn't meet requirements")
#         else:
#             copy_secret_words = list(secret_words)

#             if c_password != password:
#                 return False

#             if len(secret_words) == 0 or len(c_secret_words) == 0:
#                 return True

#             if len(c_secret_words) < len(secret_words):
#                 return False

#             attemps = 1

#             for w in c_secret_words:
#                 if w not in copy_secret_words:
#                     attemps -= 1
#                 else:
#                     copy_secret_words.pop(copy_secret_words.index(w))

#                 if attemps < 0:
#                     return False

#                 if len(copy_secret_words) != 0:
#                     continue

#         return True
#     return check


# #       "word1", "abc3", "test", 'x']))
# # ["word1", "abc3", "list"]
# # val1 = create_account(
# #     "123", "qQ1!45", ["word1", "abc3", "list", "word1", "abc3", "list", "word"])
# # print(val1("qQ1!45", ["word1", "abc3", "list",
# #       "word1", "abc3", "lisst", "worsd"]))
# # val1 = create_account("123", "qQ1!45", ["1", "word"])
# # print(val1("qQ1!45", ["1", "word"]))

# # val1 = create_account("123", "qQ1!45", ["1", "word"])
# # print(val1("qQ1!45", ["1", "word"]))

# # user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
# # print(user2("yu6r*Tt5", ["abc3", "abc3", "abc3"]))
# # tom = create_account("Tom", "Qwerty1_", ["1", "word"])
# # check1 = tom("Qwerty1_",  ["1", "word"])
# # check2 = tom("Qwerty1_",  ["word"])
# # check3 = tom("Qwerty1_",  ["word", "2"])
# # check4 = tom("Qwerty1!",  ["word", "12"])

# # val1 = create_account("123", "qQ1!45", initial_arr)
# # print(val1("qQ1!45", checked_arr_1_true))
# # # t = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{6,}$"


# # print(re.match(t, "Qwerty1_"))


# # def randomWord(words):
# #     copy_words = list(words)
# #     while True:
# #         random.shuffle(copy_words)
# #         for word in copy_words:
# #             yield word

#     # if len(copy_words) == 0:
#     #     copy_words = list(words)
#     #     yield None


# # class Employee:
# #     def __init__(self, firstname, lastname, salary):
# #         self.firstname = firstname
# #         self.lastname = lastname
# #         self.salary = salary

# #     @staticmethod
# #     def from_string(string):
# #         firstname, lastname, salary = string.split('-')
# #         new_obj = Employee(firstname, lastname, int(salary))
# #         return new_obj


# # emp1 = Employee("Mary", "Sue", 60000)
# # emp2 = Employee.from_string("John-Smith-55000")
# # # print(emp2.firstname)
# # print(isinstance(emp2.salary, int))


# # class Pizza:
# #     pizzas_created = 1

# #     def __init__(self, ingredients: list):
# #         self.order_number = Pizza.pizzas_created
# #         self.ingredients = ingredients
# #         Pizza.pizzas_created += 1

# #     def __del__(self):
# #         Pizza.pizzas_created -= 1

# #     @staticmethod
# #     def hawaiian():
# #         return Pizza(['ham', 'pineapple'])

# #     @staticmethod
# #     def meat_festival():
# #         return Pizza(['beef', 'meatball', 'bacon'])

# #     @staticmethod
# #     def garden_feast():
# #         return Pizza(["spinach", "olives", "mushroom"])


# # class Employee:
# #     def __init__(self, fullname, *args, **kwargs):
# #         self.name = fullname.split(' ')[0]
# #         self.lastname = fullname.split(' ')[1]
# #         [self.__setattr__(k, kwargs[k]) for k in kwargs.keys()]
# #         # for k in kwargs.keys():
# #         #     self.__setattr__(k, kwargs[k])


# # # john = Employee("John Doe")
# # mary = Employee("Mary Major", salary=120000)
# # richard = Employee("Richard Roe", salary=110000, height=178)
# # giancarlo = Employee("Giancarlo Rossi", salary=115000,
# #                      height=182, nationality="Italian")

# # print(giancarlo.lastname)
# # class Testpaper:
# #     def __init__(self, subject, markscheme, pass_mark):
# #         self.subject = subject
# #         self.markscheme = markscheme
# #         self.pass_mark = pass_mark


# # class Student:
# #     def __init__(self):
# #         self.tests_taken = "No tests taken"

# #     def take_test(self, paper: Testpaper, marks: list):
# #         score = 0

# #         for i in range(len(marks)):
# #             if marks[i] == paper.markscheme[i]:
# #                 score += 1

# #         percentage = (score / len(paper.markscheme)) * 100

# #         if percentage < float(paper.pass_mark[:-1]):
# #             result = "Failed!"
# #         else:
# #             result = 'Passed!'

# #         grade = f"{result} ({round(percentage)}%)"

# #         if self.tests_taken == "No tests taken":
# #             self.tests_taken = {paper.subject: grade}
# #         else:
# #             self.tests_taken = {**self.tests_taken, **{paper.subject: grade}}

# # class Gallows:
# #     def __init__(self):
# #         self.words = []
# #         self.game_over = False

# #     def restart(self):
# #         self.words = []
# #         self.game_over = False
# #         return "game restarted"

# #     def play(self, word: str):
# #         if not self.words:
# #             self.words.append(word)
# #             return self.words

# #         if word not in self.words and word[0] == self.words[-1][-1]:
# #             self.words.append(word)
# #             return self.words

# #         else:
# #             self.game_over = True
# #             return "game over"


# # my_gallows = Gallows()
# # print(my_gallows.game_over)
# # print(my_gallows.play('apple'))


# import re

# dssadasd

# def valid_email(email):
#     try:
#         # split email into user_info and domain_info
#         user_info, domain_info = email.split('@')

#         # check if user_info and domain_info are not empty
#         if not user_info or not domain_info:
#             raise ValueError

#         # check if domain_info has at least one dot
#         if '.' not in domain_info:
#             raise ValueError

#         # check if user_info and domain_info contain only valid characters
#         user_info_pattern = re.compile(
#             r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
#         if not user_info_pattern.match(email):
#             raise ValueError

#     except ValueError:
#         return "Email is not valid"
#     else:
#         return"Email is valid"


# print(valid_email("trafik@ukr.tel.com"))
# print(valid_email("trafik@ukr_tel.com"))
# print(valid_email("ownsite@our.c0m"))
# print(valid_email("tra@fik@ukr.com"))


# import logging
# import math

# logging.basicConfig(filename='app.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# sine_alpha = 0.5
# cosine_alpha = math.sqrt(3)/2

# # Log the sine and cosine values
# logging.info(f"Sine of alpha: {sine_alpha}")
# logging.info(f"Cosine of alpha: {cosine_alpha}")

# if cosine_alpha == 0:
#     # Log a warning message and notify that the tangent is not defined
#     logging.warning(
#         "The cosine of the angle alpha = 0. The tangent is not defined.")
#     logging.critical("The tangent of the angle alpha is not defined.")
# else:
#     # Calculate the tangent and log the result
#     tangent_alpha = sine_alpha / cosine_alpha
#     logging.debug(f"Tangent of alpha: {tangent_alpha}")


# sin_alpha = 0.5
# cos_alpha = math.sqrt(3) / 2

# sin_alpha = 0.5
# # cos_alpha = 'w'

# sin_alpha = 0.5
# cos_alpha = 0
# import logging

# logging.basicConfig(filename='app.log', level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')


# def average(numbers_list):
#     try:
#         if not numbers_list:
#             logging.debug("The list is empty")
#             return "The list is empty"

#     # Check if all elements in the list are numbers
#         if not all(isinstance(num, (int, float)) for num in numbers_list):
#             raise ValueError

#         mean = sum(numbers_list) / len(numbers_list)
#         logging.info(f"The arithmetic mean of the list is {mean}")
#         return mean

#     except ZeroDivisionError:
#         logging.warning("Division by zero")
#         return "Division by zero"

#     except ValueError:
#         logging.critical("Incorrect data entered")
#         return "Incorrect data entered"


# average([1, 2, 3, 4, 5])
# average([10, -20, -30])
# average([])
# average([1, 2, 3, 0, 5])
# average([1, 2, "three", 4, 5])


# def run_calc(a, b, op):
#     try:
#         if op == 0:
#             print(a + b)

#         elif op == 1:
#             print(a - b)

#         elif op == 2:
#             print(a * b)

#         elif op == 3:
#             print(a / b)

#         else:
#             print('Incorrect operation is obtained')

#     except TypeError:
#         print('TypeError')

#     except ZeroDivisionError:
#         print('Division by zero')

#     finally:
#         print('End of calculation')


# print(run_calc(1, 2, 0))
# print(run_calc(-19, "String", 3))
# run_calc(8, 2, 4)


# class MyExceptions(Exception):
#     pass


# def sum_slice_array(arr, first, second):
#     if not isinstance(arr[first - 1], int) or not isinstance(arr[second - 1], int) or first < 1 or second < 1:
#         return MyExceptions("MyExceptions")

#     else:
#         return float(arr[first - 1] + arr[second - 1])


# sum_slice_array([1, "string", 3], 1, 2)


# def day_of_week(day):
#     try:
#         day = int(day)

#         if day == 1:
#             return 'Monday'

#         elif day == 2:
#             return 'Tuesday'

#         elif day == 3:
#             return 'Wednesday'

#         elif day == 4:
#             return 'Thursday'

#         elif day == 5:
#             return 'Friday'

#         elif day == 6:
#             return 'Saturday'

#         elif day == 7:
#             return 'Sunday'

#         else:
#             return 'There is no such day of the week! Please try again.'

#     except ValueError:
#         return "You did not enter a number! Please try again."


# day_of_week('0')

# class ToSmallNumberGroupError(Exception):
#     pass


# def check_number_group(number):
#     try:
#         if int(number) < 10:
#             return ToSmallNumberGroupError(
#                 "We obtain error:Number of your group can't be less than 10")

#         return f"Number of your group {int(number)} is valid"

# #     except ValueError:
# #         return "You entered incorrect data. Please try again."

# import re


# def valid_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     if re.match(pattern, email):
#         return 'Email is valid'
#     return Exception('Email is not valid')


# import re


# def valid_email(email):
#     try:
#         user_info, domain_info = email.split('@')
#     except ValueError:
#         return 'Email is not valid'
#     if not user_info or not domain_info:
#         return 'Email is not valid'
#     if not re.match(r'^[\w.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
#         return 'Email is not valid'
#     return 'Email is valid'


# print(valid_email("trafik@ukr.tel.com"))

# import cmath


# def solve_quadric_equation(a, b, c):
#     try:
#         d = (b**2) - (4*a*c)
#         x1 = (-b-cmath.sqrt(d))/(2*a)
#         x2 = (-b+cmath.sqrt(d))/(2*a)
#         return f"The solution are x1={x1} and x2={x2}"

#     except TypeError:
#         return "Could not convert string to float"

#     except ZeroDivisionError:
#         return "Zero Division Error"


# print(solve_quadric_equation(1, 5, 6))

# import logging

# logging.basicConfig(filename='app.log',
#                     level=logging.DEBUG,
#                     format='%(name)s - %(levelname)s - %(message)s', filemode='w')


# def average(numbers):

#     if not numbers:
#         logging.debug("List is empty")

#     try:
#         logging.info(f'{sum(numbers) / len(numbers)}')

#     except ValueError:
#         logging.error("Inappropriate value")

#     except ZeroDivisionError:
#         logging.warning("Division by zero")

#     except TypeError:
#         logging.critical("Incorrect data entered")


# average([1, 2, 3, 4, 5])
# average([10, -20, -30])
# average([])
# average([1, 2, 3, 0, 5])
# average([1, 2, "three", 4, 5])

# import math
# import logging

# logging.basicConfig(filename='app.log',
#                     level=logging.DEBUG,
#                     format='%(levelname)s:%(name)s:%(message)s', filemode='w')


# def findingTangent(sine_alpha, cosine_alpha):
#     logging.info(f"A value has been entered sin(alpha) = {sine_alpha}")
#     logging.info(f"A value has been entered cos(alpha) = {cosine_alpha}")

#     if cosine_alpha == 0:
#         logging.warning(
#             "The cosine of the angle alpha = 0. The tangent is not defined.")

#     else:
#         try:
#             tangent_alpha = sine_alpha / cosine_alpha
#             logging.debug(
#                 f"The value of the tangent of the angle alpha is found = {tangent_alpha}")
#         except TypeError:
#             logging.critical('The tangent of the angle alpha is not defined.')


# findingTangent(0.5, 0)
