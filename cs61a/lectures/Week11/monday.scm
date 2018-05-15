; Metalinguistic Abstraction
; Define a new language that is tailored to a particular type of application or problem doman

; Raising Exceptions
; Exceptions are raised within lexical analysis, synatic analysis, eval and apply.
; An interactive interpreter prints information about each error.
; A well-designed interactive interpreter should not halt completely on an error, so that the user has an opportunity to try again in the current environment.

(* 1 2 3)
(+)
(+ 2 (/ 4 8))
(+ 2
     (/ 4 (+ 
   1 1 1 1 1 1 1 1)
) )

2
(2)
(+)
(+ 1 2 3)
(-)
(- 2)
(- 10 1 2 3)
(* 1 2 3 4)
(/)
(/ 4)
(/ 1024 2 2 2 2 2)
(? 2 3)

2.3.4  ; ValueError: invalid numeral: 2.3.4
)      ; SyntaxError: unexpected token: )
()     ; TypeErorr: () is not a number or call expression
(-)    ; TypeError
(/ 1 0)

