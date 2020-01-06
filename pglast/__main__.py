# -*- coding: utf-8 -*-
# :Project:   pglast -- Simple frontend to the pretty reformatter
# :Created:   dom 06 ago 2017 23:09:23 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019 Lele Gaifax
#
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *

import argparse
import json
import sys

from pglast import Error, parse_plpgsql, parse_sql, prettify, _remove_stmt_len_and_location


def workhorse(args):
    input = args.infile or sys.stdin
    with input:
        statement = input.read()

    if args.parse_tree or args.plpgsql:
        tree = parse_plpgsql(statement) if args.plpgsql else parse_sql(statement)
        if args.no_location:
            _remove_stmt_len_and_location(tree)
        output = args.outfile or sys.stdout
        with output:
            output.write(unicode(json.dumps(tree, sort_keys=True, indent=2)))
            output.write('\n')
    else:
        try:
            prettified = prettify(
                statement,
                compact_lists_margin=args.compact_lists_margin,
                split_string_literals_threshold=args.split_string_literals,
                special_functions=args.special_functions,
                comma_at_eoln=args.comma_at_eoln,
                semicolon_after_last_statement=args.semicolon_after_last_statement)
        except Error as e:
            # print()
            raise SystemExit(e)

        output = args.outfile or sys.stdout
        with output:
            output.write(prettified)
            output.write('\n')


def main(options=None):
    from argparse import ArgumentParser
    from pkg_resources import get_distribution
    from .parser import get_postgresql_version

    version = '%s, with PostgreSQL %s parser' % (
        get_distribution('pglast').version,
        '.'.join(str(p) for p in get_postgresql_version()))

    parser = ArgumentParser(description="PostgreSQL language prettifier")

    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + version,)
    parser.add_argument('-p', '--plpgsql', action='store_true', default=False,
                        help='use the plpgsql parser (and print just the resulting tree)')
    parser.add_argument('-t', '--parse-tree', action='store_true', default=False,
                        help='show just the parse tree of the statement')
    parser.add_argument('-l', '--no-location', action='store_true', default=False,
                        help='remove the location of each node from the parse tree')
    parser.add_argument('-m', '--compact-lists-margin', type=int, default=0,
                        help='use compact form for lists not exceeding the given margin')
    parser.add_argument('-s', '--split-string-literals', type=int, default=0,
                        help='split string literals longer than given value')
    parser.add_argument('-f', '--special-functions', action='store_true', default=False,
                        help='activate special functions handling')
    parser.add_argument('-c', '--comma-at-eoln', action='store_true', default=False,
                        help='use alternative style to print lists, putting the comma right'
                        ' after each item')
    parser.add_argument('-e', '--semicolon-after-last-statement', action='store_true',
                        default=False, help='end the last statement with a semicolon')
    parser.add_argument('infile', nargs='?', type=argparse.FileType(),
                        help='a file containing the SQL statement to be pretty-printed,'
                        ' by default stdin')
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        help='where the result will be written, by default stdout')

    args = parser.parse_args(options if options is not None else sys.argv[1:])

    workhorse(args)


if __name__ == '__main__':  # pragma: no cover
    main()
