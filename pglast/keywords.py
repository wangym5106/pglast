# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from kwlist.h @ 10-1.0.2-0-gd710cb0
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *

COL_NAME_KEYWORDS = {'between', 'bigint', 'bit', 'boolean', 'char', 'character', 'coalesce',
                     'dec', 'decimal', 'exists', 'extract', 'float', 'greatest', 'grouping',
                     'inout', 'int', 'integer', 'interval', 'least', 'national', 'nchar',
                     'none', 'nullif', 'numeric', 'out', 'overlay', 'position', 'precision',
                     'real', 'row', 'setof', 'smallint', 'substring', 'time', 'timestamp',
                     'treat', 'trim', 'values', 'varchar', 'xmlattributes', 'xmlconcat',
                     'xmlelement', 'xmlexists', 'xmlforest', 'xmlnamespaces', 'xmlparse',
                     'xmlpi', 'xmlroot', 'xmlserialize', 'xmltable'}

RESERVED_KEYWORDS = {'all', 'analyse', 'analyze', 'and', 'any', 'array', 'as', 'asc',
                     'asymmetric', 'both', 'case', 'cast', 'check', 'collate', 'column',
                     'constraint', 'create', 'current_catalog', 'current_date', 'current_role',
                     'current_time', 'current_timestamp', 'current_user', 'default',
                     'deferrable', 'desc', 'distinct', 'do', 'else', 'end', 'except', 'false',
                     'fetch', 'for', 'foreign', 'from', 'grant', 'group', 'having', 'in',
                     'initially', 'intersect', 'into', 'lateral', 'leading', 'limit',
                     'localtime', 'localtimestamp', 'not', 'null', 'offset', 'on', 'only',
                     'or', 'order', 'placing', 'primary', 'references', 'returning', 'select',
                     'session_user', 'some', 'symmetric', 'table', 'then', 'to', 'trailing',
                     'true', 'union', 'unique', 'user', 'using', 'variadic', 'when', 'where',
                     'window', 'with'}

TYPE_FUNC_NAME_KEYWORDS = {'authorization', 'binary', 'collation', 'concurrently', 'cross',
                           'current_schema', 'freeze', 'full', 'ilike', 'inner', 'is',
                           'isnull', 'join', 'left', 'like', 'natural', 'notnull', 'outer',
                           'overlaps', 'right', 'similar', 'tablesample', 'verbose'}

UNRESERVED_KEYWORDS = {'abort', 'absolute', 'access', 'action', 'add', 'admin', 'after',
                       'aggregate', 'also', 'alter', 'always', 'assertion', 'assignment', 'at',
                       'attach', 'attribute', 'backward', 'before', 'begin', 'by', 'cache',
                       'called', 'cascade', 'cascaded', 'catalog', 'chain', 'characteristics',
                       'checkpoint', 'class', 'close', 'cluster', 'columns', 'comment',
                       'comments', 'commit', 'committed', 'configuration', 'conflict',
                       'connection', 'constraints', 'content', 'continue', 'conversion',
                       'copy', 'cost', 'csv', 'cube', 'current', 'cursor', 'cycle', 'data',
                       'database', 'day', 'deallocate', 'declare', 'defaults', 'deferred',
                       'definer', 'delete', 'delimiter', 'delimiters', 'depends', 'detach',
                       'dictionary', 'disable', 'discard', 'document', 'domain', 'double',
                       'drop', 'each', 'enable', 'encoding', 'encrypted', 'enum', 'escape',
                       'event', 'exclude', 'excluding', 'exclusive', 'execute', 'explain',
                       'extension', 'external', 'family', 'filter', 'first', 'following',
                       'force', 'forward', 'function', 'functions', 'generated', 'global',
                       'granted', 'handler', 'header', 'hold', 'hour', 'identity', 'if',
                       'immediate', 'immutable', 'implicit', 'import', 'including',
                       'increment', 'index', 'indexes', 'inherit', 'inherits', 'inline',
                       'input', 'insensitive', 'insert', 'instead', 'invoker', 'isolation',
                       'key', 'label', 'language', 'large', 'last', 'leakproof', 'level',
                       'listen', 'load', 'local', 'location', 'lock', 'locked', 'logged',
                       'mapping', 'match', 'materialized', 'maxvalue', 'method', 'minute',
                       'minvalue', 'mode', 'month', 'move', 'name', 'names', 'new', 'next',
                       'no', 'nothing', 'notify', 'nowait', 'nulls', 'object', 'of', 'off',
                       'oids', 'old', 'operator', 'option', 'options', 'ordinality', 'over',
                       'overriding', 'owned', 'owner', 'parallel', 'parser', 'partial',
                       'partition', 'passing', 'password', 'plans', 'policy', 'preceding',
                       'prepare', 'prepared', 'preserve', 'prior', 'privileges', 'procedural',
                       'procedure', 'program', 'publication', 'quote', 'range', 'read',
                       'reassign', 'recheck', 'recursive', 'ref', 'referencing', 'refresh',
                       'reindex', 'relative', 'release', 'rename', 'repeatable', 'replace',
                       'replica', 'reset', 'restart', 'restrict', 'returns', 'revoke', 'role',
                       'rollback', 'rollup', 'rows', 'rule', 'savepoint', 'schema', 'schemas',
                       'scroll', 'search', 'second', 'security', 'sequence', 'sequences',
                       'serializable', 'server', 'session', 'set', 'sets', 'share', 'show',
                       'simple', 'skip', 'snapshot', 'sql', 'stable', 'standalone', 'start',
                       'statement', 'statistics', 'stdin', 'stdout', 'storage', 'strict',
                       'strip', 'subscription', 'sysid', 'system', 'tables', 'tablespace',
                       'temp', 'template', 'temporary', 'text', 'transaction', 'transform',
                       'trigger', 'truncate', 'trusted', 'type', 'types', 'unbounded',
                       'uncommitted', 'unencrypted', 'unknown', 'unlisten', 'unlogged',
                       'until', 'update', 'vacuum', 'valid', 'validate', 'validator', 'value',
                       'varying', 'version', 'view', 'views', 'volatile', 'whitespace',
                       'within', 'without', 'work', 'wrapper', 'write', 'xml', 'year', 'yes',
                       'zone'}
