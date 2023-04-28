
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
def solution(survey, choices):
    dict = {}
    character = ["R","T","C","F","J","M","A","N"]
    for i in character :
        dict[i] = 0 


    for i in range(len(survey)) :
        a,b = survey[i][0],survey[i][1]
        cnt = 0
        if choices[i] ==4 :
            pass
        elif choices[i] <= 3 :
            dict[a] += 4-choices[i]
        elif choices[i] > 4 :
            dict[b] += choices[i]-4

    print(dict)
    sol = []
    if dict["R"] > dict["T"] :
        sol.append("R")
    elif dict["R"] < dict["T"] :
        sol.append("T")
    else :
        sol.append("R") 

    if dict["C"] > dict["F"] :
        sol.append("C")
    elif dict["C"] < dict["F"] :
        sol.append("F")
    else :
        sol.append("C") 

    if dict["J"] > dict["M"] :
        sol.append("J")
    elif dict["J"] < dict["M"] :
        sol.append("M")
    else :
        sol.append("J") 

    if dict["A"] > dict["N"] :
        sol.append("A")
    elif dict["A"] < dict["N"] :
        sol.append("N")
    else :
        sol.append("A") 



    solutewer = "".join(sol)

    return solutewer

surveys = ["TR", "RT", "TR"]
choices = [7, 1, 3]

solution(surveys,choices)