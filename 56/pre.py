(lambda entry: (lambda enum, synerr:
  (lambda escs, conv:
    (lambda shattered: (lambda reunited, spotter:
      (lambda endsnstarts: (lambda enscc:
        (lambda ccends, ccstarts:
          synerr("unmatched ']'")
            if -1 in ccends else
          (lambda cclass_locs: (lambda rntd_wo_cc:
            (lambda brackify, orsify, delete:
              (lambda evalify, parse, shaped:
                (lambda bracketed:
                  synerr("unmatched ')'")
                    if bracketed == -1 else
                  (lambda deleted:
                    synerr("nothing to repeat")
                      if deleted == -1 else
                    (lambda orsnevaled:
                      synerr("nothing to repeat")
                        if -1 in orsnevaled else
                      "expression cannot match anything. see about page for more info"
                        if not orsnevaled else
                      sorted(orsnevaled[::-1], key = len)[0]
                    ) ([e for e in [evalify(parse, evalify, s) for s in orsify(deleted)] if e != None])
                  ) (delete(bracketed))
                ) (brackify(shaped))
              ) (lambda parse, evalify, lost:
                  (lambda processed:
                    -1
                      if any(map(lambda E: type(E) == synerr, processed)) else
                    None
                      if None in processed else
                    ''.join(processed)
                  ) ([parse(evalify, parse, e) if type(e) == list else e for e in lost]),
                 lambda evalify, parse, shaped:
                  (lambda bracketed:
                    synerr("unmatched ')'")
                      if bracketed == -1 else
                    (lambda deleted:
                      synerr("nothing to repeat")
                        if deleted == -1 else
                      (lambda orsnevaled:
                        synerr("nothing to repeat")
                          if -1 in orsnevaled else
                        None
                          if not orsnevaled else
                        sorted(orsnevaled[::-1], key = len)[0]
                      ) ([e for e in [evalify(parse, evalify, s) for s in orsify(deleted)] if e != None])
                    ) (delete(bracketed))
                  ) (brackify(shaped)),
                 rntd_wo_cc)
            ) (lambda shaped: (lambda prnens:
                (lambda pends, parts:
                  -1
                    if -1 in pends else
                  (lambda ous, ins:
                    [c for i, (s, e) in enum(ins) for c in shaped[ous[i][1] + 1:ous[i][0]] + [shaped[s + 1:e]]] + shaped[ous[-1][1] + 1:ous[-1][0]]
                  ) ((list(zip(parts + [len(shaped)], [-1] + pends))),
                     (zip(parts, pends)))
                ) (prnens[0], prnens[1])
              ) (endsnstarts(shaped, '(', ')')),
               lambda shaped: (lambda orspot:
                [shaped[e + 1:s] for s, e in zip(orspot + [len(shaped)], [-1] + orspot)]
              ) (spotter(shaped, "or")),
               lambda shaped: (lambda gzspot:
                (lambda gz_locs:
                  -1
                    if -1 in gz_locs else
                  ([c for i, c in enum(shaped) if not i in gz_locs and not i + 1 in gz_locs])
                ) ([-1 if shaped[e - 1] in ["or", "gz"] or not e else e for e in gzspot])
              ) (spotter(shaped, "gz")))
          ) ([c for s, e in list(cclass_locs) for c in reunited[e + 1:s] + [None]][:-1])
          ) (zip(ccstarts + [len(reunited)], [-1] + ccends))
        ) (enscc[0], enscc[1])
      ) (endsnstarts(reunited, '[', ']'))
      ) (lambda shaped, n, f:
          (lambda openes, closes:
            ([c for c in [(lambda num_opens: -1 if num_opens < i else None if num_opens > i else D) (len([x for x in openes if x < D]) - 1) for i, D in enum(closes)] if c != None],
             [D for i, D in enum(openes) if len([x for x in closes if x < D]) == i])
          ) (spotter(shaped, conv([n])[0]),
             spotter(shaped, conv([f])[0])))
    ) ([c for i, s in enum(shattered) for c in conv(s) + [entry[escs[i] + 1]]][:-1],
       lambda s, t: [i for i, c in enum(s) if c == t])
    ) ([entry[escs[i - 1] + 2:D] for i, D in enum(escs)])
  ) ([i for i, c in enum(entry)
      if c == '\\'
      and (lambda s: len(s
       .split(
         [c for c in s[::-1].split(s[-1]) if c][0][0]
       )[-1]) % 2) (entry[:i + 1])] + [-2],
     lambda s: [{
       '(':"bn",
       ')':"bf",
       '[':"ki",
       ']':"ck",
       '|':"or",
       '*':"gz",
     }.get(c, c) for c in s])
) (enumerate, SyntaxError)) (input() + '69')
