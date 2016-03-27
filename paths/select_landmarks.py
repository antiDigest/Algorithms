#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Algorithm 4 Select-Landmarks
    Require: Graph G = (V, E), number of landmarks k, sample size M.

    1: function Highest-Degree
    2:  For each v ∈ V let d[v] ← Degree(v).
    3:   Sort V by d[v].
    4:   Let v(i) denote the vertex with i-th largest d[v].
    5:   return {v(1), v(2), . . . , v(k)}
    6: end function

    7: function Best-Coverage
    8:  P ← ∅
    9:  for i ∈ {1, . . . , M} do
    10:   (si, ti) ← Random pair of vertices
    11:   pi ← ShortestPath(si, ti)
    12:   P ← P ∪ {pi}
    13:  end for
    14:  VP ← ∪p∈P p
    15:  for i ∈ {1, . . . , k} do
    16:   For each v ∈ VP let c[v] ← |{p ∈ P : v ∈ p}|
    17:    ui ← argmaxv∈VP
    18:    P ← P \ {ui}
    19:   end for
    20:  return {u1, . . . , uk}
    21: end function
"""

from extras import *
import numpy as np
from init import *
import time
import operator
from collections import Counter
from SPT import *

# Unused code


def highest_degree(fil):
    print "Finding degrees for all..."
    start = time.time()
    nodes = np.unique(fil.values)

    degrees = np.zeros((nodes.shape[0]))
    degrees = zip(nodes, degrees)
    degrees = dict(degrees)

    for node in nodes:
        indexes = fil[fil['from'] == node].index.tolist()
        degrees[node] = sum([fil['weight'][index:index + 1].values
                             for index in indexes])

    degrees = sorted(degrees.items(), key=operator.itemgetter(1), reverse=True)

    end = time.time()
    print "Degrees calculated in", end - start
    return degrees


def best_coverage(M, k, G, fil):

    # e = zip(fil['from'], fil['to'])
    # nodes = np.unique(e)

    # P = []

    # print "Randomizing ..."
    # for i in xrange(M):
    #     s, t = randm(nodes)
    #     d, p = shortest_path(s, G)
    #     P += [p[t]]

    # paths = P
    # print "Collecting landmarks ..."
    # U = []
    # for path in paths:
    #     Vp = []
    #     if P:
    #         for i in P:
    #             Vp += i
    #         del P[0]

    #         Vp = sorted(Counter(Vp).items(),
    #                     key=operator.itemgetter(1), reverse=True)
    #         V = [(v) for v in Vp if v[1] > 2 and v[0] in path]

    #         U += [(V[0])]

    # l = []
    # d = {}
    # for i in U:
    #     if i[0] in l:
    #         d[i[0]] = d[i[0]] + i[1]
    #     else:
    #         d[i[0]] = i[1]
    #         l += [i[0]]

    # d = sorted(d.items(),key=operator.itemgetter(1), reverse=True)
    # U = [v[0] for v in d]

    # U = list(set(U[:k]))

    # U = ['U']
    U = ['G','H']

    print "Collecting all path trees ..."
    Udict = {}
    for u in U:
        Udict[u] = path_tree(u, G)

    return U, Udict
