
% ----- membro/2 -----
% membro(Elemento, Lista) 

membro(Elemento, [Elemento|_]).

membro(Elemento, [_|Resto]) :- membro(Elemento, Resto).



% ----- prefixo/2 -----
% prefixo(Prefixo, Lista)

prefixo([], _).

prefixo([P|Rprefrixo], [P|Rlista]) :- prefixo(Rprefrixo, Rlista).



% ----- sufixo/2 -----
% sufixo(Sufixo, Lista)     nota- sufixo/2 = prefixo(inverter(Sufixo), inverter(Lista))

sufixo(S, S).

sufixo(S, [_|R]) :- sufixo(S, R).



% ----- sublista/2 -----
sublista([], _).

sublista([P|Rsl], [P|Rl]) :- sublista(Rsl, Rl).

sublista(Sl, [_|R]) :- sublista(Sl, R).

% Alternativa -> usar prefixo

sublista2(Sl, L) :- prefixo(Sl, L).

sublista2(Sl, [_|R]) :- sublista2(Sl, R).



% ----- junta/3 ----- APPEND
junta([], L, L).

junta([P|RL1], L2, [P|RL3]) :- junta(RL1, L2, RL3).



% ----- seguidos/3 -----

seguidos(N, N, N).

seguidos(N1, N2, [N1|[N2|_]]) :- seguidos(N1, N1, N1).

seguidos(N1, N2, [_|R]) :- seguidos(N1, N2, R).



% ----- ultimo/2 -----

ultimo(N, [N|[]]).

ultimo(N, [_|R]) :- ultimo(N, R).



% ----- inverte/2 -----

inverte(LN, LI) :- inverte(LN, [], LI).

inverte([], L, L).

inverte([P|R], Ac, LI) :- inverte(R, [P|Ac], LI).



% ----- comprimento/2 -----
% LENGHT

comprimento(L, N) :- comprimento(L, 0, N).

comprimento([], C, C).

comprimento([_|R], Ac, N) :- Ac1 is Ac + 1, comprimento(R, Ac1, N).



% ----- repetidos/2 -----

repetidos(LRep, LN) :- repetidos(LRep, LN, []).

repetidos(LR, [], LR).

repetidos(LRep, [P|R], Ac) :-
    member(P, R),
    not(member(P, Ac)), !,
    append(Ac, [P], Ac1),
    repetidos(LRep, R, Ac1).

repetidos(LRep, [_|R], Ac) :- repetidos(LRep, R, Ac).



% ----- nao_membro/2 -----

nao_membro(_, []).

nao_membro(E, [P|R]) :- E \== P, nao_membro(E, R).



% ----- insere_ordenado/3 -----

insere_ordenado(E, [], [E]). % caso terminal

insere_ordenado(E, [PL|RL], [E, PL|RL]) :- E < PL. % caso terminal

insere_ordenado(E, [PL|RL], [PL|R]) :- E >= PL, insere_ordenado(E, RL, R).



% -----agrupa/3 -----

%       ?- agrupa( [1,2,3], [3,2,1], L ).
%       L = [ [1,3], [2,2], [3,1] ].

agrupa_recursive([],[],[]).

agrupa_recursive([P1|R1], [P2|R2], [[P1, P2]|R3]) :-
    P1 =< P2,
    agrupa_recursive(R1, R2, R3).

agrupa_recursive([P1|R1], [P2|R2], [[P2,P1]|R3]) :-
    P1 > P2,
    agrupa_recursive(R1, R2, R3).

% ----- -----

agrupa_iterative(L1, L2, L) :- agrupa_iterative(L1, L2, L, []).

agrupa_iterative([], [], L, L).

agrupa_iterative([P1|R1], [P2|R2], L, Ac) :-
    P1 =< P2,
    append(Ac, [[P1,P2]], Ac1),
    agrupa_iterative(R1, R2, L, Ac1).

agrupa_iterative([P1|R1], [P2|R2], L, Ac) :-
    P1 > P2,
    append(Ac, [[P2, P1]], Ac1),
    agrupa_iterative(R1, R2, L, Ac1).



% ----- merge/3 -----

mrg([], L, L) :- !.

mrg(L, [], L) :- !.

mrg([P1|R1], [P2|R2], [P1|R3]) :-
    P1 < P2, !,
    mrg(R1, [P2|R2], R3).

mrg([P1|R1], [P2|R2], [P1, P2|R3]) :-
    P1 =:= P2, !,
    mrg(R1, R2, R3).

