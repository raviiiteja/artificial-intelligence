% Database of people with Name and Date of Birth

person(john, '10-05-2000').
person(mary, '15-08-2001').
person(alex, '20-12-1999').
person(jason, '25-03-2002').

% Rule to find the date of birth of a person
dob(Name, Date) :-
    person(Name, Date).