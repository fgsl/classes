(screen:clear-window (screen:make-window))
(format t "Olá, eu sou Alfredo, em que posso ajudar? ~%" nil) 
(setq resposta (read))
(format t "~%Você disse:~S~%" resposta)
(loop
    (format t "Posso ajudar em mais alguma coisa? ~%" nil)
    (setq resposta (string-downcase(read)))
(when (string= resposta "não")(return 'fim)))
(format t "~%Obrigado e até logo~%" nil nil)
