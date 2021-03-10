# def spin_words(sentence):
#     lp = sentence.split()
#     result = []
#     for i in lp:
#         if len(lp[i]) >= 5:
#             result.append(reversed(lp[i]))
#         else:
#             result.append(lp[i])
#     return join(result)

s = "This is a test String"
t = s.split()
print(t[0][-1::-1])