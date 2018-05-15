test = {
  'names': [
    'check_draw'
  ],
  'points': 0,
  'suites': [
    [
      {
        'never_lock': True,
        'test': r"""
        >>> all_lines = open('contest.scm', 'r').readlines()
        >>> non_blank = [s for s in all_lines if s.strip()]
        >>> last_line = non_blank[-1]
        >>> last_line.strip()
        '(draw)'
        """,
        'type': 'doctest'
      }
    ]
  ]
}