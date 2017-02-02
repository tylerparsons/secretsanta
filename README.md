# secretsanta

Algorithm to generate a random directed secret santa
matching of members of an extended family given the
following constraints:

  * The extended family consists of the immediate
    families of a single group of siblings, who
    may be married with children.
  * Immediate families are identified by the sibling
    connecting them to the extended family.
  * No matching can contain two members from the same
    immediate family.
  * No matching can contain two members who have been
    matched in previous years.

The algorithm performs a random shuffling of two lists
of eligible family members. It then attempts to join
the two lists subject to the constraints and match all
members in O(N) time. If no match is found with the
given shuffled lists, the shuffling is reattempted.

When the number of previous years Y is small compared to
the total number of family members N, the algorithm runs
in optimal O(N) ammortized time. However, this solution
is not appropriate when Y ~ N as the runtime is unbounded.

Each randomly generated connection is assigned a weight
based on the number of shared connections between different
immediate families. In the case of Y ~ N, a solution giving
a minimum or approximate minimum of these weights would be
more suitable.

## input

* `families.csv` - families of members in the form `member,family`
* `oldConns.csv` - prior connections in the form `giver,receiver,year`

## output

* `newConns.csv` - new connections in the form `giver,receiver,year,weight`

## execution

```bash
touch families.csv oldConns.csv
./ss
```


