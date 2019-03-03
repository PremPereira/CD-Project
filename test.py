
rules = []
non_term = []
first = {}
rules_dict = {}
follows = {}

with open("rules_test.txt", "r") as fp:
    for line in fp:
        # Splitting on newline and turning it into an array
        rules.append(line.strip().split('\n'))

#print(rules)


def non_term_appender(non_term, rules):
    for rule in rules:
        if rule[0][0] not in non_term:
            non_term.append(rule[0][0])
            follows[rule[0][0]] = []
           # first[rule[0][0]] = []


non_term_appender(non_term, rules)
#print(non_term,first)
#print(non_term)
number_of_rules = len(rules)
rule_count = first_count = 0

for nt in non_term:
    rules_dict[nt] = []
    rules_dict[nt] = rules[rule_count][0][5:]
    rule_count += 1

#print(rules_dict)

for rule in rules :
    l = str(rule[0][5:]).split()
    #print(l)
    if l[0][0].islower():
        if rule[0][0] not in first:
            first[rule[0][0]] = []

        first[rule[0][0]].append(l[0])

#print(first)

for rule in rules:
    l = str(rule[0][5:]).split()
    if l[0].isupper():
        if rule[0][0] not in first:
            first[rule[0][0]] = []

        first[rule[0][0]].extend(first[l[0]])

for s in first:
    first[s] = list(set(first[s]))

for x in first:
    print("First of %s : %s" %(x,first[x]))



def follow_calc():

    def follow_r(n_term):
        follows[n_term] = []

        if n_term == 'S':
            follows[n_term] = ['$']

        for rule in rules:
            lhs = rule[0][0]
            symbols = rule[0][5:].split()

            l = [i for i, x in enumerate(symbols) if x == n_term]
            for pos in l:
                if pos == len(symbols) - 1:
                    if lhs not in follows.keys():
                        follow_r(lhs)

                    follows[n_term].extend(follows[lhs])
                else:
                    s = symbols[pos + 1]
                    #print(s)
                    if s not in non_term:
                        f = list(s.split())
                    else:
                        f = first[s]

                    if 'epsilon' in f:
                        f.remove('epsilon')
                        follows[n_term].extend(f)
                        if lhs not in follows.keys():
                            follow_r(lhs)
                        follows[n_term].extend(follows[lhs])
                    else:
                        follows[n_term].extend(f)

        follows[n_term] = list(set(follows[n_term]))

    for n_term in non_term:
        follow_r(n_term)


follow_calc()
print("\n\n")
for x in follows:
    print("Follows of %s : %s" %(x,follows[x]))