mrg([P1|R1], [P2|R2], [P2|R3]) :-
    P1 > P2,
    mrg([P1|R1], R2, R3).



% insere_ordenado mas usando predicados de ordem superior

i_o(E, L1, L2) :- 
    findall(Nums, (member(Nums, L1), Nums < E), Menores),
    append(Menores, MaioresAux, L1),
    append([E], MaioresAux, Maiores),
    append(Menores, Maiores, L2).

junta_novo_aleatorio(L1, Linf, Lsup, L2) :-
    findall(Nums, (between(Linf, Lsup, Nums), not(member(Nums, L1))), AllRandomOptions),
    length(AllRandomOptions, Len),
    random_between(1, Len, RandomIndex),
    nth1(RandomIndex, AllRandomOptions, RandomElement),
    i_o(RandomElement, L1, L2).



% intersecao/3
int(L1, L2, I) :- 
    length(L1, Len1),
    length(L2, Len2),
    Len1 =< Len2, !,
    int(L1, L2, I, []).

int(L1, L2, I) :- 
    length(L1, Len1),
    length(L2, Len2),
    Len1 > Len2, !,
    int(L2, L1, I, []).

int([], _, I, I).

int([P|R], L2, I, Acumulador) :-
    member(P, L2), !,
    append(Acumulador, [P], AcumuladorAux),
    int(R, L2, I, AcumuladorAux).

int([P|R], L2, I, Acumulador) :-
    not(member(P, L2)), !,
    int(R, L2, I, Acumulador).


% recursivamente usando corte e negacao
int2([], _, []) :- !.

int2([P|R], L2, [P|I]) :-
    member(P, L2), !,
    int2(R, L2, I).

int2([P|R], L2, I) :-
    not(member(P, L2)), !,
    int2(R, L2, I).



% functores
/*
?- functor(maisAlto(hulk, thor), maisAlto, 2).
true.
?- arg(1, maisAlto(hulk, thor), hulk).
true.
Term =.. List
?- Termo_composto =.. [maisAlto, hulk, thor].
Termo_composto = maisAlto(hulk, thor).
?- maisAlto(hulk, thor) =.. [P|R].
P = maisAlto,
R = [hulk, thor].
*/

% substitui_f/3
substitui_f(TermoC, Novo_f, Novo_TermoC) :-
    TermoC =.. [_|Args],
    Novo_TermoC =.. [Novo_f|Args].


% substitui_arg/4  & substitui_elemento_lista/4
substitui_elemento_lista(L1, El, NovoEl, L2) :- substitui_elemento_lista(L1, El, NovoEl, L2, []).
substitui_elemento_lista([], _, _, L, L) :- !.
substitui_elemento_lista([P|R], El, NovoEl, L2, Ac) :-
    P == El, !,
    append(Ac, [NovoEl], AcAux),
    substitui_elemento_lista(R, El, NovoEl, L2, AcAux).
substitui_elemento_lista([P|R], El, NovoEl, L2, Ac) :-
    P \== El, !,
    append(Ac, [P], AcAux),
    substitui_elemento_lista(R, El, NovoEl, L2, AcAux).


substitui_arg(TermoC, Arg, Novo_Arg, Novo_TermoC) :-
    TermoC =.. [F|Argumentos],
    substitui_elemento_lista(Argumentos, Arg, Novo_Arg, Novo_Args),
    Novo_TermoC =.. [F|Novo_Args].



% quantos/3
% ?- quantos(par, [1,4,5], X).
% X = 1.

% aux
par(N) :- N mod 2 =:= 0.

quantos(Predicado, Lista, Quantos) :-
    findall(Elemento, (member(Elemento, Lista), Termo_composto =.. [Predicado|[Elemento]], Termo_composto), ListaPares),
    length(ListaPares, Quantos).



% transforma/3
% ?- transforma(soma_1, [2,4,6], L).
% L = [3,5,7].

soma_1(X,Y) :- Y is X + 1.

% transformaEasy(Predicado, L1, L2) :- maplist(Predicado, L1, L2).

transforma(Predicado, L1, L2) :- transforma(Predicado, L1, L2, []).

transforma(_, [], L, L) :- !.

transforma(Predicado, [P|R], L2, Ac) :-
    TermoC =.. [Predicado|[P, Aux]],
    TermoC,
    append(Ac, [Aux], AcAux),
    transforma(Predicado, R, L2, AcAux).
