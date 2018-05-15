test = {
  'names': [
    'final'
  ],
  'points': 0,
  'suites': [
    [
      {
        'never_lock': True,
        'test': """
        >>> i, j = 0, 0
        >>> for i in range(GOAL):
        ...    for j in range(GOAL):
        ...        assert final_strategy(i, j) == final_strategy(i, j)
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'never_lock': True,
        'test': """
        >>> type(final_bid) == int
        True
        >>> final_bid >= 0
        True
        """,
        'type': 'doctest'
      }
    ]
  ]
}